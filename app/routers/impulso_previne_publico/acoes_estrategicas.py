from fastapi import APIRouter, Depends
from app.controllers.impulso_previne_publico.acoes_estrategicas import (
    acoes_estrategicas_repasses,
    acoes_estrategicas_vigente_agrupada
)
from app.controllers.usuarios.auth import Usuario, get_current_user

router = APIRouter()

@router.get("/impulsoprevine/acoes-estrategicas/repasses")
async def obter_acoes_estrategicas_repasses(
    municipio_uf: str,
    username: Usuario = Depends(get_current_user)
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