from typing import Literal, Union
from fastapi import HTTPException
from sqlalchemy import exc

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

def obter_model_de_entidade(entidade: Entidade) -> Model:
    model = entidades.get(entidade)

    if model is None:
        raise HTTPException(
            status_code=400,
            detail=("Entidade informada é inválida"),
        )

    return model