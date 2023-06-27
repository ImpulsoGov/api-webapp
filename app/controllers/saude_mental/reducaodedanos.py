from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.reducaodedanos import ReducaoDanos, ReducaoDanos12meses

session = db.session


def dados_reducaodedanos(municipio_id_sus: str):
    dados_reducaodedanos = (
        session.query(ReducaoDanos)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_reducaodedanos) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de Redução de danos não encontrados",
        )

    return dados_reducaodedanos


def dados_reducaodedanos_12meses(
    municipio_id_sus: str,
):
    dados_reducaodedanos_12meses = (
        session.query(ReducaoDanos12meses)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_reducaodedanos_12meses) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados de Redução de danos dos 12 meses não encontrados",),
        )

    return dados_reducaodedanos_12meses
