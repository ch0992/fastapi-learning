# 날짜와 시간 처리를 위한 datetime 모듈
from datetime import datetime, timedelta
# 파이썬 타입 힌트를 위한 typing 모듈
from typing import Any, Union
# JWT(인증 토큰) 처리를 위한 PyJWT 라이브러리
from jose import jwt
# 비밀번호 해시화와 검증을 위한 라이브러리
from passlib.context import CryptContext
# 환경변수와 설정값들을 가져오기 위한 모듈
from app.core.config import settings

# 비밀번호 해시화에 사용될 컨텍스트 설정
# bcrypt 알고리즘을 사용하며, 내부적으로 자동 마이그레이션 지원
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 토큰 생성에 사용될 알고리즘
# HS256: HMAC + SHA256 알고리즘
ALGORITHM = "HS256"

def create_access_token(
    subject: Union[str, Any],
    expires_delta: timedelta = None
) -> str:
    """사용자 인증을 위한 JWT 액세스 토큰을 생성합니다.
    
    Args:
        subject: 토큰의 주체 (주로 사용자 ID)
        expires_delta: 선택적 만료 시간. None이면 기본값 사용
    
    Returns:
        str: 생성된 JWT 토큰 문자열
    """
    # 만료 시간 설정
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # 기본 만료 시간 사용 (settings에서 가져옴)
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    # 토큰에 포함될 데이터 준비
    to_encode = {
        "exp": expire,  # 만료 시간
        "sub": str(subject)  # 토큰 주체 (사용자 ID)
    }
    
    # JWT 토큰 생성
    encoded_jwt = jwt.encode(
        to_encode,  # 인코딩할 데이터
        settings.SECRET_KEY,  # 서명에 사용될 비밀키
        algorithm=ALGORITHM  # 암호화 알고리즘
    )
    
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """입력된 비밀번호가 해시된 비밀번호와 일치하는지 검증합니다.
    
    Args:
        plain_password: 사용자가 입력한 원본 비밀번호
        hashed_password: 데이터베이스에 저장된 해시화된 비밀번호
    
    Returns:
        bool: 비밀번호가 일치하면 True, 아니면 False
    """
    # passlib의 verify 함수를 사용하여 비밀번호 검증
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """입력된 비밀번호를 안전하게 해시화합니다.
    
    Args:
        password: 해시화할 원본 비밀번호
    
    Returns:
        str: bcrypt로 해시화된 비밀번호
    """
    # passlib의 hash 함수를 사용하여 비밀번호 해시화
    return pwd_context.hash(password)
