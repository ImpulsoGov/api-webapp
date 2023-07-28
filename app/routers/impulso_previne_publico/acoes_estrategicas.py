from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.impulso_previne_publico.acoes_estrategicas import (
    acoes_estrategicas_repasses,
    acoes_estrategicas_vigente_agrupada
)
router = APIRouter()

@router.get("/impulsoprevine/acoes-estrategicas/repasses")
async def obter_acoes_estrategicas_repasses(
    municipio_uf: str,
):
    return acoes_estrategicas_repasses(
        municipio_uf=municipio_uf,
    )

@router.get("/impulsoprevine/acoes-estrategicas/agrupada")
async def obter_acoes_estrategicas_agrupadas(
    municipio_uf: str,
):
    return acoes_estrategicas_vigente_agrupada(
        municipio_uf=municipio_uf
    )