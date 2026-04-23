from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    codigo_de_barras: str
    precio: float
    id_usuario: int
    id_categoria: int