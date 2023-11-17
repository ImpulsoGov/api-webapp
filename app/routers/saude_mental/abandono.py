from fastapi import APIRouter,  Request, Depends, Response
QUANTIDADE_SEGUNDOS_24_HORAS = 60 * 60 * 24
from app.controllers.saude_mental.abandono import (
    dados_caps_adesao_evasao_coortes_resumo,
    dados_caps_adesao_evasao_mensal,
    dados_caps_adesao_usuarios_perfil,
    obter_perfil_evadiram_no_mes_por_cid,
    obter_perfil_evadiram_no_mes_por_genero_e_idade,
)
async def custom_middleware(request: Request, response: Response):
    response.headers["X-Custom-Header"] = "Added by middleware"
    return response
async def adiciona_cache_header(request: Request, response: Response):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"
    return response

router = APIRouter(dependencies=[
    Depends(adiciona_cache_header),
    Depends(custom_middleware)
])


@router.get("/saude-mental/abandono/coortes")
async def obter_dados_caps_adesao_evasao_coortes_resumo(
    municipio_id_sus: str,
):
    return dados_caps_adesao_evasao_coortes_resumo(municipio_id_sus=municipio_id_sus)


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
