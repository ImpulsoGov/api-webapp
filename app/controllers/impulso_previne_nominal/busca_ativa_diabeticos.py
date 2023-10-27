from app.models import DB_PRODUCAO
from app.models.impulso_previne_nominal.diabeticos import Diabeticos
from cachetools import TTLCache

session = DB_PRODUCAO.session

def diabeticos_equipe(municipio_uf,equipe):
    try:
        return session.query(
                Diabeticos
                ).filter_by(
                municipio_uf=municipio_uf,
                equipe_ine_cadastro=equipe
                ).with_entities(
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
                    Diabeticos.dt_registro_producao_mais_recente
                ).order_by(
                    Diabeticos.cidadao_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


cache_hipertensao_aps = TTLCache(maxsize=38, ttl=24*60*60)
def diabetes_aps(municipio_uf):
    result = cache_hipertensao_aps.get(municipio_uf)
    try:
        if result is None:
            result = session.query(
                Diabeticos).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
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
                    Diabeticos.dt_registro_producao_mais_recente
                ).order_by(
                    Diabeticos.cidadao_nome
                ).all()
            cache_hipertensao_aps[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

