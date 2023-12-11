from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
from app.routers import impulso_previne_publico, impulso_previne_nominal, saude_mental, territorios, usuarios
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000/cadastro-usuarios",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(usuarios.router)
app.include_router(impulso_previne_nominal.router)
app.include_router(impulso_previne_publico.router)
app.include_router(territorios.router)
app.include_router(saude_mental.router)
class Welcome(BaseModel):
    mensagem: str
@app.get("/", response_model=Welcome)
async def main():
    return {"mensagem": "Bem Vindo"}
