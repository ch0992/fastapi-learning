from fastapi import FastAPI
from app.routers import item_router

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="FastAPI Boilerplate",
    description="FastAPI Boilerplate with Structured Project Layout",
    version="1.0.0"
)

# 라우터 등록
app.include_router(item_router.router)

# 루트 경로
@app.get("/")
async def root():
    """API 루트 경로"""
    return {
        "message": "Welcome to the FastAPI Boilerplate",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
