from fastapi import FastAPI
from routers import suporte,impulso_previne
from pydantic import BaseModel
app = FastAPI()

app.include_router(suporte.router)
app.include_router(impulso_previne.router)

class Welcome(BaseModel):
    mensagem : str

@app.get("/", response_model=Welcome)
async def main():
    return {"mensagem":"Bem Vindo"}
