from fastapi import APIRouter
from fastapi.responses import Response

from app.controllers.saude_mental.procedimentos import (
    dados_procedimentos_por_hora,
    dados_procedimentos_por_tipo,
    dados_procedimentos_por_usuario_estabelecimento,
    dados_procedimentos_por_usuario_resumo,
    dados_procedimentos_por_usuario_tempo_servico,
    consultar_procedimentos_por_usuario_tempo_servico
)
from typing import Union

router = APIRouter()


@router.get("/saude-mental/procedimentos_por_hora")
async def obter_dados_procedimentos_por_hora(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_hora(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/procedimentos_por_tipo")
async def obter_dados_procedimentos_por_tipo(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_tipo(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/procedimentos_por_usuario_estabelecimentos")
async def obter_dados_procedimentos_por_usuario_estabelecimento(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_usuario_estabelecimento(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/procedimentos_por_usuario_resumo")
async def obter_dados_procedimentos_por_usuario_resumo(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_usuario_resumo(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/procedimentos_por_usuario_tempo")
async def obter_dados_procedimentos_por_usuario_tempo_servico(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_usuario_tempo_servico(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/procedimentos-por-usuario-tempo")
async def obter_procedimentos_por_usuario_tempo_servico(
    response: Response,
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
):
    response.headers["Cache-Control"] = "private, max-age=90"

    return consultar_procedimentos_por_usuario_tempo_servico(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos
    )
