from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.reducaodedanos import ReducaoDanos, ReducaoDanos12meses
from app.utils.separar_string import separar_string

session = db.session


def consultar_reducao_de_danos(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    ocupacoes: str
):
    try:
        query = session.query(
            ReducaoDanos.id,
            ReducaoDanos.unidade_geografica_id_sus,
            ReducaoDanos.estabelecimento,
            ReducaoDanos.profissional_vinculo_ocupacao,
            ReducaoDanos.periodo,
            ReducaoDanos.quantidade_registrada,
            ReducaoDanos.nome_mes,
            ReducaoDanos.dif_quantidade_registrada_anterior,
            ReducaoDanos.competencia,
            ReducaoDanos.estabelecimento_linha_idade,
            ReducaoDanos.estabelecimento_linha_perfil
        ).filter(ReducaoDanos.unidade_geografica_id_sus == municipio_id_sus)

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                ReducaoDanos.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(ReducaoDanos.periodo.in_(lista_periodos))

        if ocupacoes is not None:
            lista_ocupacoes = separar_string(",", ocupacoes)
            query = query.filter(ReducaoDanos.profissional_vinculo_ocupacao.in_(lista_ocupacoes))

        procedimentos_por_hora = query.all()

        return procedimentos_por_hora
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_nomes_de_ocupacoes_reducao_de_danos(municipio_id_sus: str):
    try:
        nomes_de_ocupacoes = (
            session.query(ReducaoDanos.profissional_vinculo_ocupacao)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        return nomes_de_ocupacoes
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def dados_reducaodedanos_12meses(
    municipio_id_sus: str,
):
    try:
        dados_reducaodedanos_12meses = (
            session.query(ReducaoDanos12meses)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return dados_reducaodedanos_12meses
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
