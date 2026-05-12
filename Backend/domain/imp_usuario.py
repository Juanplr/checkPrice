from fastapi import HTTPException, status
from model.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from sqlmodel import select
from data_base import session_dep
from sqlalchemy.exc import IntegrityError as ExceptionIntegrityError
from pydantic import EmailStr
from fastapi.security import OAuth2PasswordRequestForm
from model.token import authenticate_user, Token, create_access_token, get_password_hash
from typing import Annotated
from datetime import datetime, timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
        usuario.contrasena = get_password_hash(usuario.contrasena)
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
        usuario_data = usuario.model_dump(exclude_unset=True)
        db_usuario.sqlmodel_update(usuario_data)
        session.add(db_usuario)
        session.commit()
        session.refresh(db_usuario)
        return db_usuario
    
    @staticmethod
    def delete_usuario(usuario_id: int, session: session_dep):
        try:
            usuario = session.get(Usuario, usuario_id)
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            session.delete(usuario)
            session.commit()
            return {"message": "Usuario eliminado"}
        except ExceptionIntegrityError as e:
            raise HTTPException(status_code=500, detail="Este usuario está asociado a uno o más productos y no se puede eliminar")
        
    @staticmethod
    def login_usuario(form_data: OAuth2PasswordRequestForm, session: session_dep):
        user = authenticate_user(session,form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.user_name}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")