from typing import Union
from fastapi import APIRouter

from app.controllers.saude_mental.procedimentos import (
    consultar_dados_procedimentos_por_usuario_estabelecimento,
    dados_procedimentos_por_usuario_resumo,
    consultar_procedimentos_por_usuario_tempo_servico,
    consultar_procedimentos_por_hora,
    consultar_procedimentos_por_tipo,
    consultar_nomes_de_procedimentos_por_tipo,
)

router = APIRouter()


@router.get("/saude-mental/procedimentos_por_usuario_estabelecimentos")
async def obter_dados_procedimentos_por_usuario_estabelecimento(
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    estabelecimento_linha_idade: Union[str, None] = None,
    estabelecimento_linha_perfil: Union[str, None] = None,
):
    return consultar_dados_procedimentos_por_usuario_estabelecimento(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        estabelecimento_linha_idade=estabelecimento_linha_idade,
        estabelecimento_linha_perfil=estabelecimento_linha_perfil,
    )


@router.get("/saude-mental/procedimentos_por_usuario_resumo")
async def obter_dados_procedimentos_por_usuario_resumo(
    municipio_id_sus: str,
):
    return dados_procedimentos_por_usuario_resumo(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/procedimentos-por-hora")
async def obter_procedimentos_por_hora(
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    ocupacao: Union[str, None] = None,
):
    return consultar_procedimentos_por_hora(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
        ocupacao=ocupacao,
    )


@router.get("/saude-mental/procedimentos-por-tipo")
async def obter_procedimentos_por_tipo(
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
    procedimentos: Union[str, None] = None,
):
    return consultar_procedimentos_por_tipo(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        procedimentos=procedimentos,
        periodos=periodos,
    )


@router.get("/saude-mental/procedimentos-por-usuario-tempo")
async def obter_procedimentos_por_usuario_tempo_servico(
    municipio_id_sus: str,
    estabelecimentos: Union[str, None] = None,
    periodos: Union[str, None] = None,
):
    return consultar_procedimentos_por_usuario_tempo_servico(
        municipio_id_sus=municipio_id_sus,
        estabelecimentos=estabelecimentos,
        periodos=periodos,
    )


@router.get("/saude-mental/procedimentos-por-tipo/procedimentos")
async def obter_nomes_de_procedimentos_por_tipo(municipio_id_sus: str):
    return consultar_nomes_de_procedimentos_por_tipo(
        municipio_id_sus=municipio_id_sus,
    )
