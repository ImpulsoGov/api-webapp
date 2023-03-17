from app.models import DB_PRODUCAO  
from app.models.diabeticos import Diabeticos

session = DB_PRODUCAO.session

def diabeticos_equipe(municipio_uf,equipe):
    '''
    try:
        return DB_PRODUCAO.session.query(Diabeticos).filter_by(equipe_ine_cadastro=equipe).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return erro
    '''
    try:
        return session.execute("SELECT  municipio_uf,consulta_e_afericao_em_dia,  cidadao_nome,  equipe_ine_atendimento,  possui_diabetes_diagnosticada,  atualizacao_data,  quadrimestre_atual,  status_em_dia,  cidadao_nome_social,  equipe_ine_cadastro,  apenas_autorreferida,  realizou_solicitacao_hemoglobina_ultimos_6_meses,  status_usuario,  cidadao_sexo,  equipe_nome_atendimento,  diagnostico_clinico,  dt_solicitacao_hemoglobina_glicada_mais_recente,  identificacao_condicao_diabetes,  dt_nascimento,  equipe_nome_cadastro,  data_ultimo_cadastro,  realizou_consulta_ultimos_6_meses,  cidadao_cpf,  estabelecimento_cnes_atendimento,  acs_nome_cadastro,  dt_ultima_consulta,  dt_consulta_mais_recente,  cidadao_cpf_dt_nascimento,  estabelecimento_cnes_cadastro,  acs_nome_visita,  se_faleceu,  municipio_id_sus,  prazo_proxima_solicitacao_hemoglobina,  cidadao_cns,  estabelecimento_nome_atendimento,  possui_diabetes_autorreferida,  se_mudou,  prazo_proxima_consulta,  estabelecimento_nome_cadastro,  criacao_data FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_diabeticos where municipio_uf='"+municipio_uf+"'"+" and equipe_ine_cadastro ='"+equipe+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def diabeticos_coordenacao(municipio_uf):
    '''
    try:
        return DB_PRODUCAO.session.query(Diabeticos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        return session.execute("SELECT  municipio_uf,consulta_e_afericao_em_dia,  cidadao_nome,  equipe_ine_atendimento,  possui_diabetes_diagnosticada,  atualizacao_data,  quadrimestre_atual,  status_em_dia,  cidadao_nome_social,  equipe_ine_cadastro,  apenas_autorreferida,  realizou_solicitacao_hemoglobina_ultimos_6_meses,  status_usuario,  cidadao_sexo,  equipe_nome_atendimento,  diagnostico_clinico,  dt_solicitacao_hemoglobina_glicada_mais_recente,  identificacao_condicao_diabetes,  dt_nascimento,  equipe_nome_cadastro,  data_ultimo_cadastro,  realizou_consulta_ultimos_6_meses,  cidadao_cpf,  estabelecimento_cnes_atendimento,  acs_nome_cadastro,  dt_ultima_consulta,  dt_consulta_mais_recente,  cidadao_cpf_dt_nascimento,  estabelecimento_cnes_cadastro,  acs_nome_visita,  se_faleceu,  municipio_id_sus,  prazo_proxima_solicitacao_hemoglobina,  cidadao_cns,  estabelecimento_nome_atendimento,  possui_diabetes_autorreferida,  se_mudou,  prazo_proxima_consulta,  estabelecimento_nome_cadastro,  criacao_data FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_diabeticos where municipio_uf='"+municipio_uf+"';").fetchall()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


