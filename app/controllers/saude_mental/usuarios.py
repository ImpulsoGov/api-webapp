from fastapi import HTTPException
from sqlalchemy import exc

from app.models import db
from app.models.saude_mental.perfildeusuarios import (
    UsuarioAtivoPorCID,
    UsuarioAtivoPorCondicao,
    UsuarioAtivoPorGeneroEIdade,
    UsuarioAtivoPorRaca,
    UsuariosPerfilEstabelecimento,
)
from app.models.saude_mental.usuariosnovos import (
    UsuarioNovoPorCID,
    UsuarioNovoPorCondicao,
    UsuarioNovoPorGeneroEIdade,
    UsuarioNovoPorRaca,
    UsuariosNovosResumo,
)
from app.utils.separar_string import separar_string

session = db.session


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

        return usuarios_ativos_por_condicao
    except (Exception) as error:
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

        return usuarios_ativos_por_genero_e_idade
    except (Exception) as error:
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

        return usuarios_ativos_por_raca
    except (Exception) as error:
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

        return usuarios_ativos_por_cid
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_novos_por_condicao(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        usuarios_novos_por_condicao = (
            session.query(UsuarioNovoPorCondicao)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(UsuarioNovoPorCondicao.periodo.in_(lista_periodos))
            .all()
        )

        return usuarios_novos_por_condicao
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_novos_por_genero_e_idade(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        usuarios_novos_por_genero_e_idade = (
            session.query(UsuarioNovoPorGeneroEIdade)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(UsuarioNovoPorGeneroEIdade.periodo.in_(lista_periodos))
            .all()
        )

        return usuarios_novos_por_genero_e_idade
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_novos_por_raca(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        usuarios_novos_por_raca = (
            session.query(UsuarioNovoPorRaca)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(UsuarioNovoPorRaca.periodo.in_(lista_periodos))
            .all()
        )

        return usuarios_novos_por_raca
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def obter_perfil_usuarios_novos_por_cid(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    try:
        lista_periodos = separar_string(separador="-", string=periodos)
        usuarios_novos_por_cid = (
            session.query(UsuarioNovoPorCID)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .filter_by(estabelecimento=estabelecimento)
            .filter(UsuarioNovoPorCID.periodo.in_(lista_periodos))
            .all()
        )

        return usuarios_novos_por_cid
    except (exc.SQLAlchemyError, Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
