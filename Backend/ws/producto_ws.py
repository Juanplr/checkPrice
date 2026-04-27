from fastapi import APIRouter, HTTPException
from model.producto import Producto, ProductoPublic, ProductoUpdate
from model.usuario import Usuario
from model.categoria import Categoria
from data_base import session_dep
from sqlmodel import select


router = APIRouter()

@router.get("/productos", response_model=list[ProductoPublic])
def read_productos(
    session: session_dep,
):
    statement = (
        select(
            Producto.id,
            Producto.nombre,
            Producto.codigo_de_barras,
            Producto.precio,
            Usuario.nombre.label("nombre_usuario"),
            Categoria.nombre.label("nombre_categoria")
        )
        .join(Usuario, Producto.id_usuario == Usuario.id)
        .join(Categoria, Producto.id_categoria == Categoria.id)
    )
    productos = session.exec(statement).all()
    return productos

@router.get("/producto/{producto_id}", response_model=ProductoPublic)
def read_producto(
    producto_id: int,
    session: session_dep,
):
    statement = (
        select(
            Producto.id,
            Producto.nombre,
            Producto.codigo_de_barras,
            Producto.precio,
            Usuario.nombre.label("nombre_usuario"),
            Categoria.nombre.label("nombre_categoria")
        )
        .join(Usuario, Producto.id_usuario == Usuario.id)
        .join(Categoria, Producto.id_categoria == Categoria.id)
        .where(Producto.id == producto_id)
    )
    producto = session.exec(statement).first()
    return producto

@router.post("/producto", response_model=ProductoPublic)
def create_producto(
    producto: Producto,
    session: session_dep,
):
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


@router.patch("/producto/{producto_id}", response_model=ProductoPublic)
def update_producto(
    producto_id: int,
    producto: ProductoUpdate,
    session: session_dep,
):
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        return HTTPException(status_code=404, content="Producto no encontrado")
    for key, value in producto.model_dump().items():
        setattr(db_producto, key, value)
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto

@router.delete("/producto/{producto_id}")
def delete_producto(
    producto_id: int,
    session: session_dep,
):
    producto = session.get(Producto, producto_id)
    if not producto:
        return HTTPException(status_code=404, content="Producto no encontrado")
    session.delete(producto)
    session.commit()
    return {"message": "Producto eliminado"}
