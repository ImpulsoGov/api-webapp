from app.models import DB_PRODUCAO  
from app.models.impulso_previne_nominal.citopatologico import Citopatologico
from sqlalchemy.sql import func
from cachetools import TTLCache
session = DB_PRODUCAO.session

cache_citopatologico_aps = TTLCache(maxsize=50, ttl=24*60*60)
def citopatologico_aps(municipio_uf):
    result = cache_citopatologico_aps.get(municipio_uf)
    try:
        if result is None:
            result = session.query(
                Citopatologico).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
                    Citopatologico.paciente_nome,
                    Citopatologico.cidadao_cpf_dt_nascimento,
                    Citopatologico.id_status_usuario,
                    Citopatologico.vencimento_da_coleta,
                    Citopatologico.prazo_proxima_coleta,
                    Citopatologico.idade,
                    Citopatologico.id_faixa_etaria,
                    Citopatologico.acs_nome,
                    Citopatologico.estabelecimento_cnes,
                    Citopatologico.estabelecimento_nome,
                    Citopatologico.equipe_ine,
                    Citopatologico.ine_master,
                    Citopatologico.equipe_nome,
                    Citopatologico.id_status_usuario,
                    Citopatologico.dt_registro_producao_mais_recente
                ).order_by(
                    Citopatologico.paciente_nome
                ).all()
            cache_citopatologico_aps[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def citopatologico_equipe(municipio_uf,equipe):
    try:
        return session.query(
                    Citopatologico
                ).filter_by(
                    municipio_uf=municipio_uf,
                    ine_master=equipe
                ).with_entities(
                    Citopatologico.paciente_nome,
                    Citopatologico.cidadao_cpf_dt_nascimento,
                    Citopatologico.id_status_usuario,
                    Citopatologico.vencimento_da_coleta,
                    Citopatologico.prazo_proxima_coleta,
                    Citopatologico.idade,
                    Citopatologico.id_faixa_etaria,
                    Citopatologico.acs_nome,
                    Citopatologico.estabelecimento_cnes,
                    Citopatologico.estabelecimento_nome,
                    Citopatologico.equipe_ine,
                    Citopatologico.ine_master,
                    Citopatologico.equipe_nome,
                    Citopatologico.id_status_usuario,
                    Citopatologico.dt_registro_producao_mais_recente
                ).order_by(
                    Citopatologico.paciente_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

