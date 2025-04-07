# 파이썬 기본 타입 힌트 기능
from typing import Any, List
# FastAPI 핵심 기능들
from fastapi import APIRouter, Depends, HTTPException, status
# SQLAlchemy 세션 관리
from sqlalchemy.orm import Session

# 사용자 인증 관련 의존성
from app.api.dependencies.auth import get_current_active_user
# 데이터베이스 연결 관리
from app.db.base import get_db
# 책 관련 Pydantic 모델 (요청/응답 데이터 검증)
from app.schemas import book as book_schema
# 책 관련 데이터베이스 CRUD 작업
from app.crud import book as crud_book
# 사용자 데이터베이스 모델
from app.db.models.user import User

# API 라우터 인스턴스 생성
router = APIRouter()

# GET 메서드로 '/' 경로에 대한 요청 처리
# response_model: 응답 데이터의 형식을 Book 모델의 리스트로 지정
# response_model_exclude_unset: 기본값이 설정되지 않은 필드는 응답에서 제외
@router.get("/", response_model=List[book_schema.Book], response_model_exclude_unset=True)
def read_books(
    # 데이터베이스 세션 의존성 주입
    db: Session = Depends(get_db),
    # 페이지네이션을 위한 건너뛸 항목 수 (기본값: 0)
    skip: int = 0,
    # 한 번에 가져올 최대 항목 수 (기본값: 100)
    limit: int = 100,
    # 현재 로그인한 사용자 정보 의존성 주입
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    모든 책 조회.
    일반 사용자는 자신의 책만 조회 가능.
    관리자는 모든 책 조회 가능.
    """
    # 관리자인 경우 모든 책 조회 가능
    if current_user.is_superuser:
        books = crud_book.get_books(db, skip=skip, limit=limit)
    # 일반 사용자인 경우 자신의 책만 조회 가능
    else:
        books = crud_book.get_books(
            db, skip=skip, limit=limit, user_id=current_user.id
        )
    return books

# POST 메서드로 '/' 경로에 대한 요청 처리 (새 책 생성)
# response_model: 응답 데이터의 형식을 Book 모델로 지정
@router.post("/", response_model=book_schema.Book, response_model_exclude_unset=True)
def create_book(
    # '*'를 사용하여 이후의 모든 매개변수를 키워드 전용으로 만듦
    *,
    # 데이터베이스 세션 의존성 주입
    db: Session = Depends(get_db),
    # 요청 본문에서 책 정보를 BookCreate 모델로 검증하여 받음
    book_in: book_schema.BookCreate,
    # 현재 로그인한 사용자 정보 의존성 주입
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """새 책 생성"""
    # CRUD 모듈을 사용하여 새 책 생성
    # 현재 사용자의 ID를 책의 소유자로 설정
    book = crud_book.create_book(db=db, book=book_in, user_id=current_user.id)
    return book

@router.get("/{book_id}", response_model=book_schema.Book, response_model_exclude_unset=True)
def read_book(
    *,
    db: Session = Depends(get_db),
    book_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """특정 책 조회"""
    book = crud_book.get_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not current_user.is_superuser and (book.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return book

@router.put("/{book_id}", response_model=book_schema.Book)
def update_book(
    *,
    db: Session = Depends(get_db),
    book_id: int,
    book_in: book_schema.BookUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """책 정보 업데이트"""
    book = crud_book.get_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not current_user.is_superuser and (book.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book = crud_book.update_book(db=db, db_book=book, book_in=book_in)
    return book

@router.delete("/{book_id}", response_model=book_schema.Book)
def delete_book(
    *,
    db: Session = Depends(get_db),
    book_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """책 삭제"""
    book = crud_book.get_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not current_user.is_superuser and (book.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book = crud_book.delete_book(db=db, book_id=book_id)
    return book
