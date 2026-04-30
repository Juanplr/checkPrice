from fastapi import APIRouter, Query
from typing import Annotated
from model.usuario import UsuarioCreate, UsuarioPublic, UsuarioUpdate
from data_base import session_dep
from domain.imp_usuario import ImpUsuario

router = APIRouter()

@router.get("/usuarios", response_model=list[UsuarioPublic])
def read_usuarios(
    session: session_dep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    return ImpUsuario.get_usuarios(session, offset, limit)


@router.get("/usuario/{usuario_id}", response_model=UsuarioPublic)
def read_usuario(
    usuario_id: int,
    session: session_dep,
):
    return ImpUsuario.get_usuario(usuario_id, session)


@router.post("/usuario", response_model=UsuarioPublic)
def create_usuario(
    usuario: UsuarioCreate,
    session: session_dep,
):
    return ImpUsuario.create_usuario(usuario, session)


@router.patch("/usuario/{usuario_id}",response_model=UsuarioPublic)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    session: session_dep,
):
    return ImpUsuario.update_usuario(usuario_id, usuario, session)


@router.delete("/usuario/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    session: session_dep,
):
    return ImpUsuario.delete_usuario(usuario_id, session)