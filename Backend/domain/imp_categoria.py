from fastapi import HTTPException
from model.categoria import Categoria, CategoriaCreate, CategoriaUpdate
from sqlmodel import select
from data_base import session_dep
from sqlalchemy.exc import IntegrityError as ExceptionIntegrityError

class ImpCategoria():
    
    @staticmethod
    def get_categorias(session: session_dep):
        categorias = session.exec(select(Categoria)).all()
        if not categorias:
            raise HTTPException(status_code=404, detail="No se encontraron categorías")
        return categorias
    
    @staticmethod
    def get_categoria(categoria_id: int, session: session_dep):
        categoria = session.get(Categoria, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return categoria
    
    @staticmethod
    def create_categoria(categoria: CategoriaCreate, session: session_dep):
        db_categoria = Categoria.model_validate(categoria)
        session.add(db_categoria)
        session.commit()
        session.refresh(db_categoria)
        return db_categoria
    
    @staticmethod
    def update_categoria(categoria_id: int, categoria: CategoriaUpdate, session: session_dep):
        db_categoria = session.get(Categoria, categoria_id)
        if not db_categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        for key, value in categoria.model_dump().items():
            setattr(db_categoria, key, value)
        session.add(db_categoria)
        session.commit()
        session.refresh(db_categoria)
        return db_categoria
    
    @staticmethod
    def delete_categoria(categoria_id: int, session: session_dep):
        try:
            categoria = session.get(Categoria, categoria_id)
            if not categoria:
                raise HTTPException(status_code=404, detail="Categoría no encontrada")
            session.delete(categoria)
            session.commit()
            return {"message": "Categoría eliminada"}
        except ExceptionIntegrityError as e:
            raise HTTPException(status_code=500, detail="Esta categoria está asociada a uno o más productos y no se puede eliminar")
    
    
    