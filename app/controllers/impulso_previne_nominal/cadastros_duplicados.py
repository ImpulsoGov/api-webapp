from app.models import db
from app.models.impulso_previne_nominal.cadastros_duplicados_gestantes import (
    CadastrosDuplicadosGestantes,
)

session = db.session


def cadastros_duplicados_gestantes_por_equipe(municipio_uf, equipe):
    try:
        return (
            session.query(CadastrosDuplicadosGestantes)
            .filter_by(municipio_uf=municipio_uf, equipe_ine=equipe)
            .with_entities(
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
            )
            .order_by(CadastrosDuplicadosGestantes.gestante_nome)
            .all()
        )
    except Exception as error:
        print({"erros": [error]})
        return error


def cadastros_duplicados_gestantes_por_municipio(municipio_uf):
    try:
        return (
            session.query(CadastrosDuplicadosGestantes)
            .filter_by(
                municipio_uf=municipio_uf,
            )
            .with_entities(
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
            )
            .order_by(CadastrosDuplicadosGestantes.gestante_nome)
            .all()
        )
    except Exception as error:
        print({"erros": [error]})
        return error
