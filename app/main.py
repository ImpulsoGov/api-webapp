from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.routers import impulso_previne, saude_mental, territorios, usuarios

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


app.include_router(usuarios.router)
app.include_router(impulso_previne.router)
app.include_router(territorios.router)
app.include_router(saude_mental.router)


class Welcome(BaseModel):
    mensagem: str


@app.get("/", response_model=Welcome)
async def main():
    return {"mensagem": "Bem Vindo"}
