from fastapi import HTTPException
from app.models import db
from app.models.saude_mental.ambulatorio import (
    AmbulatorioAtendimentoResumo,
    AmbulatorioAtendimentoResumoUltimoMes,
    AmbulatorioProcedimentosPorProfissional,
    AmbulatorioUsuariosPerfil,
)
from app.utils.separar_string import separar_string

session = db.session


def consultar_dados_ambulatorio_atendimento_resumo(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str
):
    try:
        query = session.query(AmbulatorioAtendimentoResumo).filter(
            AmbulatorioAtendimentoResumo.unidade_geografica_id_sus == municipio_id_sus
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                AmbulatorioAtendimentoResumo.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(AmbulatorioAtendimentoResumo.periodo.in_(lista_periodos))    

        ambulatorio_atendimento_resumo = query.all()
        return ambulatorio_atendimento_resumo
    except (Exception) as error:
        session.rollback()
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_ambulatorio_atendimento_resumo_ultimo_mes(
    municipio_id_sus: str,
):
    try:
        ambulatorio_atendimento_resumo_ultimo_mes = (
            session.query(AmbulatorioAtendimentoResumoUltimoMes)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return ambulatorio_atendimento_resumo_ultimo_mes
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_ambulatorio_procedimento_por_profissional(
    municipio_id_sus: str,
):
    try:
        ambulatorio_procedimento_por_profissional = (
            session.query(AmbulatorioProcedimentosPorProfissional)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return ambulatorio_procedimento_por_profissional
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_ambulatorio_usuario_perfil(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
):
    try:
        query = session.query(
            AmbulatorioUsuariosPerfil
        ).filter(AmbulatorioUsuariosPerfil.unidade_geografica_id_sus == municipio_id_sus)

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                AmbulatorioUsuariosPerfil.estabelecimento.in_(lista_estabelecimentos)
            )
        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(AmbulatorioUsuariosPerfil.periodo.in_(lista_periodos))

        ambulatorio_usuario_perfil = query.all()
        return ambulatorio_usuario_perfil

    except (Exception) as error:
        session.rollback()
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
