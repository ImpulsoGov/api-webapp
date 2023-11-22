from fastapi import APIRouter
from typing import Union
from app.controllers.saude_mental.abandono import (
    dados_caps_adesao_evasao_coortes_resumo,
    dados_caps_adesao_evasao_mensal,
    dados_caps_adesao_usuarios_perfil,
    obter_perfil_evadiram_no_mes_por_cid,
    obter_perfil_evadiram_no_mes_por_genero_e_idade,
    consultar_dados_caps_adesao_evasao_coortes_resumo
)

router = APIRouter()


@router.get("/saude-mental/abandono/coortes")
async def obter_dados_caps_adesao_evasao_coortes_resumo(
    municipio_id_sus: str,
    estabelecimento: Union[str, None] = None,
    periodo: Union[str, None] = None
):
    return consultar_dados_caps_adesao_evasao_coortes_resumo(
        municipio_id_sus=municipio_id_sus,
        periodo = periodo,
        estabelecimento = estabelecimento
        )


@router.get("/saude-mental/abandono/mensal")
async def obter_dados_caps_adesao_evasao_mensal(
    municipio_id_sus: str,
):
    return dados_caps_adesao_evasao_mensal(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/abandono/resumo")
async def obter_dados_caps_adesao_usuarios_perfil(
    municipio_id_sus: str,
):
    return dados_caps_adesao_usuarios_perfil(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/abandono/evadiram-no-mes/cid")
async def obter_cid_evadiram_no_mes(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_evadiram_no_mes_por_cid(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/abandono/evadiram-no-mes/genero-e-idade")
async def obter_genero_e_idade_evadiram_no_mes(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_evadiram_no_mes_por_genero_e_idade(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )
