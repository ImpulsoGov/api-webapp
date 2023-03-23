from app.models import DB_PRODUCAO  
from app.models.diabeticos import Diabeticos

session = DB_PRODUCAO.session

def diabeticos_equipe(municipio_uf,equipe,faixa_etaria):
    '''
    try:
        return DB_PRODUCAO.session.query(Diabeticos).filter_by(equipe_ine_cadastro=equipe).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return erro
    '''
    try:
        return session.execute("SELECT  acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_solicitacao_hemoglobina_glicada_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,identificacao_condicao_diabetes,municipio_uf,prazo_proxima_consulta,prazo_proxima_solicitacao_hemoglobina,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_solicitacao_hemoglobina_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_diabeticos where municipio_uf='"+municipio_uf+"'"+" and equipe_ine_cadastro ='"+equipe+"'"+"and cidadao_faixa_etaria='"+faixa_etaria+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def diabeticos_coordenacao(municipio_uf,faixa_etaria):
    '''
    try:
        return DB_PRODUCAO.session.query(Diabeticos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        return session.execute("SELECT  acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_solicitacao_hemoglobina_glicada_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,identificacao_condicao_diabetes,municipio_uf,prazo_proxima_consulta,prazo_proxima_solicitacao_hemoglobina,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_solicitacao_hemoglobina_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_diabeticos where municipio_uf='"+municipio_uf+"'"+"and cidadao_faixa_etaria='"+faixa_etaria+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def diabeticos_graficos(municipio_uf):
    try:
        return session.execute("SELECT  acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_solicitacao_hemoglobina_glicada_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,identificacao_condicao_diabetes,municipio_uf,prazo_proxima_consulta,prazo_proxima_solicitacao_hemoglobina,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_solicitacao_hemoglobina_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_diabeticos where municipio_uf='"+municipio_uf+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


