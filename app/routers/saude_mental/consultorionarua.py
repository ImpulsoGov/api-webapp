from fastapi import APIRouter

from app.controllers.saude_mental.consultorionarua import (
    dados_consultorionarua_atendimentos,
    dados_consultorionarua_atendimentos_12meses,
)

router = APIRouter()


@router.get("/saude-mental/consultorionarua")
async def obter_dados_consultorionarua_atendimentos_12meses(
    municipio_id_sus: str,
):
    return dados_consultorionarua_atendimentos(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/consultorionarua12meses")
async def obter_dados_consultorionarua_atendimentos_12meses(
    municipio_id_sus: str,
):
    return dados_consultorionarua_atendimentos_12meses(municipio_id_sus=municipio_id_sus)
