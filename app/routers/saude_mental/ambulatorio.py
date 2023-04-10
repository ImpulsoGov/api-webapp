from fastapi import APIRouter

from app.controllers.saude_mental.ambulatorio import (
    obter_ambulatorio_atendimento_resumo,
    obter_ambulatorio_atendimento_resumo_ultimo_mes,
    obter_ambulatorio_procedimento_por_profissional,
    obter_ambulatorio_usuario_perfil
)

router = APIRouter()


@router.get("/saude-mental/ambulatorio/atendimento-resumo")
async def obter_dados_ambulatorio_atendimento_resumo(
    municipio_id_sus: str,
):
    return obter_ambulatorio_atendimento_resumo(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/ambulatorio/atendimento-resumo-ultimomes")
async def obter_dados_ambulatorio_atendimento_resumo_ultimo_mes(
    municipio_id_sus: str,
):
    return obter_ambulatorio_atendimento_resumo_ultimo_mes(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/ambulatorio/procedimento-por-profissional")
async def obter_dados_ambulatorio_procedimento_por_profissional(
    municipio_id_sus: str,
):
    return obter_ambulatorio_procedimento_por_profissional(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/ambulatorio/usuario-perfil")
async def obter_dados_ambulatorio_usuario_perfil(
    municipio_id_sus: str,
):
    return obter_ambulatorio_usuario_perfil(
        municipio_id_sus=municipio_id_sus
    )
