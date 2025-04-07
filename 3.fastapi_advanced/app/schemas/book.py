# 파이썬 타입 힌트 모듈에서 Optional 타입 가져오기
from typing import Optional
# Pydantic의 기본 모델 클래스 가져오기
from pydantic import BaseModel

class BookBase(BaseModel):
    """책 기본 스키마 - 모든 책 관련 스키마의 기본 클래스
    
    모든 필드가 Optional로 선언되어 있어 선택적으로 사용 가능
    """
    # 책 제목 (선택적)
    title: Optional[str] = None
    # 저자 이름 (선택적)
    author: Optional[str] = None
    # 출판년도 (선택적)
    published_year: Optional[int] = None
    # ISBN (선택적)
    isbn: Optional[str] = None
    # 책 설명 (선택적)
    description: Optional[str] = None

class BookCreate(BookBase):
    """책 생성 스키마 - 새로운 책을 만들 때 사용
    
    BookBase를 상속하지만 필수 필드들을 Optional이 아닌 필수값으로 재정의
    """
    # 책 제목 (필수)
    title: str
    # 저자 이름 (필수)
    author: str
    # 출판년도 (필수)
    published_year: int
    # ISBN (필수)
    isbn: str

class BookUpdate(BookBase):
    """책 업데이트 스키마 - 기존 책 정보를 업데이트할 때 사용
    
    BookBase를 그대로 사용하여 모든 필드가 선택적
    업데이트하고 싶은 필드만 전달하면 됨
    """
    pass

class Book(BookBase):
    """책 스키마 - 데이터베이스의 책 정보를 API 응답으로 보낼 때 사용
    
    BookBase를 상속하며 추가로 데이터베이스 필드들 포함
    """
    # 책의 고유 ID (데이터베이스에서 자동 생성)
    id: int
    # 책 소유자의 ID
    user_id: int

    class Config:
        # ORM 모드 활성화 - SQLAlchemy 모델을 Pydantic 모델로 자동 변환 가능
        orm_mode = True
        # 임의의 타입 허용 - SQLAlchemy 모델의 모든 타입 허용
        arbitrary_types_allowed = True
