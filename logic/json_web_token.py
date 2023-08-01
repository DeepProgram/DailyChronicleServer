from datetime import timedelta, datetime
from typing import Optional
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "TWINGHOPURY"
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


def create_jwt_access_token(user_id: str, expires_delta: Optional[timedelta]) -> str:
    encode = {
        "sub": "DEEP WEB", "id": user_id,
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)
    encode["exp"] = expire
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
