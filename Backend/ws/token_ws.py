from fastapi import APIRouter, Depends
from data_base import session_dep
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from model.token import Token
from domain.imp_token import token_usuario

router = APIRouter(
    prefix="/token",
    tags=["token"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
def login_usuario(
    session: session_dep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    return token_usuario(form_data, session)