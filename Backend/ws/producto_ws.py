from fastapi import APIRouter
from model.producto import Producto, ProductoPublic
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

    