from fastapi import APIRouter, Depends
from model.categoria import CategoriaCreate, CategoriaPublic, CategoriaUpdate
from data_base import session_dep
from domain.imp_categoria import ImpCategoria
from domain.imp_token import get_current_active_user
from typing import Annotated
from model.usuario import UsuarioPublic

router = APIRouter(
    prefix="/categoria",
    tags=["categoria"],
    responses={404: {"description": "Not found"}},
)

@router.get("s", response_model=list[CategoriaPublic])
def read_categorias(
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpCategoria.get_categorias(session)

@router.get("/{categoria_id}", response_model=CategoriaPublic)
def read_categoria(
    categoria_id: int,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpCategoria.get_categoria(categoria_id, session)

@router.post("/", response_model=CategoriaPublic)
def create_categoría(
    categoria: CategoriaCreate,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpCategoria.create_categoria(categoria, session)

@router.patch("/{categoria_id}", response_model=CategoriaPublic)
def update_categoría(
    categoria_id: int,
    categoria: CategoriaUpdate,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpCategoria.update_categoria(categoria_id, categoria, session)

@router.delete("/{categoria_id}")
def delete_categoría(
    categoria_id: int,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpCategoria.delete_categoria(categoria_id, session)