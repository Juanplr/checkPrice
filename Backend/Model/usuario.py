from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str | None = None
    user_name: str
    correo:str
    contrasena: str
    es_administrador: bool
    