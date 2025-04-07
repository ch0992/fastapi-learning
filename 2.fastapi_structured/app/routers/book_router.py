from fastapi import APIRouter, Depends
from typing import List
from app.models.book import Book
from app.services.book_service import BookService

# 라우터 생성
router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

# 서비스 의존성 주입을 위한 함수
def get_book_service():
    return BookService()

@router.get("/", response_model=List[Book])
async def read_books(book_service: BookService = Depends(get_book_service)):
    """모든 책 목록을 조회합니다."""
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=Book)
async def read_book(
    book_id: int,
    book_service: BookService = Depends(get_book_service)
):
    """특정 ID의 책을 조회합니다."""
    return book_service.get_book_by_id(book_id)

@router.post("/", response_model=Book)
async def create_book(
    book: Book,
    book_service: BookService = Depends(get_book_service)
):
    """새로운 책을 생성합니다."""
    return book_service.create_book(book)

@router.put("/{book_id}", response_model=Book)
async def update_book(
    book_id: int,
    book: Book,
    book_service: BookService = Depends(get_book_service)
):
    """특정 ID의 책을 업데이트합니다."""
    return book_service.update_book(book_id, book)

@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    book_service: BookService = Depends(get_book_service)
):
    """특정 ID의 책을 삭제합니다."""
    return book_service.delete_book(book_id)
