import logging

from app.db.base import SessionLocal, engine, Base
from app.core.config import settings
from app.schemas.user import UserCreate
from app.crud.user import get_user_by_email, create_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db() -> None:
    """데이터베이스 테이블 생성"""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")

def init() -> None:
    """초기 데이터 생성"""
    db = SessionLocal()
    try:
        # 관리자 계정 생성
        user = get_user_by_email(db, email=settings.FIRST_SUPERUSER)
        if not user:
            user_in = UserCreate(
                email=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                is_superuser=True,
            )
            user = create_user(db, user_in)
            logger.info("Superuser created")
    finally:
        db.close()

def main() -> None:
    logger.info("Creating initial data")
    init_db()
    init()
    logger.info("Initial data created")

if __name__ == "__main__":
    main()
