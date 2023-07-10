import pandas as pd
from fastapi import HTTPException, Response

from app.models import db
from app.models.saude_mental.abandono import (
    AbandonoCoortes,
    AbandonoMensal,
    AbandonoPerfil,
)

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
