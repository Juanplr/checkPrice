import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from data_base import session_dep
from model.usuario import Usuario
from sqlmodel import select
from datetime import datetime, timedelta, timezone
from typing import Annotated

load_dotenv()

SECRET_KEY = os.getenv("KEY_JWT")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    username: str | None = None
    
    
password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("dummypassword")

def get_user(session, username: str):
    statement = select(Usuario).where(Usuario.user_name == username)
    return session.exec(statement).first()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)

def authenticate_user(session: session_dep, username: str, password: str):
    user = get_user(session, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.contrasena):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(session, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[Usuario, Depends(get_current_user)],
):
    return current_user


