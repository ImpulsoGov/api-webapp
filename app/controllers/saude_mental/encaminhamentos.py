from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.encaminhamentos import (
    EncaminhamentoApsCaps,
    EncaminhamentoApsCapsResumoUltimoMesHorizontal,
    EncaminhamentoApsCapsResumoUltimoMesVertical,
    EncaminhamentoApsEspecializada,
    EncaminhamentoApsEspecializadaResumoUltimoMesHorizontal,
    EncaminhamentoApsEspecializadaResumoUltimoMesVertical,
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


def obter_dados_aps_especializada_resumo_horizontal_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_especializada_resumo = (
        session.query(EncaminhamentoApsEspecializadaResumoUltimoMesHorizontal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_especializada_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo horizontal da APS especializada no último mês ",
                "do município não encontrado",
            ),
        )

    return dados_aps_especializada_resumo


def obter_dados_aps_especializada_resumo_vertical_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_especializada_resumo = (
        session.query(EncaminhamentoApsEspecializadaResumoUltimoMesVertical)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_especializada_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo vertical da APS especializada no último mês ",
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


def obter_dados_aps_caps_resumo_horizontal_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_caps_resumo = (
        session.query(EncaminhamentoApsCapsResumoUltimoMesHorizontal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_caps_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo horizontal da APS CAPS no último mês ",
                "do município não encontrado",
            ),
        )

    return dados_aps_caps_resumo


def obter_dados_aps_caps_resumo_vertical_por_id_sus(
    municipio_id_sus: str,
):
    dados_aps_caps_resumo = (
        session.query(EncaminhamentoApsCapsResumoUltimoMesVertical)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_aps_caps_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Resumo vertical da APS CAPS no último mês ",
                "do município não encontrado",
            ),
        )

    return dados_aps_caps_resumo


def selecionar_resumo_aps_especializada_por_sentido(municipio_id_sus: str, sentido: str):
    if sentido == "vertical":
        return obter_dados_aps_especializada_resumo_vertical_por_id_sus(
            municipio_id_sus=municipio_id_sus
        )

    if sentido == "horizontal" or sentido is None:
        dados = obter_dados_aps_especializada_resumo_horizontal_por_id_sus(
            municipio_id_sus=municipio_id_sus
        )
        return dados

    raise HTTPException(
        status_code=400, detail="O resumo deve ser horizontal ou vertical"
    )


def selecionar_resumo_aps_caps_por_sentido(municipio_id_sus: str, sentido: str):
    if sentido == "vertical":
        return obter_dados_aps_caps_resumo_vertical_por_id_sus(
            municipio_id_sus=municipio_id_sus
        )

    if sentido == "horizontal" or sentido is None:
        return obter_dados_aps_caps_resumo_horizontal_por_id_sus(
            municipio_id_sus=municipio_id_sus
        )

    raise HTTPException(
        status_code=400, detail="O resumo deve ser horizontal ou vertical"
    )
