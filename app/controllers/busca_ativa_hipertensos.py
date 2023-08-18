from app.models import DB_PRODUCAO  
from app.models.hipertensos import Hipertensos
from cachetools import TTLCache
session = DB_PRODUCAO.session

cache_hipertensao_aps = TTLCache(maxsize=38, ttl=24*60*60)
def hipertensao_aps(municipio_uf):
    result = cache_hipertensao_aps.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                Hipertensos).filter_by(
                municipio_uf=municipio_uf
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
                ).order_by(
                    Hipertensos.cidadao_nome
                ).all()
            cache_hipertensao_aps[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensao_equipe(municipio_uf,equipe):
    try:
        return DB_PRODUCAO.session.query(
                Hipertensos
                ).filter_by(
                municipio_uf=municipio_uf,
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
                    Hipertensos.equipe_nome_cadastro
                ).order_by(
                    Hipertensos.cidadao_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
