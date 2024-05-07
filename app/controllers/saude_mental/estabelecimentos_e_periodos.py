from typing import Literal, Union

from fastapi import HTTPException
from sqlalchemy import exc

from app.models.db import session
from app.models.saude_mental.abandono import AbandonoPorCID
from app.models.saude_mental.atendimentos_individuais import AtendimentoIndividualPorCID
from app.models.saude_mental.perfildeusuarios import UsuarioAtivoPorCondicao
from app.models.saude_mental.usuariosnovos import UsuarioNovoPorCondicao
from app.models.saude_mental.procedimentos import ProcedimentoPorUsuarioTempoServiço
from app.models.saude_mental.procedimentos import ProcedimentosPorHora
from app.models.saude_mental.procedimentos import ProcedimentosPorTipo
from app.models.saude_mental.reducaodedanos import ReducaoDanos
from app.models.saude_mental.ambulatorio import AmbulatorioAtendimentoResumo
from app.models.saude_mental.ambulatorio import AmbulatorioUsuariosPerfil
from app.models.saude_mental.configuracoes_estabelecimentos import EstabelecimentosAusentesPorPeriodo
entidades = {
    "usuarios_ativos_perfil": UsuarioAtivoPorCondicao,
    "usuarios_novos_perfil": UsuarioNovoPorCondicao,
    "atendimentos_inidividuais_perfil": AtendimentoIndividualPorCID,
    "abandono_perfil": AbandonoPorCID,
    "procedimentos_usuarios_tempo_servico": ProcedimentoPorUsuarioTempoServiço,
    "procedimentos_por_hora": ProcedimentosPorHora,
    "procedimentos_por_tipo": ProcedimentosPorTipo,
    "reducao_de_danos": ReducaoDanos,
    "atendimentos_resumo": AmbulatorioAtendimentoResumo,
    "usuarios_perfil": AmbulatorioUsuariosPerfil
}

Entidade = Literal[
    "usuarios_ativos_perfil",
    "usuarios_novos_perfil",
    "atendimentos_inidividuais_perfil",
    "abandono_perfil",
    "procedimentos_usuarios_tempo_servico",
    "procedimentos_por_hora",
    "procedimentos_por_tipo",
    "reducao_de_danos",
    "atendimentos_resumo",
    "usuarios_perfil"
]
Model = Union[
    UsuarioAtivoPorCondicao,
    UsuarioNovoPorCondicao,
    AtendimentoIndividualPorCID,
    AbandonoPorCID,
    ProcedimentoPorUsuarioTempoServiço,
    ProcedimentosPorHora,
    ProcedimentosPorTipo,
    ReducaoDanos,
    AmbulatorioAtendimentoResumo,
    AmbulatorioUsuariosPerfil
]
def construir_novo_periodo(periodo: dict, entidade: str):
    model = obter_model_de_entidade(entidade=entidade)
    competencia = periodo["competencia"]
    periodo_ordem = periodo["periodo_ordem"]
    nome_mes = periodo["nome_mes"]
    novo_periodo = converte_competencia_para_periodo(competencia)
    return model(periodo=novo_periodo, competencia=competencia, periodo_ordem=periodo_ordem, nome_mes=nome_mes)


def converte_competencia_para_periodo(competencia):
    periodo = competencia.strftime("%b/%y")
    return periodo

def obter_lista_estabelecimentos_ausentes_de_entidade_por_id_sus(municipio_id_sus: str, entidade: str):
    try: 
        model = obter_model_de_entidade(entidade=entidade)
        query = session.query(
            EstabelecimentosAusentesPorPeriodo.estabelecimento,
        ).filter(
            EstabelecimentosAusentesPorPeriodo.unidade_geografica_id_sus == municipio_id_sus,
            EstabelecimentosAusentesPorPeriodo.tabela_referencia == model.__tablename__
        )
        estabelecimentos_ausentes = query.distinct().all()
        return estabelecimentos_ausentes
    except (exc.SQLAlchemyError, Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
    
def obter_lista_periodos_ausentes_de_entidade_por_id_sus(municipio_id_sus: str, entidade: str):
    try:
        model = obter_model_de_entidade(entidade=entidade)
        query = session.query(
            EstabelecimentosAusentesPorPeriodo.periodo,
            EstabelecimentosAusentesPorPeriodo.competencia,
            EstabelecimentosAusentesPorPeriodo.periodo_ordem,
            EstabelecimentosAusentesPorPeriodo.nome_mes
        ).filter(
            EstabelecimentosAusentesPorPeriodo.unidade_geografica_id_sus == municipio_id_sus,
            EstabelecimentosAusentesPorPeriodo.tabela_referencia == model.__tablename__
        )
        periodos_ausentes = query.distinct().all()
        print(periodos_ausentes)
        return periodos_ausentes
    except (exc.SQLAlchemyError, Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )

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
        
        estabelecimentos_ausentes = obter_lista_estabelecimentos_ausentes_de_entidade_por_id_sus(municipio_id_sus, entidade=entidade)
        if all(estabelecimento_ausente in estabelecimentos for estabelecimento_ausente in estabelecimentos_ausentes):
            return estabelecimentos
        else:
            estabelecimentos = estabelecimentos + estabelecimentos_ausentes
            return estabelecimentos
        
    except HTTPException as error:
        raise error
    except (exc.SQLAlchemyError, Exception) as error:
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
                model.periodo_ordem,
                model.nome_mes
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

        periodos_ausentes = obter_lista_periodos_ausentes_de_entidade_por_id_sus(municipio_id_sus, entidade=entidade)
        if all(periodo_ausente in periodos for periodo_ausente in periodos_ausentes):
            return periodos
        else: #O último período que retorna da TR(tabela referencia) é o verdadeiro último período
               if any(periodo_ausente.periodo == "Último período" for periodo_ausente in periodos_ausentes):
                    index_antigo_ultimo_periodo = next((index for index, periodos in enumerate(periodos) if periodos.periodo == "Último período"), None)
                    if index_antigo_ultimo_periodo is not None:
                        periodos[index_antigo_ultimo_periodo] = construir_novo_periodo(periodos[index_antigo_ultimo_periodo], entidade=entidade)
                        periodos += periodos_ausentes
                        return periodos
               else:
                    periodos += periodos_ausentes
                    return periodos
    except HTTPException as error:
        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        error_details = {
        "type": type(error).__name__,
        "message": str(error)
    }
        print({"error": error_details})
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
