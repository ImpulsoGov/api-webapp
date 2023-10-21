from app.models import db  
from app.models.impulso_previne_nominal.hipertensos import Hipertensos
from fastapi import HTTPException, status
from cachetools import TTLCache
session = db.session

cache_hipertensao_aps = TTLCache(maxsize=38, ttl=24*60*60)
def hipertensao_aps(municipio_id_sus):
    result = cache_hipertensao_aps.get(municipio_id_sus)
    try:
        if result is None:
            result = session.query(
                Hipertensos).filter_by(
                municipio_id_sus=municipio_id_sus
                ).with_entities(
                    Hipertensos.cidadao_nome,
                    Hipertensos.cidadao_cpf_dt_nascimento,
                    Hipertensos.identificacao_condicao_hipertensao,
                    Hipertensos.dt_ultima_consulta,
                    Hipertensos.prazo_proxima_consulta,
                    Hipertensos.status_usuario,
                    Hipertensos.dt_afericao_pressao_mais_recente,
                    Hipertensos.prazo_proxima_afericao_pa,
                    Hipertensos.acs_nome_cadastro,
                    Hipertensos.equipe_ine_cadastro,
                    Hipertensos.equipe_nome_cadastro,
                    Hipertensos.dt_consulta_mais_recente,
                    Hipertensos.dt_registro_producao_mais_recente
                ).order_by(
                    Hipertensos.cidadao_nome
                ).all()
            cache_hipertensao_aps[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )

def hipertensao_equipe(municipio_id_sus,equipe):
    try:
        return session.query(
                Hipertensos
                ).filter_by(
                municipio_id_sus=municipio_id_sus,
                equipe_ine_cadastro=equipe
                ).with_entities(
                    Hipertensos.cidadao_nome,
                    Hipertensos.cidadao_cpf_dt_nascimento,
                    Hipertensos.identificacao_condicao_hipertensao,
                    Hipertensos.dt_ultima_consulta,
                    Hipertensos.prazo_proxima_consulta,
                    Hipertensos.status_usuario,
                    Hipertensos.dt_afericao_pressao_mais_recente,
                    Hipertensos.prazo_proxima_afericao_pa,
                    Hipertensos.acs_nome_cadastro,
                    Hipertensos.equipe_ine_cadastro,
                    Hipertensos.equipe_nome_cadastro,
                    Hipertensos.dt_consulta_mais_recente,
                    Hipertensos.dt_registro_producao_mais_recente
                ).order_by(
                    Hipertensos.cidadao_nome
                ).all()
    except Exception as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )
