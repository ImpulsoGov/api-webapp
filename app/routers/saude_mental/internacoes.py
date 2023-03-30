from fastapi import APIRouter

from app.controllers.saude_mental.internacoes import (
    obter_internacoes_raps_resumo_admissoes_12m_vertical_por_id_sus,
    obter_internacoes_raps_resumo_altas_12m_vertical_por_id_sus,
)

router = APIRouter()


@router.get("/saude-mental/internacoes/raps/admissoes/resumo/vertical")
async def obter_internacoes_raps_resumo_admissoes(
    municipio_id_sus: str,
):
    return obter_internacoes_raps_resumo_admissoes_12m_vertical_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/internacoes/raps/altas/resumo/vertical")
async def obter_internacoes_raps_resumo_altas(
    municipio_id_sus: str,
):
    return obter_internacoes_raps_resumo_altas_12m_vertical_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )
