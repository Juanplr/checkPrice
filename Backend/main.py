from fastapi import FastAPI
from ws import usuario_ws, producto_ws, categoria_ws, token_ws
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_ws.router)
app.include_router(producto_ws.router)
app.include_router(categoria_ws.router)
app.include_router(token_ws.router)


    