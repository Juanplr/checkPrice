from fastapi import HTTPException
from model.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from sqlmodel import select
from data_base import session_dep

class ImpUsuario():
    
    @staticmethod
    def get_usuarios(session: session_dep, offset: int, limit: int):
        usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
        if not usuarios:
            raise HTTPException(status_code=404, detail="No se encontraron usuarios")
        return usuarios
    
    @staticmethod
    def get_usuario(usuario_id: int, session: session_dep):
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario
    
    @staticmethod
    def create_usuario(usuario: UsuarioCreate, session: session_dep):
        db_usuario = Usuario.model_validate(usuario)
        session.add(db_usuario)
        session.commit()
        session.refresh(db_usuario)
        return db_usuario
    
    @staticmethod
    def update_usuario(usuario_id: int, usuario: UsuarioUpdate, session: session_dep):
        db_usuario = session.get(Usuario, usuario_id)
        if not db_usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        for key, value in usuario.model_dump().items():
            setattr(db_usuario, key, value)
        session.add(db_usuario)
        session.commit()
        session.refresh(db_usuario)
        return db_usuario
    
    @staticmethod
    def delete_usuario(usuario_id: int, session: session_dep):
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        session.delete(usuario)
        session.commit()
        return {"message": "Usuario eliminado"}