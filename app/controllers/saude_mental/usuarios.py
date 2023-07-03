import pandas as pd
from fastapi import HTTPException, Response
from sqlalchemy import exc

from app.models import db
from app.models.saude_mental.perfildeusuarios import (
    UsuarioAtivoPorCID,
    UsuarioAtivoPorCondicao,
    UsuarioAtivoPorGeneroEIdade,
    UsuarioAtivoPorRaca,
    UsuariosPerfilCondicao,
    UsuariosPerfilEstabelecimento,
    UsuariosPerfilIdadeRaca,
)
from app.models.saude_mental.usuariosnovos import (
    UsuarioNovoPorCID,
    UsuarioNovoPorCondicao,
    UsuarioNovoPorGeneroEIdade,
    UsuarioNovoPorRaca,
    UsuariosNovosResumo,
)

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
    ).query(
        "(estabelecimento_linha_perfil == 'Todos' & estabelecimento_linha_idade == 'Todos')"
    )

    if len(usuarios_perfil) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dado perfil do usuario não encontrado."),
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
            detail=("Dado perfil estabelecimento não encontrado."),
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
            detail=("Dado perfil do usuario não encontrado."),
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
            detail=("Dado perfil estabelecimento não encontrado."),
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
    ).query(
        "(estabelecimento_linha_perfil == 'Todos' & estabelecimento_linha_idade == 'Todos') | estabelecimento == 'Todos'"
    )

    if len(usuarios_novos) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Dados usuarios novos não encontrados."),
        )

    return Response(
        usuarios_novos.to_json(orient="records"),
        media_type="application/json",
    )


def obter_usuarios_novos_resumo(
    municipio_id_sus: str,
):
    try:
        usuarios_novos_resumo = (
            session.query(UsuariosNovosResumo)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        if len(usuarios_novos_resumo) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados usuarios resumo novos não encontrados."),
            )

        return usuarios_novos_resumo
    except exc.SQLAlchemyError as e:
        session.rollback()

        error = str(e)

        print({"error": error})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_ativos_por_condicao(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    try:
        usuarios_ativos_por_condicao = (
            session.query(UsuarioAtivoPorCondicao)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(periodo=periodo)
            .all()
        )

        if len(usuarios_ativos_por_condicao) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados de condição de usuários ativos não encontrados."),
            )

        return usuarios_ativos_por_condicao
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_ativos_por_genero_e_idade(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    try:
        usuarios_ativos_por_genero_e_idade = (
            session.query(UsuarioAtivoPorGeneroEIdade)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(periodo=periodo)
            .all()
        )

        if len(usuarios_ativos_por_genero_e_idade) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados de gênero/idade de usuários ativos não encontrados."),
            )

        return usuarios_ativos_por_genero_e_idade
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_ativos_por_raca(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    try:
        usuarios_ativos_por_raca = (
            session.query(UsuarioAtivoPorRaca)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(periodo=periodo)
            .all()
        )

        if len(usuarios_ativos_por_raca) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados de raça/cor de usuários ativos não encontrados."),
            )

        return usuarios_ativos_por_raca
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_ativos_por_cid(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    try:
        usuarios_ativos_por_cid = (
            session.query(UsuarioAtivoPorCID)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(periodo=periodo)
            .all()
        )

        if len(usuarios_ativos_por_cid) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados de cid de usuários ativos não encontrados."),
            )

        return usuarios_ativos_por_cid
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_estabelecimentos_por_id_sus(municipio_id_sus: str):
    try:
        estabelecimentos = (
            session.query(UsuarioAtivoPorCondicao.estabelecimento)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        if len(estabelecimentos) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Estabelecimentos de município não encontrados."),
            )

        return estabelecimentos
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_periodos_por_id_sus(municipio_id_sus: str):
    try:
        estabelecimentos = (
            session.query(
                UsuarioAtivoPorCondicao.periodo,
                UsuarioAtivoPorCondicao.competencia,
            )
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        if len(estabelecimentos) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Estabelecimentos de município não encontrados."),
            )

        return estabelecimentos
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_novos_por_condicao(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    try:
        usuarios_novos_por_condicao = (
            session.query(UsuarioNovoPorCondicao)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter_by(periodo=periodo)
            .all()
        )

        if len(usuarios_novos_por_condicao) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Dados de condição de usuários novos não encontrados."),
            )

        return usuarios_novos_por_condicao
    except HTTPException as error:
        session.rollback()

        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )

