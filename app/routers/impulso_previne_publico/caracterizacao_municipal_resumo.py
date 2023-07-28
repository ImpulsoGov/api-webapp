from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.impulso_previne_publico.caracterizacao_municipal_resumo import (
    caracterizacao_municipal_resumo
)

router = APIRouter()

@router.get("/impulsoprevine/caracterizacao_municipal/resumo")
async def obter_caracterizacao_municipal_resumo(
    municipio_uf: str,
):
    return caracterizacao_municipal_resumo(
        municipio_uf=municipio_uf
    )