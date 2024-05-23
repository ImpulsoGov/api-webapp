from fastapi import APIRouter

from app.controllers.saude_mental.estabelecimentos_e_periodos import (
    Entidade,
    obter_estabelecimentos_de_entidade_por_id_sus,
    obter_periodos_de_entidade_por_id_sus,
    obter_ultima_competencia_disponivel_por_entidade
)

router = APIRouter()


@router.get("/saude-mental/estabelecimentos")
async def obter_estabelecimentos(municipio_id_sus: str, entidade: Entidade):
    return obter_estabelecimentos_de_entidade_por_id_sus(
        municipio_id_sus=municipio_id_sus, entidade=entidade
    )


@router.get("/saude-mental/periodos")
async def obter_periodos(municipio_id_sus: str, entidade: Entidade):
    return obter_periodos_de_entidade_por_id_sus(
        municipio_id_sus=municipio_id_sus, entidade=entidade
    )

@router.get("/saude-mental/ultima-competencia")
async def obter_ultima_competencia(municipio_id_sus: str, entidade: Entidade, estabelecimento_linha_idade: str):
    return obter_ultima_competencia_disponivel_por_entidade(
        municipio_id_sus=municipio_id_sus,
        entidade=entidade,
        estabelecimento_linha_idade=estabelecimento_linha_idade
    )