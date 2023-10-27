from app.models import DB_PRODUCAO
from app.models.impulso_previne_nominal.busca_ativa_aps import GestantesCoordenacao
from app.models.impulso_previne_nominal.busca_ativa_equipe import Gestantes
from app.models.impulso_previne_nominal.cadastros_duplicados_gestantes import CadastrosDuplicadosGestantes

session = DB_PRODUCAO.session


def consulta_gestantes_equipe(municipio_uf, equipe):
    try:
        return session.query(
                    Gestantes
                ).filter_by(
                    municipio_uf=municipio_uf,
                    equipe_ine=equipe
                ).with_entities(
                    Gestantes.municipio_id_sus,
                    Gestantes.municipio_uf,
                    Gestantes.estabelecimento_cnes,
                    Gestantes.estabelecimento_nome,
                    Gestantes.equipe_ine,
                    Gestantes.equipe_nome,
                    Gestantes.acs_nome,
                    Gestantes.acs_data_ultima_visita,
                    Gestantes.gestante_documento_cpf,
                    Gestantes.gestante_documento_cns,
                    Gestantes.gestante_nome,
                    Gestantes.gestante_data_de_nascimento,
                    Gestantes.gestante_telefone,
                    Gestantes.gestante_endereco,
                    Gestantes.gestante_dum,
                    Gestantes.gestante_idade_gestacional_atual,
                    Gestantes.gestante_idade_gestacional_primeiro_atendimento,
                    Gestantes.gestante_dpp,
                    Gestantes.gestante_quadrimestre,
                    Gestantes.gestante_consulta_prenatal_data_limite,
                    Gestantes.gestacao_dpp_dias_para,
                    Gestantes.gestante_consulta_prenatal_total,
                    Gestantes.gestantes_com_6_consultas,
                    Gestantes.gestante_consulta_prenatal_ultima_data,
                    Gestantes.gestante_consulta_prenatal_ultima_dias_desde,
                    Gestantes.atendimento_odontologico_realizado,
                    Gestantes.atendimento_odontologico_realizado_identificacao,
                    Gestantes.exame_hiv_realizado,
                    Gestantes.exame_sifilis_realizado,
                    Gestantes.exame_sifilis_hiv_realizado,
                    Gestantes.exame_sifilis_hiv_realizado_identificacao,
                    Gestantes.possui_registro_aborto,
                    Gestantes.possui_registro_parto,
                    Gestantes.criacao_data
                ).order_by(
                    Gestantes.gestante_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def consulta_gestantes_coordenacao(municipio_uf):
    try:
        return session.query(
                    Gestantes
                ).filter_by(
                    municipio_uf=municipio_uf
                ).with_entities(
                    Gestantes.municipio_id_sus,
                    Gestantes.municipio_uf,
                    Gestantes.estabelecimento_cnes,
                    Gestantes.estabelecimento_nome,
                    Gestantes.equipe_ine,
                    Gestantes.equipe_nome,
                    Gestantes.acs_nome,
                    Gestantes.acs_data_ultima_visita,
                    Gestantes.gestante_documento_cpf,
                    Gestantes.gestante_documento_cns,
                    Gestantes.gestante_nome,
                    Gestantes.gestante_data_de_nascimento,
                    Gestantes.gestante_telefone,
                    Gestantes.gestante_endereco,
                    Gestantes.gestante_dum,
                    Gestantes.gestante_idade_gestacional_atual,
                    Gestantes.gestante_idade_gestacional_primeiro_atendimento,
                    Gestantes.gestante_dpp,
                    Gestantes.gestante_quadrimestre,
                    Gestantes.gestante_consulta_prenatal_data_limite,
                    Gestantes.gestacao_dpp_dias_para,
                    Gestantes.gestante_consulta_prenatal_total,
                    Gestantes.gestantes_com_6_consultas,
                    Gestantes.gestante_consulta_prenatal_ultima_data,
                    Gestantes.gestante_consulta_prenatal_ultima_dias_desde,
                    Gestantes.atendimento_odontologico_realizado,
                    Gestantes.atendimento_odontologico_realizado_identificacao,
                    Gestantes.exame_hiv_realizado,
                    Gestantes.exame_sifilis_realizado,
                    Gestantes.exame_sifilis_hiv_realizado,
                    Gestantes.exame_sifilis_hiv_realizado_identificacao,
                    Gestantes.possui_registro_aborto,
                    Gestantes.possui_registro_parto,
                    Gestantes.criacao_data
                ).order_by(
                    Gestantes.gestante_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def cadastros_duplicados_gestantes_por_equipe(municipio_uf, equipe):
    try:
        return session.query(
                    CadastrosDuplicadosGestantes
                ).filter_by(
                    municipio_uf=municipio_uf,
                    equipe_ine=equipe
                ).with_entities(
                    CadastrosDuplicadosGestantes.municipio_id_sus,
                    CadastrosDuplicadosGestantes.municipio_uf,
                    CadastrosDuplicadosGestantes.gestante_nome,
                    CadastrosDuplicadosGestantes.gestante_data_de_nascimento,
                    CadastrosDuplicadosGestantes.gestante_documento_cpf,
                    CadastrosDuplicadosGestantes.gestante_documento_cns,
                    CadastrosDuplicadosGestantes.periodo_data_transmissao,
                    CadastrosDuplicadosGestantes.gestante_dum,
                    CadastrosDuplicadosGestantes.gestante_dpp,
                    CadastrosDuplicadosGestantes.duplicacao_motivo,
                    CadastrosDuplicadosGestantes.atualizacao_data,
                    CadastrosDuplicadosGestantes.equipe_ine,
                    CadastrosDuplicadosGestantes.equipe_nome,
                    CadastrosDuplicadosGestantes.estabelecimento_cnes,
                    CadastrosDuplicadosGestantes.estabelecimento_nome,
                    CadastrosDuplicadosGestantes.acs_nome,
                ).order_by(
                    CadastrosDuplicadosGestantes.gestante_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def cadastros_duplicados_gestantes_por_municipio(municipio_uf):
    try:
        return session.query(
                    CadastrosDuplicadosGestantes
                ).filter_by(
                    municipio_uf=municipio_uf,
                ).with_entities(
                    CadastrosDuplicadosGestantes.municipio_id_sus,
                    CadastrosDuplicadosGestantes.municipio_uf,
                    CadastrosDuplicadosGestantes.gestante_nome,
                    CadastrosDuplicadosGestantes.gestante_data_de_nascimento,
                    CadastrosDuplicadosGestantes.gestante_documento_cpf,
                    CadastrosDuplicadosGestantes.gestante_documento_cns,
                    CadastrosDuplicadosGestantes.periodo_data_transmissao,
                    CadastrosDuplicadosGestantes.gestante_dum,
                    CadastrosDuplicadosGestantes.gestante_dpp,
                    CadastrosDuplicadosGestantes.duplicacao_motivo,
                    CadastrosDuplicadosGestantes.atualizacao_data,
                    CadastrosDuplicadosGestantes.equipe_ine,
                    CadastrosDuplicadosGestantes.equipe_nome,
                    CadastrosDuplicadosGestantes.estabelecimento_cnes,
                    CadastrosDuplicadosGestantes.estabelecimento_nome,
                    CadastrosDuplicadosGestantes.acs_nome,
                ).order_by(
                    CadastrosDuplicadosGestantes.gestante_nome
                ).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error
