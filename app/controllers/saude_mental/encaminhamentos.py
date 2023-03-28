from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.encaminhamentos import (
    EncaminhamentoApsCaps,
    EncaminhamentoApsEspecializada,
    EncaminhamentosApsCapsResumoUltimoMesHorizontal,
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
    dados_aps_especializada_resumo = (
        session.query(EncaminhamentosApsEspecializadaResumoUltimoMesHorizontal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .first()
    )

    if not dados_aps_especializada_resumo:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo horizontal da APS especializada no último mês ",
                "do município não encontrado",
            ),
        )

    return dados_aps_especializada_resumo


def obter_dados_aps_caps_por_id_sus(municipio_id_sus: str):
    dados_aps_caps = (
        session.query(EncaminhamentoApsCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de APS CAPS do município não encontrados",
        )

    return dados_aps_caps


def obter_dados_aps_caps_resumo_ultimo_mes_horizontal_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_caps_resumo = (
        session.query(EncaminhamentosApsCapsResumoUltimoMesHorizontal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .first()
    )

    if not dados_aps_caps_resumo:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo horizontal da APS CAPS no último mês ",
                "do município não encontrado",
            ),
        )

    return dados_aps_caps_resumo
