from typing import Optional

from fastapi import APIRouter

from app.controllers.saude_mental.encaminhamentos import (
    obter_dados_aps_caps_por_id_sus,
    obter_dados_aps_especializada_por_id_sus,
    selecionar_resumo_aps_caps_por_sentido,
    selecionar_resumo_aps_especializada_por_sentido,
)

router = APIRouter()


@router.get("/saude-mental/encaminhamentos/aps/especializada")
async def obter_dados_aps_especializada(
    municipio_id_sus: str,
):
    return obter_dados_aps_especializada_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/encaminhamentos/aps/especializada/resumo")
async def obter_dados_aps_especializada_resumo(
    municipio_id_sus: str,
    sentido: Optional[str] = None,
):
    return selecionar_resumo_aps_especializada_por_sentido(
        municipio_id_sus=municipio_id_sus, sentido=sentido
    )


@router.get("/saude-mental/encaminhamentos/aps/caps")
async def obter_dados_aps_caps(
    municipio_id_sus: str,
):
    return obter_dados_aps_caps_por_id_sus(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/encaminhamentos/aps/caps/resumo")
async def obter_dados_aps_caps_resumo(
    municipio_id_sus: str,
    sentido: Optional[str] = None,
):
    return selecionar_resumo_aps_caps_por_sentido(
        municipio_id_sus=municipio_id_sus, sentido=sentido
    )
