import pandas as pd
from fastapi import HTTPException, Response
from sqlalchemy import exc

from app.models import db
from app.models.saude_mental.atendimentos_individuais import (
    AtendimentoIndividualPorCID,
    AtendimentoIndividualPorGeneroEIdade,
    AtendimentoIndividualPorRaca,
    AtendimentosIndividuaisPorCaps,
    ResumoPerfilUsuariosAtendimentosIndividuaisCaps,
)
from app.utils.separar_string import separar_string

session = db.session


def obter_atendimentos_individuais_por_caps_de_municipio(municipio_id_sus: str):
    atendimentos_individuais_caps = (
        session.query(AtendimentosIndividuaisPorCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(atendimentos_individuais_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de atendimentos individuais CAPS "
            "do município não encontrados",
        )

    return atendimentos_individuais_caps


def obter_perfil_usuarios_caps_por_id_sus(municipio_id_sus: str):
    # perfil_usuarios_caps = (
    #     session.query(PerfilUsuariosAtendimentosIndividuaisCaps)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )

    perfil_usuarios_caps = pd.read_parquet(
        f"data/caps_usuarios_atendimentos_individuais_perfil_{municipio_id_sus}.parquet",
    ).query(
        "(estabelecimento_linha_perfil == 'Todos' & estabelecimento_linha_idade == 'Todos') | estabelecimento == 'Todos'"
    )

    if len(perfil_usuarios_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de perfil de usuários CAPS " "do município não encontrados",
        )

    return Response(
        perfil_usuarios_caps.to_json(orient="records"),
        media_type="application/json",
    )


def obter_resumo_perfil_usuarios_caps_por_id_sus(municipio_id_sus: str):
    resumo_perfil_usuarios_caps = (
        session.query(ResumoPerfilUsuariosAtendimentosIndividuaisCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(resumo_perfil_usuarios_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Resumo do perfil de usuários CAPS " "do município não encontrado",
        )

    return resumo_perfil_usuarios_caps


def obter_perfil_atendimentos_individuais_por_cid(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        atendimentos_individuais_por_cid = (
            session.query(AtendimentoIndividualPorCID)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(AtendimentoIndividualPorCID.periodo.in_(lista_periodos))
            .all()
        )

        return atendimentos_individuais_por_cid
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_atendimentos_individuais_por_genero_e_idade(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        atendimentos_individuais_por_genero_e_idade = (
            session.query(AtendimentoIndividualPorGeneroEIdade)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(AtendimentoIndividualPorGeneroEIdade.periodo.in_(lista_periodos))
            .all()
        )

        return atendimentos_individuais_por_genero_e_idade
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_atendimentos_individuais_por_raca(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        atendimentos_individuais_por_raca = (
            session.query(AtendimentoIndividualPorRaca)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(AtendimentoIndividualPorRaca.periodo.in_(lista_periodos))
            .all()
        )

        return atendimentos_individuais_por_raca
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
