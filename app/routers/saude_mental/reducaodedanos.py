from fastapi import APIRouter

from app.controllers.saude_mental.reducaodedanos import (
    dados_reducaodedanos,
    dados_reducaodedanos_12meses,
)

router = APIRouter()


@router.get("/saude-mental/reducaodedanos")
async def obter_dados_reducaodedanos(
    municipio_id_sus: str,
):
    return dados_reducaodedanos(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/reducaodedanos12meses")
async def obter_dados_reducaodedanos_12meses(
    municipio_id_sus: str,
):
    return dados_reducaodedanos_12meses(municipio_id_sus=municipio_id_sus)
