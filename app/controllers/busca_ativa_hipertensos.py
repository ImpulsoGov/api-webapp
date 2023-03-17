from app.models import DB_PRODUCAO  
from app.models.hipertensos import Hipertensos

session = DB_PRODUCAO.session

def hipertensos_equipe(municipio_uf,equipe):
    '''
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(equipe_ine_cadastro=equipe,municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        res_tupla = session.execute("SELECT    dt_consulta_mais_recente,  cidadao_cpf_dt_nascimento,  estabelecimento_cnes_cadastro,  acs_nome_visita,  se_faleceu,  municipio_id_sus,  prazo_proxima_afericao_pa,  cidadao_cns,  estabelecimento_nome_atendimento,  possui_hipertensao_autorreferida,  se_mudou,  municipio_uf,  prazo_proxima_consulta,  cidadao_nome,  estabelecimento_nome_cadastro,  possui_hipertensao_diagnosticada,  criacao_data,  quadrimestre_atual,  consulta_e_afericao_em_dia,  cidadao_nome_social,  equipe_ine_atendimento,  apenas_autorreferida,  atualizacao_data,  realizou_afericao_ultimos_6_meses,  status_em_dia,  cidadao_sexo,  equipe_ine_cadastro,  diagnostico_clinico,  dt_afericao_pressao_mais_recente,  status_usuario,  dt_nascimento,  equipe_nome_atendimento,  data_ultimo_cadastro,  realizou_consulta_ultimos_6_meses,  identificacao_condicao_hipertensao,  estabelecimento_cnes_atendimento,  equipe_nome_cadastro,  dt_ultima_consulta,  cidadao_cpf,  acs_nome_cadastro FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"+municipio_uf+"'"+" and equipe_ine_cadastro ='"+equipe+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensos_coordenacao(municipio_uf):
    '''
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    '''
    try:
        res_tupla = session.execute("SELECT    dt_consulta_mais_recente,  cidadao_cpf_dt_nascimento,  estabelecimento_cnes_cadastro,  acs_nome_visita,  se_faleceu,  municipio_id_sus,  prazo_proxima_afericao_pa,  cidadao_cns,  estabelecimento_nome_atendimento,  possui_hipertensao_autorreferida,  se_mudou,  municipio_uf,  prazo_proxima_consulta,  cidadao_nome,  estabelecimento_nome_cadastro,  possui_hipertensao_diagnosticada,  criacao_data,  quadrimestre_atual,  consulta_e_afericao_em_dia,  cidadao_nome_social,  equipe_ine_atendimento,  apenas_autorreferida,  atualizacao_data,  realizou_afericao_ultimos_6_meses,  status_em_dia,  cidadao_sexo,  equipe_ine_cadastro,  diagnostico_clinico,  dt_afericao_pressao_mais_recente,  status_usuario,  dt_nascimento,  equipe_nome_atendimento,  data_ultimo_cadastro,  realizou_consulta_ultimos_6_meses,  identificacao_condicao_hipertensao,  estabelecimento_cnes_atendimento,  equipe_nome_cadastro,  dt_ultima_consulta,  cidadao_cpf,  acs_nome_cadastro FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"+municipio_uf+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

