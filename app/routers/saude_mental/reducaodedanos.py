from typing import Union
from fastapi import APIRouter

from app.controllers.saude_mental.reducaodedanos import (
    dados_reducaodedanos_12meses,
    consultar_reducao_de_danos,
    consultar_nomes_de_ocupacoes_reducao_de_danos,
)


router = APIRouter()


@router.get("/saude-mental/reducao-de-danos")
async def obter_dados_reducao_de_danos(
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    ocupacoes: Union[str, None] = None,
):
    return consultar_reducao_de_danos(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        ocupacoes=ocupacoes,
    )


@router.get("/saude-mental/reducao-de-danos/ocupacoes")
async def obter_nomes_de_ocupacoes_reducao_de_danos(municipio_id_sus: str):
    return consultar_nomes_de_ocupacoes_reducao_de_danos(
        municipio_id_sus=municipio_id_sus,
    )


@router.get("/saude-mental/reducaodedanos12meses")
async def obter_dados_reducaodedanos_12meses(
    municipio_id_sus: str,
):
    return dados_reducaodedanos_12meses(municipio_id_sus=municipio_id_sus)
