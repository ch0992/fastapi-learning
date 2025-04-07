from typing import List, Optional
from fastapi import HTTPException
from app.models.book import Book

class BookService:
    """책 관련 비즈니스 로직을 처리하는 서비스 클래스"""
    
    def __init__(self):
        # 테스트용 초기 데이터
        self.books: List[Book] = [
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
    
    def get_all_books(self) -> List[Book]:
        """모든 책 목록을 반환합니다."""
        return self.books
    
    def get_book_by_id(self, book_id: int) -> Book:
        """ID로 특정 책을 찾아 반환합니다.
        
        Args:
            book_id: 찾으려는 책의 ID
            
        Returns:
            Book: 찾은 책 객체
            
        Raises:
            HTTPException: 책을 찾지 못한 경우
        """
        for book in self.books:
            if book.id == book_id:
                return book
        raise HTTPException(status_code=404, detail="Book not found")
    
    def create_book(self, book: Book) -> Book:
        """새로운 책을 생성합니다.
        
        Args:
            book: 생성할 책 정보
            
        Returns:
            Book: 생성된 책 객체
            
        Raises:
            HTTPException: ID가 중복되는 경우
        """
        for existing_book in self.books:
            if existing_book.id == book.id:
                raise HTTPException(status_code=400, detail="Book ID already exists")
        self.books.append(book)
        return book
    
    def update_book(self, book_id: int, updated_book: Book) -> Book:
        """책 정보를 업데이트합니다.
        
        Args:
            book_id: 업데이트할 책의 ID
            updated_book: 새로운 책 정보
            
        Returns:
            Book: 업데이트된 책 객체
            
        Raises:
            HTTPException: 책을 찾지 못한 경우
        """
        for i, book in enumerate(self.books):
            if book.id == book_id:
                self.books[i] = updated_book
                return updated_book
        raise HTTPException(status_code=404, detail="Book not found")
    
    def delete_book(self, book_id: int) -> dict:
        """책을 삭제합니다.
        
        Args:
            book_id: 삭제할 책의 ID
            
        Returns:
            dict: 삭제 성공 메시지
            
        Raises:
            HTTPException: 책을 찾지 못한 경우
        """
        for i, book in enumerate(self.books):
            if book.id == book_id:
                self.books.pop(i)
                return {"message": "Book deleted successfully"}
        raise HTTPException(status_code=404, detail="Book not found")
