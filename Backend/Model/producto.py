from sqlmodel import SQLModel, Field

class ProductoBase(SQLModel):
    nombre: str = Field(index=True)
    codigo_de_barras: str
    precio: float
    
class Producto(ProductoBase, table=True):
    id: int = Field(default=None, primary_key=True)
    id_usuario: int  = Field(foreign_key="usuario.id")
    id_categoria: int = Field(foreign_key="categoria.id")

class ProductoPublic(ProductoBase):
    id: int
    nombre_usuario: str
    nombre_categoria: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    nombre: str | None = None
    codigo_de_barras: str | None = None
    precio: float | None = None
    id_usuario: int | None = None
    id_categoria: int | None = None