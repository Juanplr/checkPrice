from fastapi import HTTPException
from model.categoria import Categoria
from model.usuario import Usuario
from model.producto import Producto, ProductoCreate, ProductoUpdate
from sqlmodel import select
from data_base import session_dep


class ImpProducto():
    
    @staticmethod
    def get_productos(session: session_dep):
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
       if not productos: 
           raise HTTPException(status_code=404, detail="No se encontraron productos")
       return productos
    
    @staticmethod
    def get_producto(codigo_de_barras: str, session: session_dep):
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
        .where(Producto.codigo_de_barras == codigo_de_barras)
    )
        producto = session.exec(statement).first()
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto
        
    @staticmethod
    def create_producto(producto: ProductoCreate, session: session_dep):
        db_producto = Producto.model_validate(producto)
        session.add(db_producto)
        session.commit()
        session.refresh(db_producto)
        return db_producto
    
    @staticmethod
    def update_producto(producto_id: int, producto: ProductoUpdate, session: session_dep):
        db_producto = session.get(Producto, producto_id)
        if not db_producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        for key, value in producto.model_dump().items():
            setattr(db_producto, key, value)
        session.add(db_producto)
        session.commit()
        session.refresh(db_producto)
        return db_producto
    
    @staticmethod
    def delete_producto(producto_id: int, session: session_dep):
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        session.delete(producto)
        session.commit()
        return {"message": "Producto eliminado"}