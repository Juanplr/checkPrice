from fastapi import APIRouter, HTTPException
from model.categoria import Categoria, CategoriaPublic, CategoriaUpdate
from data_base import session_dep
from sqlmodel import select

router = APIRouter()

@router.get("/categorias", response_model=list[CategoriaPublic])
def read_categorias(
    session: session_dep,
):
    categorias = session.exec(select(Categoria)).all()
    return categorias

@router.get("/categoria/{categoria_id}", response_model=CategoriaPublic)
def read_categoría(
    categoria_id: int,
    session: session_dep,
):
    categoria = session.exec(select(Categoria, categoria_id))
    if not categoria:
        return HTTPException(status_code=404, content="Categoría no encontrada")
    return categoria

@router.post("/categoria", response_model=CategoriaPublic)
def create_categoría(
    categoria: Categoria,
    session: session_dep,
):
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

@router.patch("/categoria/{categoria_id}", response_model=CategoriaPublic)
def update_categoría(
    categoria_id: int,
    categoria: CategoriaUpdate,
    session: session_dep,
):
    db_categoría = session.get(Categoria, categoria_id)
    if not db_categoría:
        return HTTPException(status_code=404, content="Categoría no encontrada")
    for key, value in categoria.model_dump().items():
        setattr(db_categoría, key, value)
    session.add(db_categoría)
    session.commit()
    session.refresh(db_categoría)
    return db_categoría

@router.delete("/categoria/{categoria_id}")
def delete_categoría(
    categoria_id: int,
    session: session_dep,
):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return HTTPException(status_code=404, content="Categoría no encontrada")
    session.delete(categoria)
    session.commit()
    return {"message": "Categoría eliminada"}