from sqlmodel import SQLModel, Field
from decimal import Decimal

class ProductoBase(SQLModel):
    nombre: str = Field(index=True)
    codigo_de_barras: str
    precio: Decimal
    
class Producto(ProductoBase, table=True):
    id: int = Field(default=None, primary_key=True)
    id_usuario: int  = Field(foreign_key="usuario.id")
    id_categoria: int = Field(foreign_key="categoria.id")

class ProductoPublic(ProductoBase):
    id: int
    nombre_usuario: str | None = None
    nombre_categoria: str | None = None
    
class ProductoCreate(ProductoBase):
    nombre: str = Field(index=True)
    codigo_de_barras: str
    precio: Decimal
    id_usuario: int  
    id_categoria: int

class ProductoUpdate(ProductoBase):
    nombre: str | None = None
    codigo_de_barras: str | None = None
    precio: Decimal | None = None
    id_usuario: int | None = None
    id_categoria: int | None = None