from fastapi import APIRouter, Depends
from model.producto import ProductoCreate, ProductoPublic, ProductoUpdate
from data_base import session_dep
from domain.imp_producto import ImpProducto
from domain.imp_token import get_current_active_user
from typing import Annotated
from model.usuario import UsuarioPublic


router = APIRouter(
    prefix="/producto",
    tags=["producto"],
    responses={404: {"description": "Not found"}},
)

@router.get("s", response_model=list[ProductoPublic])
def read_productos(
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpProducto.get_productos(session)

@router.get("/{codigo_de_barras}", response_model=ProductoPublic)
def read_producto(
    codigo_de_barras: str,
    session: session_dep,
):
    return ImpProducto.get_producto(codigo_de_barras, session)

@router.post("/", response_model=ProductoPublic)
def create_producto(
    producto: ProductoCreate,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpProducto.create_producto(producto, session)


@router.patch("/{producto_id}", response_model=ProductoPublic)
def update_producto(
    producto_id: int,
    producto: ProductoUpdate,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpProducto.update_producto(producto_id, producto, session)


@router.delete("/{producto_id}")
def delete_producto(
    producto_id: int,
    session: session_dep,
    current_user: Annotated[UsuarioPublic, Depends(get_current_active_user)],
):
    return ImpProducto.delete_producto(producto_id, session)
