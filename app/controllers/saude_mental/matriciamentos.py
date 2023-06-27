from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.matriciamentos import (
    MatriciamentoPorCapsUltimoAno,
    MatriciamentoPorMunicipioUltimoAno,
)

session = db.session


def obter_matriciamentos_caps_ultimo_ano_por_id_sus(municipio_id_sus: str):
    matriciamentos_caps = (
        session.query(MatriciamentoPorCapsUltimoAno)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(matriciamentos_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Matriciamentos CAPS no último ano " "do município não encontrados"
            ),
        )

    return matriciamentos_caps


def obter_matriciamentos_municipio_ultimo_ano_por_id_sus(municipio_id_sus: str):
    matriciamentos_municipio = (
        session.query(MatriciamentoPorMunicipioUltimoAno)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(matriciamentos_municipio) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return matriciamentos_municipio
