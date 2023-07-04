from typing import Literal, Union

from fastapi import HTTPException
from sqlalchemy import exc

from app.models.db import session
from app.models.saude_mental.perfildeusuarios import UsuarioAtivoPorCondicao
from app.models.saude_mental.usuariosnovos import UsuarioNovoPorCondicao

entidades = {
    "usuarios_ativos_perfil": UsuarioAtivoPorCondicao,
    "usuarios_novos_perfil": UsuarioNovoPorCondicao,
}

Entidade = Literal["usuarios_ativos_perfil", "usuarios_novos_perfil"]
Model = Union[UsuarioAtivoPorCondicao, UsuarioNovoPorCondicao]


def obter_model_de_entidade(entidade: Entidade) -> Model:
    model = entidades.get(entidade)

    if model is None:
        raise HTTPException(
            status_code=400,
            detail=("Entidade informada é inválida"),
        )

    return model


def obter_estabelecimentos_de_entidade_por_id_sus(municipio_id_sus: str, entidade: str):
    try:
        model = obter_model_de_entidade(entidade=entidade)
        estabelecimentos = (
            session.query(model.estabelecimento)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        if len(estabelecimentos) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Estabelecimentos de município não encontrados"),
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


def obter_periodos_de_entidade_por_id_sus(municipio_id_sus: str, entidade: str):
    try:
        model = obter_model_de_entidade(entidade=entidade)
        periodos = (
            session.query(
                model.periodo,
                model.competencia,
            )
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        if len(periodos) == 0:
            raise HTTPException(
                status_code=404,
                detail=("Períodos de município não encontrados"),
            )

        return periodos
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