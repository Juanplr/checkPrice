from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
from model.usuario import UsuarioCreate, UsuarioPublic, Usuario, UsuarioUpdate
from data_base import session_dep
from sqlmodel import select

router = APIRouter()

@router.get("/usuarios", response_model=list[UsuarioPublic])
def read_usuarios(
    session: session_dep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return usuarios

@router.get("/usuario/{usuario_id}", response_model=UsuarioPublic)
def read_usuario(
    usuario_id: int,
    session: session_dep,
):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return usuario


@router.post("/usuario", response_model=UsuarioPublic)
def create_usuario(
    usuario: UsuarioCreate,
    session: session_dep,
):
    db_usuario = Usuario.model_validate(usuario)
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario


@router.patch("/usuario/{usuario_id}",response_model=UsuarioPublic)
def update_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    session: session_dep,
):
    db_usuario = session.get(Usuario, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    for key, value in usuario.model_dump().items():
        setattr(db_usuario, key, value)
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario


@router.delete("/usuario/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    session: session_dep,
):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    session.delete(usuario)
    session.commit()
    return {"message": "Usuario eliminado"}