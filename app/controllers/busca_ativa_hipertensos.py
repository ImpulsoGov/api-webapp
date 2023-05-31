from app.models import DB_PRODUCAO  
from app.models.hipertensos import Hipertensos
from app.models.score_cards_hipertensos import ScoreCardHipertensos
from sqlalchemy.sql import func
from cachetools import TTLCache
session = DB_PRODUCAO.session

def hipertensos_equipe(municipio_uf,equipe,faixa_etaria):
    print("================================================="+ municipio_uf,equipe,faixa_etaria)
    '''
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(equipe_ine_cadastro=equipe,municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        res= session.execute("SELECT identificacao_condicao_hipertensao,acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_afericao_pressao_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,municipio_uf,prazo_proxima_consulta,prazo_proxima_afericao_pa,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_afericao_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"+municipio_uf+"'"+" and equipe_ine_cadastro ='"+equipe+"'"+"and cidadao_faixa_etaria='"+faixa_etaria+"';").fetchall()
        print(res)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensos_coordenacao(municipio_uf,faixa_etaria):
    '''
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        return session.execute("SELECT identificacao_condicao_hipertensao,acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_afericao_pressao_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,municipio_uf,prazo_proxima_consulta,prazo_proxima_afericao_pa,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_afericao_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"+municipio_uf+"'"+"and cidadao_faixa_etaria='"+faixa_etaria+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensos_graficos(municipio_uf):
    try:
        return session.execute("SELECT identificacao_condicao_hipertensao,acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_afericao_pressao_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,municipio_uf,prazo_proxima_consulta,prazo_proxima_afericao_pa,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_afericao_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"+municipio_uf+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

cache_hipertensao_score_cards_aps = TTLCache(maxsize=38, ttl=24*60*60)
def hipertensao_score_cards_aps(municipio_id_sus):
    result = cache_hipertensao_score_cards_aps.get(municipio_id_sus)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                ScoreCardHipertensos).filter_by(
                municipio_id_sus=municipio_id_sus).with_entities(
                    func.sum(ScoreCardHipertensos.total_usuarios_com_hipertensao).label("total_usuarios_com_hipertensao"),
                    func.sum(ScoreCardHipertensos.total_com_consulta_afericao_pa_em_dia).label("total_com_consulta_afericao_pa_em_dia"),
                    func.sum(ScoreCardHipertensos.total_com_diagnostico_autorreferido).label("total_com_diagnostico_autorreferido"),
                    func.sum(ScoreCardHipertensos.total_com_diagnostico_clinico).label("total_com_diagnostico_clinico"),
                ).all()
            cache_hipertensao_score_cards_aps[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

cache_hipertensao_score_cards_equipe = TTLCache(maxsize=340, ttl=24*60*60)
def hipertensao_score_cards_equipe(municipio_id_sus,equipe):
    result = cache_hipertensao_score_cards_equipe.get(municipio_id_sus)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                    ScoreCardHipertensos
                    ).filter_by(
                    municipio_id_sus=municipio_id_sus,
                    equipe_ine=equipe
                    ).with_entities(
                    func.sum(ScoreCardHipertensos.total_usuarios_com_hipertensao).label("total_usuarios_com_hipertensao"),
                    func.sum(ScoreCardHipertensos.total_com_consulta_afericao_pa_em_dia).label("total_com_consulta_afericao_pa_em_dia"),
                    func.sum(ScoreCardHipertensos.total_com_diagnostico_autorreferido).label("total_com_diagnostico_autorreferido"),
                    func.sum(ScoreCardHipertensos.total_com_diagnostico_clinico).label("total_com_diagnostico_clinico"),
                ).all()
            cache_hipertensao_score_cards_equipe[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

cache_hipertensao_aps = TTLCache(maxsize=38, ttl=24*60*60)
def hipertensao_aps(municipio_id_sus):
    result = cache_hipertensao_aps.get(municipio_id_sus)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                Hipertensos).filter_by(
                municipio_id_sus=municipio_id_sus
                ).with_entities(
                    Hipertensos.cidadao_nome,
                    Hipertensos.cidadao_cpf,
                    Hipertensos.identificacao_condicao_hipertensao,
                    Hipertensos.dt_ultima_consulta,
                    Hipertensos.prazo_proxima_consulta,
                    Hipertensos.dt_afericao_pressao_mais_recente,
                    Hipertensos.prazo_proxima_afericao_pa,
                    Hipertensos.acs_nome_cadastro
                ).all()
            cache_hipertensao_aps[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensao_equipe(municipio_id_sus,equipe):
    try:
        return DB_PRODUCAO.session.query(
                Hipertensos
                ).filter_by(
                municipio_id_sus=municipio_id_sus,
                equipe_ine_cadastro=equipe
                ).with_entities(
                    Hipertensos.cidadao_nome,
                    Hipertensos.cidadao_cpf,
                    Hipertensos.identificacao_condicao_hipertensao,
                    Hipertensos.dt_ultima_consulta,
                    Hipertensos.prazo_proxima_consulta,
                    Hipertensos.dt_afericao_pressao_mais_recente,
                    Hipertensos.prazo_proxima_afericao_pa,
                    Hipertensos.acs_nome_cadastro
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    

cache_hipertensao_grafico = TTLCache(maxsize=38, ttl=24*60*60)
def hipertensao_grafico(municipio_id_sus):
    result = cache_hipertensao_grafico.get(municipio_id_sus)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                    ScoreCardHipertensos
                    ).filter_by(
                        municipio_id_sus=municipio_id_sus,
                    ).with_entities(
                        ScoreCardHipertensos.equipe_nome,
                        ScoreCardHipertensos.equipe_ine,
                        ScoreCardHipertensos.id_tipo_de_diagnostico,
                        ScoreCardHipertensos.id_faixa_etaria,
                        func.sum(ScoreCardHipertensos.total_usuarios_com_hipertensao).label("total_usuarios_com_hipertensao"),
                        func.sum(ScoreCardHipertensos.total_com_consulta_afericao_pa_em_dia).label("total_com_consulta_afericao_pa_em_dia"),
                        func.sum(ScoreCardHipertensos.total_com_diagnostico_autorreferido).label("total_com_diagnostico_autorreferido"),
                        func.sum(ScoreCardHipertensos.total_com_diagnostico_clinico).label("total_com_diagnostico_clinico"),
                    ).group_by(
                        ScoreCardHipertensos.equipe_nome,
                    ).all()
            cache_hipertensao_grafico[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
