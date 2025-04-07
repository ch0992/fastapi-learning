# 파이썬 타입 힌트를 위한 모듈
from typing import List, Optional
# SQLAlchemy 세션 관리를 위한 클래스
from sqlalchemy.orm import Session

# 데이터베이스 모델과 스키마 임포트
from app.db.models.book import Book  # SQLAlchemy 모델
from app.schemas.book import BookCreate, BookUpdate  # Pydantic 모델

def get_book(db: Session, book_id: int) -> Optional[Book]:
    """특정 ID의 책을 조회합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        book_id (int): 조회할 책의 ID
    
    Returns:
        Optional[Book]: 책이 존재하면 Book 객체를, 없으면 None을 반환
    """
    # 해당 ID의 책을 찾아서 반환 (없으면 None 반환)
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = None
) -> List[Book]:
    """책 목록을 조회합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        skip (int): 건너뛸 항목 수 (기본값: 0)
        limit (int): 가져올 최대 항목 수 (기본값: 100)
        user_id (Optional[int]): 특정 사용자의 책만 조회하려면 해당 사용자 ID 지정
    
    Returns:
        List[Book]: 책 목록
    """
    # 기본 쿼리 생성
    query = db.query(Book)
    
    # 특정 사용자의 책만 필터링
    if user_id:
        query = query.filter(Book.user_id == user_id)
    
    # 페이지네이션 적용 후 결과 반환
    return query.offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate, user_id: int) -> Book:
    """새로운 책을 생성합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        book (BookCreate): 생성할 책 정보
        user_id (int): 책의 소유자 ID
    
    Returns:
        Book: 생성된 책 객체
    """
    # BookCreate 스키마를 데이터베이스 모델로 변환
    db_book = Book(
        **book.dict(),  # 책 정보 펼치기
        user_id=user_id  # 소유자 ID 설정
    )
    
    # 데이터베이스에 추가
    db.add(db_book)
    # 변경사항 저장
    db.commit()
    # 생성된 객체 정보 새로고침
    db.refresh(db_book)
    
    return db_book

def update_book(
    db: Session,
    db_book: Book,
    book_in: BookUpdate
) -> Book:
    """기존 책 정보를 업데이트합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        db_book (Book): 업데이트할 기존 책 객체
        book_in (BookUpdate): 업데이트할 내용
    
    Returns:
        Book: 업데이트된 책 객체
    """
    # 설정된 값만 추출 (None인 필드 제외)
    update_data = book_in.dict(exclude_unset=True)
    
    # 각 필드를 순회하며 값 업데이트
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    # 데이터베이스에 변경사항 적용
    db.add(db_book)
    db.commit()
    # 업데이트된 객체 정보 새로고침
    db.refresh(db_book)
    
    return db_book

def delete_book(db: Session, book_id: int) -> Book:
    """특정 ID의 책을 삭제합니다.
    
    Args:
        db (Session): 데이터베이스 세션
        book_id (int): 삭제할 책의 ID
    
    Returns:
        Book: 삭제된 책 객체 (없으면 None)
    """
    # 삭제할 책 찾기
    book = db.query(Book).filter(Book.id == book_id).first()
    
    # 책이 존재하면 삭제 진행
    if book:
        db.delete(book)
        db.commit()
    
    return book
