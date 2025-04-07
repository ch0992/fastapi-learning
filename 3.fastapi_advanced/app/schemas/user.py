from typing import List, Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """사용자 기본 스키마"""
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False

class UserCreate(UserBase):
    """사용자 생성 스키마"""
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    """사용자 수정 스키마"""
    password: Optional[str] = None

class User(UserBase):
    """사용자 응답 스키마"""
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Token(BaseModel):
    """토큰 스키마"""
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    """토큰 페이로드 스키마"""
    sub: Optional[int] = None
