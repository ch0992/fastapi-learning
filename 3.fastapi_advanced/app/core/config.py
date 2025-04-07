# 안전한 랜덤 토큰 생성을 위한 모듈
import secrets
# 파이썬 타입 힌트를 위한 모듈
from typing import Any, Dict, List, Optional, Union
# Pydantic의 환경변수 및 유효성 검사 관련 클래스들
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    """애플리케이션의 환경변수와 설정값들을 관리하는 클래스
    
    모든 설정값은 환경변수나 .env 파일에서 가져올 수 있으며,
    값이 없는 경우 여기서 정의된 기본값을 사용합니다.
    """
    # API 버전 경로 (기본값: /api/v1)
    API_V1_STR: str = "/api/v1"
    
    # JWT 토큰 생성에 사용될 비밀키
    # 기본값: 32바이트 랜덤 URL-safe 토큰
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    # JWT 토큰 만료 시간 (8일)
    # 60분 * 24시간 * 8일 = 11,520분
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # CORS 설정: 허용된 원본(Origin) 목록
    # JSON 형식의 URL 목록으로 지정
    # 예: '["http://localhost", "http://localhost:4200"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """백엔드 CORS 원본 목록을 파싱합니다.
        
        Args:
            v: 원본 목록 (문자열 또는 목록)
        
        Returns:
            Union[List[str], str]: 파싱된 원본 목록
        
        Raises:
            ValueError: 잘못된 형식의 입력값
        """
        # 콤마로 구분된 문자열인 경우
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        # JSON 목록 또는 단일 URL인 경우
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # 프로젝트 이름 (필수)
    PROJECT_NAME: str
    
    # 데이터베이스 연결 URL (필수)
    # 예: sqlite:///./sql_app.db
    DATABASE_URL: str

    # 초기 관리자 계정 설정
    FIRST_SUPERUSER: EmailStr  # 관리자 이메일
    FIRST_SUPERUSER_PASSWORD: str  # 관리자 비밀번호

    class Config:
        # 환경변수 이름의 대소문자를 구분
        case_sensitive = True
        # 환경변수 파일 위치
        env_file = ".env"


# 싱글톤 설정 객체 생성
# 이 객체를 통해 전역적으로 설정값에 접근 가능
settings = Settings()
