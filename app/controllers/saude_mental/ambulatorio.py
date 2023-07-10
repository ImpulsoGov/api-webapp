from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.ambulatorio import (
    AmbulatorioAtendimentoResumo,
    AmbulatorioAtendimentoResumoUltimoMes,
    AmbulatorioProcedimentosPorProfissional,
    AmbulatorioUsuariosPerfil,
)

session = db.session


def obter_ambulatorio_atendimento_resumo(
    municipio_id_sus: str,
):
    ambulatorio_atendimento_resumo = (
        session.query(AmbulatorioAtendimentoResumo)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ambulatorio_atendimento_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados não encontrados",),
        )

    return ambulatorio_atendimento_resumo


def obter_ambulatorio_atendimento_resumo_ultimo_mes(
    municipio_id_sus: str,
):
    ambulatorio_atendimento_resumo_ultimo_mes = (
        session.query(AmbulatorioAtendimentoResumoUltimoMes)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ambulatorio_atendimento_resumo_ultimo_mes) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados não encontrados",),
        )

    return ambulatorio_atendimento_resumo_ultimo_mes


def obter_ambulatorio_procedimento_por_profissional(
    municipio_id_sus: str,
):
    ambulatorio_procedimento_por_profissional = (
        session.query(AmbulatorioProcedimentosPorProfissional)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ambulatorio_procedimento_por_profissional) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados não encontrados",),
        )

    return ambulatorio_procedimento_por_profissional


def obter_ambulatorio_usuario_perfil(
    municipio_id_sus: str,
):
    ambulatorio_usuario_perfil = (
        session.query(AmbulatorioUsuariosPerfil)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ambulatorio_usuario_perfil) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados não encontrados",),
        )

    return ambulatorio_usuario_perfil
