from fastapi import APIRouter
from model.producto import ProductoCreate, ProductoPublic, ProductoUpdate
from data_base import session_dep
from domain.imp_producto import ImpProducto


router = APIRouter()

@router.get("/productos", response_model=list[ProductoPublic])
def read_productos(
    session: session_dep,
):
    return ImpProducto.get_productos(session)

@router.get("/producto/{codigo_de_barras}", response_model=ProductoPublic)
def read_producto(
    codigo_de_barras: str,
    session: session_dep,
):
    return ImpProducto.get_producto(codigo_de_barras, session)

@router.post("/producto", response_model=ProductoPublic)
def create_producto(
    producto: ProductoCreate,
    session: session_dep,
):
    return ImpProducto.create_producto(producto, session)


@router.patch("/producto/{producto_id}", response_model=ProductoPublic)
def update_producto(
    producto_id: int,
    producto: ProductoUpdate,
    session: session_dep,
):
    return ImpProducto.update_producto(producto_id, producto, session)


@router.delete("/producto/{producto_id}")
def delete_producto(
    producto_id: int,
    session: session_dep,
):
    return ImpProducto.delete_producto(producto_id, session)
