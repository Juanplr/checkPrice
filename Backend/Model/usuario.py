from sqlmodel import SQLModel, Field

class UsuarioBase(SQLModel):
    nombre: str = Field(index=True)
    user_name: str
    es_administrador: bool

class Usuario(UsuarioBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    correo:str
    contrasena: str

class UsuarioPublic(UsuarioBase):
    id: int
    correo:str

class UsuarioCreate(UsuarioBase):
    correo:str
    contrasena: str
    
class UsuarioUpdate(UsuarioBase):
    nombre: str | None = None
    user_name: str | None = None
    es_administrador: bool | None = None
    correo:str | None = None
    contrasena: str | None = None