# 파이썬 표준 타입 힌트 모듈
from typing import Generator, Optional
# FastAPI 핵심 기능
from fastapi import Depends, HTTPException, status
# OAuth2 비밀번호 기반 인증
from fastapi.security import OAuth2PasswordBearer
# JWT 토큰 처리를 위한 라이브러리
from jose import jwt
# Pydantic 데이터 검증 오류
from pydantic import ValidationError
# SQLAlchemy 데이터베이스 세션
from sqlalchemy.orm import Session

# 애플리케이션 내부 모듈
# 보안 관련 유틸리티
from app.core import security
# 환경 설정
from app.core.config import settings
# 데이터베이스 연결 관리
from app.db.base import get_db
# 사용자 데이터베이스 모델
from app.db.models.user import User
# JWT 토큰 페이로드 스키마
from app.schemas.token import TokenPayload
# 사용자 CRUD 작업
from app.crud import user as crud_user

# OAuth2 인증 처리기 인스턴스 생성
# tokenUrl: 토큰을 발급하는 엔드포인트 URL 지정
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

# 현재 인증된 사용자 정보를 가져오는 의존성 함수
def get_current_user(
    # 데이터베이스 세션 의존성
    db: Session = Depends(get_db),
    # OAuth2 인증 토큰 의존성 (헤더에서 추출)
    token: str = Depends(reusable_oauth2)
) -> User:
    """현재 인증된 사용자 가져오기"""
    try:
        # JWT 토큰 복호화 (서명 검증)
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        # 토큰 데이터를 TokenPayload 모델로 검증
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        # JWT 토큰 검증 실패 시 403 오류 발생
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    # 토큰에서 추출한 사용자 ID로 사용자 정보 조회
    user = crud_user.get_user(db, user_id=token_data.sub)
    if not user:
        # 사용자가 존재하지 않는 경우 404 오류 발생
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 현재 활성화된 사용자 정보를 가져오는 의존성 함수
def get_current_active_user(
    # get_current_user 함수의 결과를 의존성으로 사용
    current_user: User = Depends(get_current_user),
) -> User:
    """현재 활성화된 사용자 가져오기"""
    # 사용자 계정이 비활성화된 경우 400 오류 발생
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# 현재 활성화된 관리자 사용자 정보를 가져오는 의존성 함수
def get_current_active_superuser(
    # get_current_user 함수의 결과를 의존성으로 사용
    current_user: User = Depends(get_current_user),
) -> User:
    """현재 활성화된 관리자 사용자 가져오기"""
    # 사용자가 관리자가 아닌 경우 403 오류 발생
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
