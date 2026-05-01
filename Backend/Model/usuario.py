from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class UsuarioBase(SQLModel):
    nombre: str = Field(index=True)
    user_name: str
    es_administrador: bool

class Usuario(UsuarioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    correo:EmailStr
    contrasena: str

class UsuarioPublic(UsuarioBase):
    id: int
    correo:EmailStr

class UsuarioCreate(UsuarioBase):
    correo:EmailStr
    contrasena: str
    
class UsuarioUpdate(UsuarioBase):
    nombre: str | None = None
    user_name: str | None = None
    es_administrador: bool | None = None
    correo:EmailStr | None = None
    contrasena: str | None = None