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
from app.utils.separar_string import separar_string

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
    # procedimentos_por_usuario_por_tempo_servico = (
    #     session.query(ProcedimentoPorUsuarioTempoServiço)
    #     .filter_by(unidade_geografica_id_sus=municipio_id_sus)
    #     .all()
    # )

    procedimentos_por_usuario_por_tempo_servico = pd.read_parquet(
        f"data/caps_procedimentos_por_usuario_por_tempo_servico_{municipio_id_sus}.parquet",
    ).query(
        "((estabelecimento_linha_perfil == 'Todos' & estabelecimento_linha_idade == 'Todos')) & competencia > @pd.Timestamp(2022, 11, 1).date()"
    )

    if len(procedimentos_por_usuario_por_tempo_servico) == 0:
        raise HTTPException(
            status_code=404,
            detail="Matriciamentos no último ano do município não encontrados",
        )

    return Response(
        procedimentos_por_usuario_por_tempo_servico.to_json(orient="records"),
        media_type="application/json",
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


def consultar_procedimentos_por_hora(
    municipio_id_sus: str,
    estabelecimentos: str,
    periodos: str
):
    try:
        if estabelecimentos is not None and periodos is None:
            lista_estabelecimentos = separar_string("-", estabelecimentos)

            procedimentos_por_hora = (
                session.query(
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
                )
                .filter(
                    ProcedimentosPorHora.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorHora.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_hora

        if estabelecimentos is None and periodos is not None:
            lista_periodos = separar_string("-", periodos)

            procedimentos_por_hora = (
                session.query(
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
                )
                .filter(
                    ProcedimentosPorHora.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorHora.periodo.in_(lista_periodos)
                )
                .all()
            )

            return procedimentos_por_hora

        if estabelecimentos is not None and periodos is not None:
            lista_periodos = separar_string("-", periodos)
            lista_estabelecimentos = separar_string("-", estabelecimentos)

            procedimentos_por_hora = (
                session.query(
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
                )
                .filter(
                    ProcedimentosPorHora.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorHora.periodo.in_(lista_periodos),
                    ProcedimentosPorHora.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_hora

        procedimentos_por_hora = (
            session.query(
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
            )
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .all()
        )

        return procedimentos_por_hora
    except (Exception) as error:
        session.rollback()

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
        )

        if estabelecimentos is not None and periodos is None and procedimentos is None:
            lista_estabelecimentos = separar_string("-", estabelecimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is None and procedimentos is None and periodos is not None:
            lista_periodos = separar_string("-", periodos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.periodo.in_(lista_periodos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is not None and periodos is not None and procedimentos is None:
            lista_periodos = separar_string("-", periodos)
            lista_estabelecimentos = separar_string("-", estabelecimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.periodo.in_(lista_periodos),
                    ProcedimentosPorTipo.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is None and periodos is None and procedimentos is not None:
            lista_procedimentos = separar_string("-", procedimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.procedimento.in_(lista_procedimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is None and periodos is not None and procedimentos is not None:
            lista_periodos = separar_string("-", periodos)
            lista_procedimentos = separar_string("-", procedimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.periodo.in_(lista_periodos),
                    ProcedimentosPorTipo.procedimento.in_(lista_procedimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is not None and periodos is None and procedimentos is not None:
            lista_estabelecimentos = separar_string("-", estabelecimentos)
            lista_procedimentos = separar_string("-", procedimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.estabelecimento.in_(lista_estabelecimentos),
                    ProcedimentosPorTipo.procedimento.in_(lista_procedimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        if estabelecimentos is not None and periodos is not None and procedimentos is not None:
            lista_periodos = separar_string("-", periodos)
            lista_estabelecimentos = separar_string("-", estabelecimentos)
            lista_procedimentos = separar_string("-", procedimentos)

            procedimentos_por_tipo = (
                query.filter(
                    ProcedimentosPorTipo.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentosPorTipo.periodo.in_(lista_periodos),
                    ProcedimentosPorTipo.estabelecimento.in_(lista_estabelecimentos),
                    ProcedimentosPorTipo.procedimento.in_(lista_procedimentos)
                )
                .all()
            )

            return procedimentos_por_tipo

        procedimentos_por_tipo = (
            query.filter_by(unidade_geografica_id_sus=municipio_id_sus).all()
        )

        return procedimentos_por_tipo
    except (Exception) as error:
        session.rollback()

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
        if estabelecimentos is not None and periodos is None:
            lista_estabelecimentos = separar_string("-", estabelecimentos)

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
                .filter(
                    ProcedimentoPorUsuarioTempoServiço.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentoPorUsuarioTempoServiço.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_usuario_por_tempo_servico

        if estabelecimentos is None and periodos is not None:
            lista_periodos = separar_string("-", periodos)

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
                .filter(
                    ProcedimentoPorUsuarioTempoServiço.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentoPorUsuarioTempoServiço.periodo.in_(lista_periodos)
                )
                .all()
            )

            return procedimentos_por_usuario_por_tempo_servico

        if estabelecimentos is not None and periodos is not None:
            lista_periodos = separar_string("-", periodos)
            lista_estabelecimentos = separar_string("-", estabelecimentos)

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
                .filter(
                    ProcedimentoPorUsuarioTempoServiço.unidade_geografica_id_sus == municipio_id_sus,
                    ProcedimentoPorUsuarioTempoServiço.periodo.in_(lista_periodos),
                    ProcedimentoPorUsuarioTempoServiço.estabelecimento.in_(lista_estabelecimentos)
                )
                .all()
            )

            return procedimentos_por_usuario_por_tempo_servico

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
