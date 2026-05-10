from fastapi import APIRouter, Query
from typing import Annotated
from model.usuario import UsuarioCreate, UsuarioPublic, UsuarioUpdate
from data_base import session_dep
from domain.imp_usuario import ImpUsuario
from pydantic import EmailStr

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

@router.get("/login/{correo}/{contrasena}", response_model=UsuarioPublic)
def login_usuario(
    correo: EmailStr,
    contrasena: str,
    session: session_dep,
):
    return ImpUsuario.login_usuario(correo, contrasena, session)