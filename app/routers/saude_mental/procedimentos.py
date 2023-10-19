from fastapi import APIRouter

from app.controllers.saude_mental.procedimentos import (
    dados_procedimentos_por_hora,
    dados_procedimentos_por_tipo,
    dados_procedimentos_por_usuario_estabelecimento,
    dados_procedimentos_por_usuario_resumo,
    dados_procedimentos_por_usuario_tempo_servico,
)
from typing import Optional

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
    estabelecimentos: Optional[str],
    periodos: Optional[str]
):
    return dados_procedimentos_por_usuario_tempo_servico(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos
    )
