from sqlmodel import SQLModel, Field

class ProductoBase(SQLModel):
    nombre: str
    codigo_de_barras: str
    precio: float
    id_usuario: int
    id_categoria: int
    
class Producto(ProductoBase, table=True):
    id: int = Field(default=None, primary_key=True)

class ProductoPublic(ProductoBase):
    id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    nombre: str | None = None
    codigo_de_barras: str | None = None
    precio: float | None = None
    id_usuario: int | None = None
    id_categoria: int | None = None