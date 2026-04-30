from fastapi import APIRouter
from model.categoria import CategoriaCreate, CategoriaPublic, CategoriaUpdate
from data_base import session_dep
from domain.imp_categoria import ImpCategoria

router = APIRouter()

@router.get("/categorias", response_model=list[CategoriaPublic])
def read_categorias(
    session: session_dep,
):
    return ImpCategoria.get_categorias(session)

@router.get("/categoria/{categoria_id}", response_model=CategoriaPublic)
def read_categoria(
    categoria_id: int,
    session: session_dep,
):
    return ImpCategoria.get_categoria(categoria_id, session)

@router.post("/categoria", response_model=CategoriaPublic)
def create_categoría(
    categoria: CategoriaCreate,
    session: session_dep,
):
    return ImpCategoria.create_categoria(categoria, session)

@router.patch("/categoria/{categoria_id}", response_model=CategoriaPublic)
def update_categoría(
    categoria_id: int,
    categoria: CategoriaUpdate,
    session: session_dep,
):
    return ImpCategoria.update_categoria(categoria_id, categoria, session)

@router.delete("/categoria/{categoria_id}")
def delete_categoría(
    categoria_id: int,
    session: session_dep,
):
    return ImpCategoria.delete_categoria(categoria_id, session)