from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.procedimentos import (
    ProcedimentoPorUsuarioEstabelecimento,
    ProcedimentoPorUsuarioResumo,
    ProcedimentoPorUsuarioTempoServiço,
    ProcedimentosPorHora,
    ProcedimentosPorTipo,
)
from app.utils.separar_string import separar_string

session = db.session


def consultar_dados_procedimentos_por_usuario_estabelecimento(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    estabelecimento_linha_idade: str,
    estabelecimento_linha_perfil: str
):
    try:
        query = session.query(
            ProcedimentoPorUsuarioEstabelecimento
        ).filter(
            ProcedimentoPorUsuarioEstabelecimento.unidade_geografica_id_sus == municipio_id_sus
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                ProcedimentoPorUsuarioEstabelecimento.estabelecimento.in_(
                    lista_estabelecimentos
                )
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(
                ProcedimentoPorUsuarioEstabelecimento.periodo.in_(lista_periodos)
            )

        if estabelecimento_linha_idade is not None:
            lista_linhas_de_idade = separar_string(",", estabelecimento_linha_idade)
            query = query.filter(
                ProcedimentoPorUsuarioEstabelecimento.estabelecimento_linha_idade.in_(
                    lista_linhas_de_idade
                )
            )
        if estabelecimento_linha_perfil is not None:
            lista_linhas_de_perfil = separar_string(",", estabelecimento_linha_perfil)
            query = query.filter(
                ProcedimentoPorUsuarioEstabelecimento.estabelecimento_linha_perfil.in_(
                    lista_linhas_de_perfil
                )  
            )
        procedimentos_por_usuario_por_estabelecimento = query.all()

        return procedimentos_por_usuario_por_estabelecimento

    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )



def dados_procedimentos_por_usuario_resumo(municipio_id_sus: str):
    ProcedimentoPorUsuarioResumo_dados = (
        session.query(ProcedimentoPorUsuarioResumo)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentoPorUsuarioResumo_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return ProcedimentoPorUsuarioResumo_dados


def consultar_procedimentos_por_hora(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str,
    ocupacao: str
):
    try:
        query = session.query(
            ProcedimentosPorHora.id,
            ProcedimentosPorHora.unidade_geografica_id_sus,
            ProcedimentosPorHora.competencia,
            ProcedimentosPorHora.ocupacao,
            ProcedimentosPorHora.procedimentos_por_hora,
            ProcedimentosPorHora.estabelecimento,
            ProcedimentosPorHora.periodo,
            ProcedimentosPorHora.nome_mes,
            ProcedimentosPorHora.perc_dif_procedimentos_por_hora_anterior,
            ProcedimentosPorHora.procedimentos_registrados_raas,
            ProcedimentosPorHora.procedimentos_registrados_bpa,
            ProcedimentosPorHora.procedimentos_registrados_total,
            ProcedimentosPorHora.estabelecimento_linha_idade,
            ProcedimentosPorHora.estabelecimento_linha_perfil
        ).filter(ProcedimentosPorHora.unidade_geografica_id_sus == municipio_id_sus)

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)
            query = query.filter(
                ProcedimentosPorHora.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)
            query = query.filter(ProcedimentosPorHora.periodo.in_(lista_periodos))

        if ocupacao is not None:
            query = query.filter(ProcedimentosPorHora.ocupacao == ocupacao)

        procedimentos_por_hora = query.all()
        return procedimentos_por_hora
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_procedimentos_por_tipo(
    municipio_id_sus: str,
    estabelecimentos: str,
    procedimentos: str,
    periodos: str,
):
    try:
        query = session.query(
            ProcedimentosPorTipo.id,
            ProcedimentosPorTipo.unidade_geografica_id_sus,
            ProcedimentosPorTipo.competencia,
            ProcedimentosPorTipo.procedimento,
            ProcedimentosPorTipo.estabelecimento,
            ProcedimentosPorTipo.periodo,
            ProcedimentosPorTipo.nome_mes,
            ProcedimentosPorTipo.procedimentos_registrados_raas,
            ProcedimentosPorTipo.procedimentos_registrados_bpa,
            ProcedimentosPorTipo.procedimentos_registrados_total,
            ProcedimentosPorTipo.estabelecimento_linha_idade,
            ProcedimentosPorTipo.estabelecimento_linha_perfil
        ).filter(
            ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)

            query = query.filter(
                ProcedimentosPorTipo.estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)

            query = query.filter(
                ProcedimentosPorTipo.periodo.in_(lista_periodos)
            )

        if procedimentos is not None:
            lista_procedimentos = separar_string(",", procedimentos)

            query = query.filter(
                ProcedimentosPorTipo.procedimento.in_(lista_procedimentos)
            )

        procedimentos_por_tipo = query.all()

        return procedimentos_por_tipo
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_nomes_de_procedimentos_por_tipo(municipio_id_sus: str):
    try:
        nomes_de_procedimentos = (
            session.query(ProcedimentosPorTipo.procedimento)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .distinct()
            .all()
        )

        return nomes_de_procedimentos
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def consultar_procedimentos_por_usuario_tempo_servico(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str
):
    try:
        query = session.query(
            ProcedimentoPorUsuarioTempoServiço.id,
            ProcedimentoPorUsuarioTempoServiço.unidade_geografica_id_sus,
            ProcedimentoPorUsuarioTempoServiço.competencia,
            ProcedimentoPorUsuarioTempoServiço.tempo_servico_descricao,
            ProcedimentoPorUsuarioTempoServiço.procedimentos_por_usuario,
            ProcedimentoPorUsuarioTempoServiço.estabelecimento,
            ProcedimentoPorUsuarioTempoServiço.periodo,
            ProcedimentoPorUsuarioTempoServiço.nome_mes
        ).filter(
            ProcedimentoPorUsuarioTempoServiço
            .unidade_geografica_id_sus == municipio_id_sus,
        )

        if estabelecimentos is not None:
            lista_estabelecimentos = separar_string(",", estabelecimentos)

            query = query.filter(
                ProcedimentoPorUsuarioTempoServiço
                .estabelecimento.in_(lista_estabelecimentos)
            )

        if periodos is not None:
            lista_periodos = separar_string(",", periodos)

            query = query.filter(
                ProcedimentoPorUsuarioTempoServiço.periodo.in_(lista_periodos)
            )

        procedimentos_por_usuario_por_tempo_servico = query.all()

        return procedimentos_por_usuario_por_tempo_servico
    except (Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
