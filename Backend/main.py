from fastapi import FastAPI, Query
from typing import Annotated
from Model.usuario import UsuarioPublic, Usuario
from data_base import session_dep
from sqlmodel import select

app = FastAPI()

@app.get("/")
async def get_precio():
    return {"saludo": "Hola mundo!"}

@app.get("/usuarios", response_model=list[UsuarioPublic])
def read_usuarios(
    session: session_dep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    usuarios = session.exec(select(Usuario).offset(offset).limit(limit)).all()
    return usuarios


    