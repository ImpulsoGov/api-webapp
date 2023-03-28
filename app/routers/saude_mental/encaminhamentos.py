from typing import Optional

from fastapi import APIRouter

from app.controllers.saude_mental.encaminhamentos import (
    obter_dados_aps_caps_por_id_sus,
    obter_dados_aps_caps_resumo_ultimo_mes_horizontal_por_id_sus,
    obter_dados_aps_especializada_por_id_sus,
    obter_dados_aps_especializada_resumo_ultimo_mes_horizontal_por_id_sus,
)

router = APIRouter()


@router.get("/saude-mental/encaminhamentos/aps/especializada")
async def obter_dados_aps_especializada(
    municipio_id_sus: Optional[str] = None,
):
    return obter_dados_aps_especializada_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/encaminhamentos/aps/especializada/resumo")
async def obter_dados_aps_especializada_resumo(
    municipio_id_sus: Optional[str] = None,
):
    return (
        obter_dados_aps_especializada_resumo_ultimo_mes_horizontal_por_id_sus(
            municipio_id_sus=municipio_id_sus
        )
    )


@router.get("/saude-mental/encaminhamentos/aps/caps")
async def obter_dados_aps_caps(
    municipio_id_sus: Optional[str] = None,
):
    return obter_dados_aps_caps_por_id_sus(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/encaminhamentos/aps/caps/resumo")
async def obter_dados_aps_caps_resumo(
    municipio_id_sus: Optional[str] = None,
):
    return obter_dados_aps_caps_resumo_ultimo_mes_horizontal_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )
