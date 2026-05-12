from fastapi import APIRouter, Query, Depends
from typing import Annotated
from model.usuario import UsuarioCreate, UsuarioPublic, UsuarioUpdate, Usuario
from data_base import session_dep
from domain.imp_usuario import ImpUsuario
from pydantic import EmailStr
from fastapi.security import OAuth2PasswordRequestForm
from model.token import Token, get_current_active_user

router = APIRouter(
    prefix="/usuario",
    tags=["usuario"],
    responses={404: {"description": "Not found"}},
)


@router.get("s", response_model=list[UsuarioPublic])
def read_usuarios(
    session: session_dep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    return ImpUsuario.get_usuarios(session, offset, limit)


@router.get("/{usuario_id}", response_model=UsuarioPublic)
def read_usuario(
    usuario_id: int,
    session: session_dep,
    current_user: Annotated[Usuario, Depends(get_current_active_user)]
):
    return ImpUsuario.get_usuario(usuario_id, session)


@router.post("/", response_model=UsuarioPublic)
def create_usuario(
    usuario: UsuarioCreate,
    session: session_dep,
):
    return ImpUsuario.create_usuario(usuario, session)


@router.patch("/{usuario_id}",response_model=UsuarioPublic)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    session: session_dep,
):
    return ImpUsuario.update_usuario(usuario_id, usuario, session)


@router.delete("/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    session: session_dep,
):
    return ImpUsuario.delete_usuario(usuario_id, session)

@router.post("/login")
async def login_usuario(
    session: session_dep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    return ImpUsuario.login_usuario(form_data, session)