from fastapi import APIRouter

from app.controllers.saude_mental.abandono import (
    dados_caps_adesao_evasao_coortes_resumo,
    dados_caps_adesao_evasao_mensal,
    dados_caps_adesao_usuarios_perfil
)

router = APIRouter()


@router.get("/saude-mental/abandono/coortes")
async def obter_dados_caps_adesao_evasao_coortes_resumo(
    municipio_id_sus: str,
):
    return dados_caps_adesao_evasao_coortes_resumo(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/abandono/mensal")
async def obter_dados_caps_adesao_evasao_mensal(
    municipio_id_sus: str,
):
    return dados_caps_adesao_evasao_mensal(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/abandono/resumo")
async def obter_dados_caps_adesao_evasao_coortes_resumo(
    municipio_id_sus: str,
):
    return dados_caps_adesao_usuarios_perfil(
        municipio_id_sus=municipio_id_sus
    )
