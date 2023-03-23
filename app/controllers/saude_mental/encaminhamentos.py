from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.encaminhamentos.aps_especializada import (
    EncaminhamentoApsEspecializada,
)
from app.models.saude_mental.encaminhamentos.aps_especializada_resumo_ultimo_mes_horizontal import (
    EncaminhamentosApsEspecializadaResumoUltimoMesHorizontal,
)

session = db.session


def obter_dados_aps_especializada_por_id_sus(municipio_id_sus: str):
    dados_aps_especializada = (
        session.query(EncaminhamentoApsEspecializada)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_especializada) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de APS especializada do município não encontrados",
        )

    return dados_aps_especializada


def obter_dados_aps_especializada_resumo_ultimo_mes_horizontal_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_especializada = (
        session.query(EncaminhamentosApsEspecializadaResumoUltimoMesHorizontal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .first()
    )

    if not dados_aps_especializada:
        raise HTTPException(
            status_code=404,
            detail=("Resumo da APS especializada do município não encontrado"),
        )

    return dados_aps_especializada
