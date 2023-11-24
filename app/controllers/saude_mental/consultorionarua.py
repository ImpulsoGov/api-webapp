from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.consultorionarua import (
    ConsultorionaruaAtendimentos,
    ConsultorionaruaAtendimentos12meses,
)

session = db.session


def dados_consultorionarua_atendimentos(municipio_id_sus: str):
    try:
        dados_consultorionarua_atendimentos = (
            session.query(ConsultorionaruaAtendimentos)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return dados_consultorionarua_atendimentos
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def dados_consultorionarua_atendimentos_12meses(
    municipio_id_sus: str,
):
    try:
        dados_consultorionarua_atendimentos_12meses = (
            session.query(ConsultorionaruaAtendimentos12meses)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return dados_consultorionarua_atendimentos_12meses
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
