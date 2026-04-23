from fastapi import FastAPI
app = FastAPI()

@app.get("/idtipo/{idtipo:path}")
async def get_precio(idtipo: str):
    return {"precio": idtipo}