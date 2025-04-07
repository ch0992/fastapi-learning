from fastapi import APIRouter
from app.api.v1.endpoints import book, login, users

api_router = APIRouter()

# 각 엔드포인트 라우터 포함
api_router.include_router(
    login.router,
    prefix="/login",
    tags=["login"],
)
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)
api_router.include_router(
    book.router,
    prefix="/books",
    tags=["books"],
)
