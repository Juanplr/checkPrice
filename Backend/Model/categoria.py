from sqlmodel import SQLModel, Field


class CategoriaBase(SQLModel):
    nombre: str
    
class Categoria(CategoriaBase, table=True):
    id: int = Field(default=None, primary_key=True)

class CategoriaPublic(CategoriaBase):
    id: int

class CategoriaCreate(CategoriaBase):
    nombre: str

class CategoriaUpdate(CategoriaBase):
    nombre: str | None = None