from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    """책 데이터 모델
    
    Attributes:
        id (int): 책 고유 ID
        title (str): 책 제목
        author (str): 저자
        published_year (int): 출판년도
        isbn (str): ISBN 번호
        description (Optional[str]): 책 설명 (선택적)
    """
    id: int
    title: str
    author: str
    published_year: int
    isbn: str
    description: Optional[str] = None
