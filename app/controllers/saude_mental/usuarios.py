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


def consultar_usuarios_ativos_por_estabelecimento(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str
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
            UsuariosPerfilEstabelecimento.dif_tornandose_inativos_anterior
        ).filter(
            UsuariosPerfilEstabelecimento.unidade_geografica_id_sus == municipio_id_sus,
            UsuariosPerfilEstabelecimento.estabelecimento_linha_idade == "Todos",
            UsuariosPerfilEstabelecimento.estabelecimento_linha_perfil == "Todos"
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string("-", estabelecimentos)
            query = query.filter(
                UsuariosPerfilEstabelecimento.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string("-", periodos)
            query = query.filter(
                UsuariosPerfilEstabelecimento.periodo.in_(lista_periodos)
            )

        usuarios_ativos = query.all()

        return usuarios_ativos
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
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


def consultar_usuarios_novos_resumo(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    linhas_de_perfil: str,
    linhas_de_idade: str
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
            lista_estabelecimentos = separar_string("-", estabelecimentos)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string("-", periodos)
            query = query.filter(
                UsuariosNovosResumo.periodo.in_(lista_periodos)
            )

        if linhas_de_perfil is not None:
            lista_linhas_de_perfil = separar_string("-", linhas_de_perfil)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento_linha_perfil.in_(
                    lista_linhas_de_perfil
                )
            )

        if linhas_de_idade is not None:
            lista_linhas_de_idade = separar_string("-", linhas_de_idade)
            query = query.filter(
                UsuariosNovosResumo.estabelecimento_linha_idade.in_(lista_linhas_de_idade)
            )

        usuarios_novos = query.all()

        return usuarios_novos
    except (Exception) as error:
        session.rollback()

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
