from fastapi import APIRouter
from fastapi.responses import Response
from typing import Union

from app.controllers.saude_mental.usuarios import (
    obter_perfil_usuarios_ativos_por_cid,
    obter_perfil_usuarios_ativos_por_condicao,
    obter_perfil_usuarios_ativos_por_genero_e_idade,
    obter_perfil_usuarios_ativos_por_raca,
    obter_perfil_usuarios_novos_por_cid,
    obter_perfil_usuarios_novos_por_condicao,
    obter_perfil_usuarios_novos_por_genero_e_idade,
    obter_perfil_usuarios_novos_por_raca,
    obter_usuarios_novos_resumo,
    obter_usuarios_perfil_estabelecimento,
    consultar_usuarios_ativos_por_estabelecimento,
    consultar_usuarios_novos_resumo
)

QUANTIDADE_SEGUNDOS_24_HORAS = 60 * 60 * 24

router = APIRouter()


@router.get("/saude-mental/usuarios/perfilestabelecimento")
async def obter_perfil_usuarios_estabelecimento(
    municipio_id_sus: str,
):
    return obter_usuarios_perfil_estabelecimento(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/perfil/por-estabelecimento")
async def obter_usuarios_ativos_por_estabelecimento(
    response: Response,
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    estabelecimento_linha_perfil: Union[str, None] = None,
    estabelecimento_linha_idade: Union[str, None] = None,
):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"

    return consultar_usuarios_ativos_por_estabelecimento(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        estabelecimento_linha_perfil=estabelecimento_linha_perfil,
        estabelecimento_linha_idade=estabelecimento_linha_idade
    )


@router.get("/saude-mental/usuarios/novosresumo")
async def obter_novos_usuarios_resumo(
    municipio_id_sus: str,
):
    return obter_usuarios_novos_resumo(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/novos/resumo")
async def obter_resumo_usuarios_novos(
    response: Response,
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    estabelecimento_linha_perfil: Union[str, None] = None,
    estabelecimento_linha_idade: Union[str, None] = None,
):
    response.headers["Cache-Control"] = f"private, max-age={QUANTIDADE_SEGUNDOS_24_HORAS}"

    return consultar_usuarios_novos_resumo(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        estabelecimento_linha_perfil=estabelecimento_linha_perfil,
        estabelecimento_linha_idade=estabelecimento_linha_idade,
    )


@router.get("/saude-mental/usuarios/perfil/condicao")
async def obter_condicao_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_condicao(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/genero-e-idade")
async def obter_genero_e_idade_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_genero_e_idade(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/raca")
async def obter_raca_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_raca(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/cid")
async def obter_cid_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_cid(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/novos/condicao")
async def obter_condicao_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_usuarios_novos_por_condicao(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/usuarios/novos/genero-e-idade")
async def obter_genero_e_idade_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_usuarios_novos_por_genero_e_idade(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/usuarios/novos/raca")
async def obter_raca_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_usuarios_novos_por_raca(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/usuarios/novos/cid")
async def obter_cid_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_usuarios_novos_por_cid(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )
