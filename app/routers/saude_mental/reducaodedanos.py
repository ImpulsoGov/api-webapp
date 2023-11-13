from fastapi import APIRouter
from fastapi.responses import Response

from app.controllers.saude_mental.reducaodedanos import (
    dados_reducaodedanos,
    dados_reducaodedanos_12meses,
    consultar_reducao_de_danos,
    consultar_nomes_de_ocupacoes_reducao_de_danos
)
from typing import Union

QUANTIDADE_SEGUNDOS_24_HORAS = 60 * 60 * 24

router = APIRouter()


@router.get("/saude-mental/reducaodedanos")
async def obter_dados_reducaodedanos(
    municipio_id_sus: str,
):
    return dados_reducaodedanos(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/reducao-de-danos")
async def obter_dados_reducao_de_danos(
    response: Response,
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    ocupacoes: Union[str, None] = None
):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"

    return consultar_reducao_de_danos(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        ocupacoes=ocupacoes
    )


@router.get("/saude-mental/reducao-de-danos/ocupacoes")
async def obter_nomes_de_ocupacoes_reducao_de_danos(
    response: Response,
    municipio_id_sus: str,
):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"

    return consultar_nomes_de_ocupacoes_reducao_de_danos(
        municipio_id_sus=municipio_id_sus,
    )


@router.get("/saude-mental/reducaodedanos12meses")
async def obter_dados_reducaodedanos_12meses(
    municipio_id_sus: str,
):
    return dados_reducaodedanos_12meses(municipio_id_sus=municipio_id_sus)
