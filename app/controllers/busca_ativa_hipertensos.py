from app.models import DB_PRODUCAO
from app.models.hipertensos import Hipertensos

session = DB_PRODUCAO.session


def hipertensos_equipe(municipio_uf, equipe, faixa_etaria):
    """
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(equipe_ine_cadastro=equipe,municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    """
    try:
        return session.execute(
            "SELECT identificacao_condicao_hipertensao,acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_afericao_pressao_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,municipio_uf,prazo_proxima_consulta,prazo_proxima_afericao_pa,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_afericao_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"
            + municipio_uf
            + "'"
            + " and equipe_ine_cadastro ='"
            + equipe
            + "'"
            + "and cidadao_faixa_etaria='"
            + faixa_etaria
            + "';"
        ).fetchall()
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error


def hipertensos_coordenacao(municipio_uf, faixa_etaria):
    """
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
    """
    try:
        return session.execute(
            "SELECT identificacao_condicao_hipertensao,acs_nome_cadastro,apenas_autorreferida,cidadao_cpf_dt_nascimento,cidadao_nome,consulta_e_afericao_em_dia,criacao_data,diagnostico_clinico,dt_consulta_mais_recente,dt_afericao_pressao_mais_recente,equipe_ine_cadastro,equipe_nome_atendimento,equipe_nome_cadastro,municipio_uf,prazo_proxima_consulta,prazo_proxima_afericao_pa,quadrimestre_atual,realizou_consulta_ultimos_6_meses,realizou_afericao_ultimos_6_meses,se_faleceu,se_mudou,status_em_dia,status_usuario,cidadao_faixa_etaria FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_hipertensos where municipio_uf='"
            + municipio_uf
            + "'"
            + "and cidadao_faixa_etaria='"
            + faixa_etaria
            + "';"
        ).fetchall()
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error
