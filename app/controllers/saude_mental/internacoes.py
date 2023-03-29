from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.internacoes import (
    InternacaoRelacaoRapsResumoAdmissoes12mVertical,
    InternacaoRelacaoRapsResumoAltas12mVertical,
)

session = db.session


def obter_internacoes_raps_resumo_admissoes_12m_vertical_por_id_sus(
    municipio_id_sus: str,
):
    internacoes_raps_resumo = (
        session.query(InternacaoRelacaoRapsResumoAdmissoes12mVertical)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(internacoes_raps_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo vertical de internações por admissões ",
                "do município não encontrado",
            ),
        )

    return internacoes_raps_resumo


def obter_internacoes_raps_resumo_altas_12m_vertical_por_id_sus(
    municipio_id_sus: str,
):
    internacoes_raps_resumo = (
        session.query(InternacaoRelacaoRapsResumoAltas12mVertical)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(internacoes_raps_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo vertical de internações por altas ",
                "do município não encontrado",
            ),
        )

    return internacoes_raps_resumo
