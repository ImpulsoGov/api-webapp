import pandas as pd
from fastapi import HTTPException, Response
from sqlalchemy import exc

from app.models import db
from app.models.saude_mental.abandono import (
    AbandonoCoortes,
    AbandonoMensal,
    AbandonoPorCID,
    AbandonoPorGeneroEIdade,
)
from app.utils.separar_string import separar_string

session = db.session


def dados_caps_adesao_usuarios_perfil(municipio_id_sus: str):
    # dados_caps_adesao_usuarios_perfil = (
    #     session.query(AbandonoPerfil)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )

    dados_caps_adesao_usuarios_perfil = pd.read_parquet(
        f"data/caps_adesao_usuarios_perfil_{municipio_id_sus}.parquet",
    )

    if len(dados_caps_adesao_usuarios_perfil) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de Caps Adesão usuarios perfil não encontrado",
        )

    return Response(
        dados_caps_adesao_usuarios_perfil.to_json(orient="records"),
        media_type="application/json",
    )


def dados_caps_adesao_evasao_coortes_resumo(municipio_id_sus: str):
    dados_caps_adesao_evasao_coortes_resumo = (
        session.query(AbandonoCoortes)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_caps_adesao_evasao_coortes_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados de Abandono Coortes não encontrados",),
        )

    return dados_caps_adesao_evasao_coortes_resumo


def dados_caps_adesao_evasao_mensal(municipio_id_sus: str):
    dados_caps_adesao_evasao_mensal = (
        session.query(AbandonoMensal)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(dados_caps_adesao_evasao_mensal) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados de evasão mensal não encontrados",),
        )

    return dados_caps_adesao_evasao_mensal


def obter_perfil_evadiram_no_mes_por_cid(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        adesao_por_cid = (
            session.query(AbandonoPorCID)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(estatus_adesao_mes="Evadiram no mês")
            .filter(AbandonoPorCID.periodo.in_(lista_periodos))
            .all()
        )

        return adesao_por_cid
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_evadiram_no_mes_por_genero_e_idade(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        adesao_por_genero_e_idade = (
            session.query(AbandonoPorGeneroEIdade)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(estatus_adesao_mes="Evadiram no mês")
            .filter(AbandonoPorGeneroEIdade.periodo.in_(lista_periodos))
            .all()
        )

        return adesao_por_genero_e_idade
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
