from fastapi import FastAPI

from ws import usuario_ws

app = FastAPI()

app.include_router(usuario_ws.router)



    