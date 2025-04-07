# FastAPI: 현대적인 웹 프레임워크로, 빠른 API 개발을 위한 다양한 기능 제공
from fastapi import FastAPI
# CORS: 다른 도메인의 리소스 요청을 허용하기 위한 미들웨어
from starlette.middleware.cors import CORSMiddleware

# 프로젝트 내부 모듈 임포트
# api_router: API 엔드포인트들을 그룹화한 라우터
from app.api.v1.router import api_router
# settings: 환경 설정 값들을 담고 있는 객체
from app.core.config import settings
# Base: SQLAlchemy 모델의 기본 클래스, engine: 데이터베이스 연결 관리 객체
from app.db.base import Base, engine

# 애플리케이션 시작 시 데이터베이스 테이블 자동 생성
# SQLAlchemy의 모든 모델(테이블)을 검사하여 데이터베이스에 없는 테이블을 생성
Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    # 프로젝트 이름 설정 (API 문서에 표시됨)
    title=settings.PROJECT_NAME,
    # OpenAPI 문서 URL 설정 (API 명세를 JSON 형식으로 제공)
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # Swagger UI URL 설정 (대화형 API 문서 제공)
    docs_url=f"{settings.API_V1_STR}/docs",
    # ReDoc URL 설정 (또 다른 형식의 API 문서 제공)
    redoc_url=f"{settings.API_V1_STR}/redoc",
    # API 설명 문서 (마크다운 형식 지원)
    description="""
    FastAPI Advanced Book Management System API
    
    ## Features
    * User authentication with JWT
    * Book management with CRUD operations
    * Role-based access control
    """,
    # API 버전 정보
    version="1.0.0",
)

# CORS 설정
# 프론트엔드가 다른 도메인에서 이 API에 접근할 수 있도록 허용
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # 허용할 출처(도메인) 목록 설정
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # 인증 정보(쿠키 등)를 포함한 요청 허용
        allow_credentials=True,
        # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
        allow_methods=["*"],
        # 모든 HTTP 헤더 허용
        allow_headers=["*"],
    )

# API 라우터를 애플리케이션에 등록
# prefix를 사용하여 모든 API 엔드포인트 앞에 버전 정보 추가 (예: /api/v1/...)
app.include_router(api_router, prefix=settings.API_V1_STR)
