from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.consultorionarua import (
    ConsultorionaruaAtendimentos,
    ConsultorionaruaAtendimentos12meses,
)

session = db.session


def dados_consultorionarua_atendimentos(municipio_id_sus: str):
    dados_consultorionarua_atendimentos = (
        session.query(ConsultorionaruaAtendimentos)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_consultorionarua_atendimentos) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de Consultorio na Rua não encontrados",
        )

    return dados_consultorionarua_atendimentos


def dados_consultorionarua_atendimentos_12meses(
    municipio_id_sus: str,
):
    dados_consultorionarua_atendimentos_12meses = (
        session.query(ConsultorionaruaAtendimentos12meses)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_consultorionarua_atendimentos_12meses) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados de Consultorio na Rua dos 12 meses não encontrados",),
        )

    return dados_consultorionarua_atendimentos_12meses
