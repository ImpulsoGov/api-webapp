from fastapi import HTTPException, status
from app.models import db
from app.models.impulso_previne_nominal.gestantes import Gestantes

session = db.session


def consulta_gestantes_equipe(municipio_id_sus, equipe):
    try:
        return (
            session.query(Gestantes)
            .filter_by(municipio_id_sus=municipio_id_sus, equipe_ine=equipe)
            .with_entities(
                Gestantes.chave_id_gestacao,
                Gestantes.municipio_id_sus,
                Gestantes.equipe_ine,
                Gestantes.equipe_nome,
                Gestantes.cidadao_nome,
                Gestantes.cidadao_cpf_dt_nascimento,
                Gestantes.gestacao_data_dpp,
                Gestantes.gestacao_quadrimestre,
                Gestantes.gestacao_idade_gestacional_atual,
                Gestantes.gestacao_idade_gestacional_primeiro_atendimento,
                Gestantes.consulta_prenatal_ultima_data,
                Gestantes.consultas_pre_natal_validas,
                Gestantes.id_atendimento_odontologico,
                Gestantes.id_exame_hiv_sifilis,
                Gestantes.id_status_usuario,
                Gestantes.id_registro_parto,
                Gestantes.id_registro_aborto,
                Gestantes.acs_nome,
                Gestantes.atualizacao_data,
                Gestantes.criacao_data,
                Gestantes.municipio_uf,
                Gestantes.dt_registro_producao_mais_recente,
            )
            .order_by(Gestantes.cidadao_nome)
            .all()
        )
    except Exception as error:
        session.rollback()
        print(error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def consulta_gestantes_coordenacao(municipio_id_sus):
    try:
        return (
            session.query(Gestantes)
            .filter_by(municipio_id_sus=municipio_id_sus)
            .with_entities(
                Gestantes.chave_id_gestacao,
                Gestantes.municipio_id_sus,
                Gestantes.equipe_ine,
                Gestantes.equipe_nome,
                Gestantes.cidadao_nome,
                Gestantes.cidadao_cpf_dt_nascimento,
                Gestantes.gestacao_data_dpp,
                Gestantes.gestacao_quadrimestre,
                Gestantes.gestacao_idade_gestacional_atual,
                Gestantes.gestacao_idade_gestacional_primeiro_atendimento,
                Gestantes.consulta_prenatal_ultima_data,
                Gestantes.consultas_pre_natal_validas,
                Gestantes.id_atendimento_odontologico,
                Gestantes.id_exame_hiv_sifilis,
                Gestantes.id_status_usuario,
                Gestantes.id_registro_parto,
                Gestantes.id_registro_aborto,
                Gestantes.acs_nome,
                Gestantes.atualizacao_data,
                Gestantes.criacao_data,
                Gestantes.municipio_uf,
                Gestantes.dt_registro_producao_mais_recente,
            )
            .order_by(Gestantes.cidadao_nome)
            .all()
        )
    except Exception as error:
        session.rollback()
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )
