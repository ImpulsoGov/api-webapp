from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.routers import impulso_previne, suporte, territorios
from app.routers.saude_mental import (
    atendimentos_individuais,
    encaminhamentos,
    internacoes,
    matriciamentos,
    consultorionarua,
    reducaodedanos,
    usuarios,
    abandono,
    procedimentos,
    ambulatorio,
    atencao_hospitalar
)

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


app.include_router(suporte.router)
app.include_router(impulso_previne.router)
app.include_router(territorios.router)
app.include_router(encaminhamentos.router)
app.include_router(matriciamentos.router)
app.include_router(internacoes.router)
app.include_router(atendimentos_individuais.router)
app.include_router(consultorionarua.router)
app.include_router(reducaodedanos.router)
app.include_router(usuarios.router)
app.include_router(abandono.router)
app.include_router(procedimentos.router)
app.include_router(atencao_hospitalar.router)
app.include_router(ambulatorio.router)


class Welcome(BaseModel):
    mensagem: str


@app.get("/", response_model=Welcome)
async def main():
    return {"mensagem": "Bem Vindo"}
