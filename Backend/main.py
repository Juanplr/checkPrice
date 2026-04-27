from fastapi import FastAPI
from ws import usuario_ws, producto_ws, categoria_ws

app = FastAPI()

app.include_router(usuario_ws.router)
app.include_router(producto_ws.router)
app.include_router(categoria_ws.router)


    