from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.matriciamentos import (
    MatriciamentosPorCapsUltimoAno,
    MatriciamentosPorMunicipioUltimoAno,
)

session = db.session


def obter_matriciamentos_caps_ultimo_ano_por_id_sus(municipio_id_sus: str):
    matriciamentos_caps = (
        session.query(MatriciamentosPorCapsUltimoAno)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .first()
    )

    if not matriciamentos_caps:
        raise HTTPException(
            status_code=404,
            detail=(
                "Matriciamentos CAPS no último ano "
                "do município não encontrados"
            ),
        )

    return matriciamentos_caps


def obter_matriciamentos_municipio_ultimo_ano_por_id_sus(municipio_id_sus: str):
    matriciamentos_municipio = (
        session.query(MatriciamentosPorMunicipioUltimoAno)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .first()
    )

    if not matriciamentos_municipio:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return matriciamentos_municipio
