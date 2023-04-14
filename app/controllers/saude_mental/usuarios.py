import pandas as pd
from fastapi import HTTPException, Response

from app.models import db
from app.models.saude_mental.perfildeusuarios import ( UsuariosPerfil, UsuariosPerfilEstabelecimento, UsuariosPerfilCondicao, UsuariosPerfilIdadeRaca)
from app.models.saude_mental.usuariosnovos import ( UsuariosNovosPerfil, UsuariosNovosResumo)

session = db.session


def obter_usuarios_perfil(
    municipio_id_sus: str,
):
    # usuarios_perfil = (
    #     session.query(UsuariosPerfil)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )
    usuarios_perfil = pd.read_parquet(
        f"data/caps_usuarios_ativos_perfil_{municipio_id_sus}.parquet",
    ).query("(estabelecimento_linha_perfil != 'Todos' & estabelecimento_linha_idade != 'Todos') | estabelecimento == 'Todos'")

    if len(usuarios_perfil) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dado perfil do usuario não encontrado."
            ),
        )

    return Response(
        usuarios_perfil.to_json(orient="records"),
        media_type="application/json",
    )


def obter_usuarios_perfil_estabelecimento(
    municipio_id_sus: str,
):
    usuarios_perfil_estabelecimento = (
        session.query(UsuariosPerfilEstabelecimento)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(usuarios_perfil_estabelecimento) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dado perfil estabelecimento não encontrado."
            ),
        )

    return usuarios_perfil_estabelecimento


def obter_usuarios_perfil_condicao(
    municipio_id_sus: str,
):
    usuarios_perfil_condicao = (
        session.query(UsuariosPerfilCondicao)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(usuarios_perfil_condicao) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dado perfil do usuario não encontrado."
            ),
        )

    return usuarios_perfil_condicao


def obter_usuarios_perfil_idade_raca(
    municipio_id_sus: str,
):
    usuarios_perfil_idade_raca = (
        session.query(UsuariosPerfilIdadeRaca)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(usuarios_perfil_idade_raca) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dado perfil estabelecimento não encontrado."
            ),
        )

    return usuarios_perfil_idade_raca


def obter_usuarios_novos(
    municipio_id_sus: str,
):
    # usuarios_novos = (
    #     session.query(UsuariosNovosPerfil)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )

    usuarios_novos = pd.read_parquet(
        f"data/caps_usuarios_novos_perfil_{municipio_id_sus}.parquet",
    ).query("(estabelecimento_linha_perfil != 'Todos' & estabelecimento_linha_idade != 'Todos') | estabelecimento == 'Todos'")

    if len(usuarios_novos) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dados usuarios novos não encontrados."
            ),
        )

    return Response(
        usuarios_novos.to_json(orient="records"),
        media_type="application/json",
    )


def obter_usuarios_novos_resumo(
    municipio_id_sus: str,
):
    usuarios_novos_resumo = (
        session.query(UsuariosNovosResumo)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(usuarios_novos_resumo) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dados usuarios resumo novos não encontrados."
            ),
        )

    return usuarios_novos_resumo
