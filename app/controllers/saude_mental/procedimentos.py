from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.procedimentos import (
    ProcedimentoPorUsuarioEstabelecimento,
    ProcedimentoPorUsuarioResumo,
    ProcedimentoPorUsuarioTempoServiço,
    ProcedimentosPorHora,
    ProcedimentosPorTipo
)

session = db.session

def dados_procedimentos_por_usuario_estabelecimento(municipio_id_sus: str):
    ProcedimentoPorUsuarioEstabelecimento_dados = (
        session.query(ProcedimentoPorUsuarioEstabelecimento)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentoPorUsuarioEstabelecimento_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Matriciamentos CAPS no último ano "
                "do município não encontrados"
            ),
        )

    return ProcedimentoPorUsuarioEstabelecimento_dados


def dados_procedimentos_por_usuario_resumo(municipio_id_sus: str):
    ProcedimentoPorUsuarioResumo_dados = (
        session.query(ProcedimentoPorUsuarioResumo)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentoPorUsuarioResumo_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return ProcedimentoPorUsuarioResumo_dados


def dados_procedimentos_por_usuario_tempo_servico(municipio_id_sus: str):
    ProcedimentoPorUsuarioTempoServiço_dados = (
        session.query(ProcedimentoPorUsuarioTempoServiço)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentoPorUsuarioTempoServiço_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return ProcedimentoPorUsuarioTempoServiço_dados


def dados_procedimentos_por_hora(municipio_id_sus: str):
    ProcedimentosPorHora_dados = (
        session.query(ProcedimentosPorHora)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentosPorHora_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return ProcedimentosPorHora_dados


def dados_procedimentos_por_tipo(municipio_id_sus: str):
    ProcedimentosPorTipo_dados = (
        session.query(ProcedimentosPorTipo)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentosPorTipo_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return ProcedimentosPorTipo_dados
