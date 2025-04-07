from fastapi import FastAPI
from app.routers import book_router

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="Book Management API",
    description="FastAPI를 사용한 도서 관리 API (MVC 패턴 적용)",
    version="2.0.0"
)

# 라우터 등록
app.include_router(book_router.router)

# 루트 경로
@app.get("/")
async def root():
    """API 루트 경로"""
    return {
        "message": "Welcome to the Book Management API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
