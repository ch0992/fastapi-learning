# 날짜와 시간 처리를 위한 모듈
from datetime import timedelta
# 파이썬 타입 힌트를 위한 모듈
from typing import Any

# FastAPI 관련 모듈
from fastapi import APIRouter, Depends, HTTPException
# OAuth2 인증 관련 모듈
from fastapi.security import OAuth2PasswordRequestForm
# SQLAlchemy 세션 관리를 위한 모듈
from sqlalchemy.orm import Session

# 프로젝트 내부 모듈
from app.api.dependencies.auth import get_current_user  # 현재 사용자 가져오기
from app.core import security  # 보안 관련 함수들
from app.core.config import settings  # 환경변수와 설정값들
from app.db.base import get_db  # 데이터베이스 세션 가져오기
from app.schemas.token import Token  # 토큰 스키마
from app.crud import user as crud_user  # 사용자 CRUD 작업
from app.schemas import user as user_schema  # 사용자 스키마
from app.db.models.user import User  # 사용자 데이터베이스 모델

# 로그인 관련 라우터 생성
router = APIRouter()

@router.post("/access-token", response_model=Token, response_model_exclude_unset=True)
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """사용자 로그인을 처리하고 JWT 토큰을 발급합니다.
    
    OAuth2 호환 형식의 로그인을 제공하며, 인증이 성공하면 JWT 토큰을 반환합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        form_data (OAuth2PasswordRequestForm): 사용자 이메일과 비밀번호가 포함된 폼 데이터
    
    Returns:
        dict: access_token과 token_type이 포함된 응답
    
    Raises:
        HTTPException: 이메일/비밀번호가 잘못되었거나 비활성화된 사용자인 경우
    """
    # 사용자 인증 시도
    user = crud_user.authenticate(
        db,
        email=form_data.username,  # OAuth2에서는 이메일을 username으로 전달
        password=form_data.password
    )
    
    # 인증 실패 처리
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    # 비활성화된 사용자 처리
    elif not user.is_active:
        raise HTTPException(
            status_code=400,
            detail="Inactive user"
        )
    
    # 토큰 만료 시간 설정
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # JWT 토큰 생성 및 반환
    return {
        "access_token": security.create_access_token(
            user.id,  # 사용자 ID를 토큰에 포함
            expires_delta=access_token_expires  # 만료 시간 설정
        ),
        "token_type": "bearer",  # Bearer 토큰 형식 사용
    }

@router.post("/test-token", response_model=user_schema.User, response_model_exclude_unset=True)
def test_token(current_user: User = Depends(get_current_user)) -> Any:
    """토큰의 유효성을 테스트하고 현재 사용자 정보를 반환합니다.
    
    이 엔드포인트는 JWT 토큰의 유효성을 테스트하고,
    유효한 토큰을 가진 사용자의 정보를 반환합니다.
    
    Args:
        current_user (User): 현재 인증된 사용자 (자동으로 주입됨)
    
    Returns:
        User: 현재 사용자 정보
    """
    return current_user
