from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.base_class import Base

# Import all models for SQLAlchemy to detect them
from app.db.models.user import User
from app.db.models.book import Book

# SQLAlchemy 엔진 생성
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    """데이터베이스 세션 의존성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
