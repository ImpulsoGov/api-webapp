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


def consultar_usuarios_ativos_por_estabelecimento(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    estabelecimento_linha_perfil: str,
    estabelecimento_linha_idade: str
):
    try:
        query = session.query(
            UsuariosPerfilEstabelecimento.id,
            UsuariosPerfilEstabelecimento.unidade_geografica_id_sus,
            UsuariosPerfilEstabelecimento.competencia,
            UsuariosPerfilEstabelecimento.estabelecimento,
            UsuariosPerfilEstabelecimento.periodo,
            UsuariosPerfilEstabelecimento.nome_mes,
            UsuariosPerfilEstabelecimento.ativos_mes,
            UsuariosPerfilEstabelecimento.dif_ativos_mes_anterior,
            UsuariosPerfilEstabelecimento.ativos_3meses,
            UsuariosPerfilEstabelecimento.dif_ativos_3meses_anterior,
            UsuariosPerfilEstabelecimento.tornandose_inativos,
            UsuariosPerfilEstabelecimento.dif_tornandose_inativos_anterior,
            UsuariosPerfilEstabelecimento.sexo_predominante,
            UsuariosPerfilEstabelecimento.usuarios_idade_media,
        ).filter(
            UsuariosPerfilEstabelecimento.unidade_geografica_id_sus == municipio_id_sus,
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                UsuariosPerfilEstabelecimento.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(
                UsuariosPerfilEstabelecimento.periodo.in_(lista_periodos)
            )

        if estabelecimento_linha_perfil is not None:
            lista_linhas_de_perfil = separar_string(",", estabelecimento_linha_perfil)
            query = query.filter(
                UsuariosPerfilEstabelecimento.estabelecimento_linha_perfil.in_(
                    lista_linhas_de_perfil
                )
            )

        if estabelecimento_linha_idade is not None:
            lista_linhas_de_idade = separar_string(",", estabelecimento_linha_idade)
            query = query.filter(
                UsuariosPerfilEstabelecimento.estabelecimento_linha_idade.in_(
                    lista_linhas_de_idade
                )
            )

        usuarios_ativos = query.all()

        return usuarios_ativos
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_usuarios_novos_resumo(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    estabelecimento_linha_perfil: str,
    estabelecimento_linha_idade: str
):
    try:
        query = session.query(
            UsuariosNovosResumo.id,
            UsuariosNovosResumo.unidade_geografica_id_sus,
            UsuariosNovosResumo.competencia,
            UsuariosNovosResumo.estabelecimento,
            UsuariosNovosResumo.periodo,
            UsuariosNovosResumo.nome_mes,
            UsuariosNovosResumo.usuarios_novos,
            UsuariosNovosResumo.dif_usuarios_novos_anterior,
            UsuariosNovosResumo.estabelecimento_linha_perfil
        ).filter(
            UsuariosNovosResumo.unidade_geografica_id_sus == municipio_id_sus,
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(
                UsuariosNovosResumo.periodo.in_(lista_periodos)
            )

        if estabelecimento_linha_perfil is not None:
            lista_linhas_de_perfil = separar_string(",", estabelecimento_linha_perfil)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento_linha_perfil.in_(
                    lista_linhas_de_perfil
                )
            )

        if estabelecimento_linha_idade is not None:
            lista_linhas_de_idade = separar_string(",", estabelecimento_linha_idade)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento_linha_idade.in_(lista_linhas_de_idade)
            )

        usuarios_novos = query.all()

        return usuarios_novos
    except (Exception) as error:
        print({"error": str(error)})
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
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
