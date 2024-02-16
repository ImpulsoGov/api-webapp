from app.models import db
from app.models.impulso_previne_nominal.diabeticos import Diabeticos
from fastapi import HTTPException, status
from cachetools import TTLCache

session = db.session


def diabeticos_equipe(municipio_id_sus, equipe):
    try:
        return (
            session.query(Diabeticos)
            .filter_by(municipio_id_sus=municipio_id_sus, equipe_ine_cadastro=equipe)
            .with_entities(
                Diabeticos.cidadao_nome,
                Diabeticos.cidadao_cpf_dt_nascimento,
                Diabeticos.identificacao_condicao_diabetes,
                Diabeticos.dt_ultima_consulta,
                Diabeticos.prazo_proxima_consulta,
                Diabeticos.status_usuario,
                Diabeticos.dt_solicitacao_hemoglobina_glicada_mais_recente,
                Diabeticos.prazo_proxima_solicitacao_hemoglobina,
                Diabeticos.acs_nome_cadastro,
                Diabeticos.equipe_ine_cadastro,
                Diabeticos.equipe_nome_cadastro,
                Diabeticos.dt_consulta_mais_recente,
                Diabeticos.dt_registro_producao_mais_recente,
                Diabeticos.atualizacao_data,
            )
            .order_by(Diabeticos.cidadao_nome)
            .all()
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


cache_hipertensao_aps = TTLCache(maxsize=38, ttl=24 * 60 * 60)


def diabetes_aps(municipio_id_sus):
    result = cache_hipertensao_aps.get(municipio_id_sus)
    try:
        if result is None:
            result = (
                session.query(Diabeticos)
                .filter_by(municipio_id_sus=municipio_id_sus)
                .with_entities(
                    Diabeticos.cidadao_nome,
                    Diabeticos.cidadao_cpf_dt_nascimento,
                    Diabeticos.identificacao_condicao_diabetes,
                    Diabeticos.dt_ultima_consulta,
                    Diabeticos.prazo_proxima_consulta,
                    Diabeticos.status_usuario,
                    Diabeticos.dt_solicitacao_hemoglobina_glicada_mais_recente,
                    Diabeticos.prazo_proxima_solicitacao_hemoglobina,
                    Diabeticos.acs_nome_cadastro,
                    Diabeticos.equipe_ine_cadastro,
                    Diabeticos.equipe_nome_cadastro,
                    Diabeticos.dt_consulta_mais_recente,
                    Diabeticos.criacao_data,
                    Diabeticos.dt_registro_producao_mais_recente,
                    Diabeticos.atualizacao_data,
                )
                .order_by(Diabeticos.cidadao_nome)
                .all()
            )
            cache_hipertensao_aps[municipio_id_sus] = result
        return result
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
