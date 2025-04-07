from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.api.dependencies.auth import (
    get_current_active_superuser,
    get_current_active_user,
)
from app.db.base import get_db
from app.schemas import user as user_schema
from app.crud import user as crud_user
from app.db.models.user import User

router = APIRouter()

@router.get("/", response_model=List[user_schema.User], response_model_exclude_unset=True)
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """모든 사용자 조회 (관리자 전용)"""
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=user_schema.User, response_model_exclude_unset=True)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: user_schema.UserCreate,
    current_user: User = Depends(get_current_active_superuser),
) -> Any:
    """새 사용자 생성 (관리자 전용)"""
    user = crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud_user.create_user(db, user_in)
    return user

@router.get("/me", response_model=user_schema.User, response_model_exclude_unset=True)
def read_user_me(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """현재 사용자 정보 조회"""
    return current_user

@router.put("/me", response_model=user_schema.User)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    password: str = Body(None),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """현재 사용자 정보 업데이트"""
    current_user_data = jsonable_encoder(current_user)
    user_in = user_schema.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    user = crud_user.update_user(db, db_user=current_user, user_in=user_in)
    return user

@router.get("/{user_id}", response_model=user_schema.User)
def read_user_by_id(
    user_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> Any:
    """특정 사용자 정보 조회"""
    user = crud_user.get_user(db, user_id=user_id)
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user
