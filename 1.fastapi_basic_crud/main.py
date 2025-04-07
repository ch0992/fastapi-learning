# 필요한 모듈 임포트
from fastapi import FastAPI, HTTPException  # FastAPI 프레임워크와 예외 처리를 위한 모듈
from pydantic import BaseModel      # 데이터 검증을 위한 Pydantic 모델
from typing import List, Optional   # 타입 힌트를 위한 typing 모듈
from datetime import datetime       # 날짜/시간 처리를 위한 datetime 모듈

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 책 데이터 모델 정의
class Book(BaseModel):
    id: int                         # 책 고유 ID
    title: str                      # 책 제목
    author: str                     # 저자
    published_year: int             # 출판년도
    isbn: str                       # ISBN 번호
    description: Optional[str] = None  # 책 설명 (선택적)

# 테스트를 위한 샘플 데이터
books = [
    Book(
        id=1,
        title="Python Programming",
        author="John Doe",
        published_year=2023,
        isbn="978-1234567890",
        description="A comprehensive guide to Python"
    ),
    Book(
        id=2,
        title="FastAPI Master",
        author="Jane Smith",
        published_year=2024,
        isbn="978-0987654321",
        description="Learn FastAPI development"
    )
]

# 1. Create (POST /books/)
@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    """
    새로운 책을 생성합니다.
    - book: 생성할 책의 정보
    - returns: 생성된 책 정보
    - raises: 400 Bad Request (ID 중복 시)
    """
    # ID 중복 검사
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    # 새 책 추가
    books.append(book)
    return book

# 2. Read - 모든 책 조회 (GET /books/)
@app.get("/books/", response_model=List[Book])
async def read_books():
    """
    모든 책 목록을 반환합니다.
    - returns: 책 목록
    """
    return books

# 3. Read - 특정 책 조회 (GET /books/{book_id})
@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    """
    특정 ID의 책을 찾아 반환합니다.
    - book_id: 찾으려는 책의 ID
    - returns: 찾은 책 정보
    - raises: 404 Not Found (책을 찾지 못한 경우)
    """
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# 4. Update (PUT /books/{book_id})
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    """
    특정 ID의 책 정보를 업데이트합니다.
    - book_id: 업데이트할 책의 ID
    - updated_book: 새로운 책 정보
    - returns: 업데이트된 책 정보
    - raises: 404 Not Found (책을 찾지 못한 경우)
    """
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# 5. Delete (DELETE /books/{book_id})
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """
    특정 ID의 책을 삭제합니다.
    - book_id: 삭제할 책의 ID
    - returns: 삭제 성공 메시지
    - raises: 404 Not Found (책을 찾지 못한 경우)
    """
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
