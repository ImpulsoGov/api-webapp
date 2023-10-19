import pandas as pd
from fastapi import HTTPException, Response

from app.models import db
from app.models.saude_mental.procedimentos import (
    ProcedimentoPorUsuarioEstabelecimento,
    ProcedimentoPorUsuarioResumo,
    ProcedimentoPorUsuarioTempoServiço,
    ProcedimentosPorHora,
    ProcedimentosPorTipo,
)

session = db.session


def dados_procedimentos_por_usuario_estabelecimento(municipio_id_sus: str):
    ProcedimentoPorUsuarioEstabelecimento_dados = (
        session.query(ProcedimentoPorUsuarioEstabelecimento)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(ProcedimentoPorUsuarioEstabelecimento_dados) == 0:
        raise HTTPException(
            status_code=404,
            detail=("Matriciamentos CAPS no último ano " "do município não encontrados"),
        )

    return ProcedimentoPorUsuarioEstabelecimento_dados


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


def dados_procedimentos_por_usuario_tempo_servico(municipio_id_sus: str):
    try:
        procedimentos_por_usuario_por_tempo_servico = (
            session.query(
                ProcedimentoPorUsuarioTempoServiço.id,
                ProcedimentoPorUsuarioTempoServiço.unidade_geografica_id_sus,
                ProcedimentoPorUsuarioTempoServiço.competencia,
                ProcedimentoPorUsuarioTempoServiço.tempo_servico_descricao,
                ProcedimentoPorUsuarioTempoServiço.procedimentos_por_usuario,
                ProcedimentoPorUsuarioTempoServiço.estabelecimento,
                ProcedimentoPorUsuarioTempoServiço.periodo,
                ProcedimentoPorUsuarioTempoServiço.nome_mes
            )
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return procedimentos_por_usuario_por_tempo_servico
    except (Exception) as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def dados_procedimentos_por_hora(municipio_id_sus: str):
    # procedimentos_por_hora = (
    #     session.query(ProcedimentosPorHora)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )
    procedimentos_por_hora = pd.read_parquet(
        f"data/caps_procedimentos_por_hora_resumo_{municipio_id_sus}.parquet",
    ).query("competencia > @pd.Timestamp(2022, 2, 1).date()")

    if len(procedimentos_por_hora) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return Response(
        procedimentos_por_hora.to_json(orient="records"),
        media_type="application/json",
    )


def dados_procedimentos_por_tipo(municipio_id_sus: str):
    # procedimentos_por_tipo = (
    #     session.query(ProcedimentosPorTipo)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )
    procedimentos_por_tipo = pd.read_parquet(
        f"data/caps_procedimentos_por_tipo_{municipio_id_sus}.parquet",
    ).query(
        "((estabelecimento_linha_perfil == 'Todos' & estabelecimento_linha_idade == 'Todos')) & competencia > @pd.Timestamp(2022, 2, 1).date()"
    )

    if len(procedimentos_por_tipo) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return Response(
        procedimentos_por_tipo.to_json(orient="records"),
        media_type="application/json",
    )
