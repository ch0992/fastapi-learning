from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """토큰 스키마"""
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """토큰 페이로드 스키마"""
    sub: Optional[int] = None
