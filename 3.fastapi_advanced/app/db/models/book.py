# SQLAlchemy의 데이터베이스 테이블 정의를 위한 타입들
from sqlalchemy import Column, Integer, String, Text, ForeignKey
# SQLAlchemy의 관계 설정을 위한 함수
from sqlalchemy.orm import relationship
# 모든 모델의 기본 클래스
from app.db.base_class import Base

class Book(Base):
    """책 모델 - 데이터베이스의 books 테이블을 표현
    
    속성:
        id: 기본 키
        title: 책 제목
        author: 저자
        published_year: 출판년도
        isbn: 국제 표준 도서 번호
        description: 책 설명
        user_id: 소유자 ID (외래 키)
        user: 소유자 객체와의 관계
    """
    # SQLAlchemy에게 이 모델이 매핑될 테이블 이름을 알려줌
    __tablename__ = "books"

    # 기본 키 - 자동 증가하는 정수형 ID
    # index=True로 설정하여 검색 성능 향상
    id = Column(Integer, primary_key=True, index=True)
    
    # 책 제목 - 최대 100자, 검색을 위한 인덱스 생성
    title = Column(String(100), index=True)
    
    # 저자 이름 - 최대 100자, 검색을 위한 인덱스 생성
    author = Column(String(100), index=True)
    
    # 출판년도 - 정수형으로 저장
    published_year = Column(Integer)
    
    # ISBN - 최대 20자, 유니크 제약 추가
    # unique=True로 설정하여 중복 ISBN 방지
    isbn = Column(String(20), unique=True, index=True)
    
    # 책 설명 - 긴 텍스트 형식, null 허용
    description = Column(Text, nullable=True)
    
    # 외래 키 관계 설정
    # users 테이블의 id를 참조하는 외래 키
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # User 모델과의 양방향 관계 설정
    # back_populates로 User 모델의 books 속성과 연결
    user = relationship("User", back_populates="books")
