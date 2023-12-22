from app.models import db
from app.models.busca_ativa_vacinacao import Vacinacao
from cachetools import TTLCache

session = db.session

cache_vacinacao_aps = TTLCache(maxsize=38, ttl=24 * 60 * 60)


def vacinacao_municipio(municipio_id_sus):
    result = cache_vacinacao_aps.get(municipio_id_sus)
    try:
        if result is None:
            result = (
                session.query(Vacinacao)
                .filter_by(municipio_id_sus=municipio_id_sus)
                .with_entities(
                    Vacinacao.municipio_id_sus,
                    Vacinacao.municipio_uf,
                    Vacinacao.cidadao_nome,
                    Vacinacao.cidadao_nome_responsavel,
                    Vacinacao.cidadao_cpf_dt_nascimento,
                    Vacinacao.cidadao_idade_meses,
                    Vacinacao.quadrimestre_completa_1_ano,
                    Vacinacao.id_status_quadrimestre,
                    Vacinacao.data_ou_prazo_1dose_polio,
                    Vacinacao.data_ou_prazo_2dose_polio,
                    Vacinacao.data_ou_prazo_3dose_polio,
                    Vacinacao.id_status_polio,
                    Vacinacao.id_cor_1dose_polio,
                    Vacinacao.id_cor_2dose_polio,
                    Vacinacao.id_cor_3dose_polio,
                    Vacinacao.data_ou_prazo_1dose_penta,
                    Vacinacao.data_ou_prazo_2dose_penta,
                    Vacinacao.data_ou_prazo_3dose_penta,
                    Vacinacao.id_status_penta,
                    Vacinacao.id_cor_1dose_penta,
                    Vacinacao.id_cor_2dose_penta,
                    Vacinacao.id_cor_3dose_penta,
                    Vacinacao.acs_nome,
                    Vacinacao.equipe_ine,
                    Vacinacao.equipe_nome,
                    Vacinacao.criacao_data,
                    Vacinacao.atualizacao_data,
                    Vacinacao.dt_registro_producao_mais_recente,
                )
                .order_by(Vacinacao.cidadao_nome)
                .all()
            )
            cache_vacinacao_aps[municipio_id_sus] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error


def vacinacao_equipe(municipio_id_sus, equipe):
    try:
        return (
            session.query(Vacinacao)
            .filter_by(municipio_id_sus=municipio_id_sus, equipe_ine=equipe)
            .with_entities(
                Vacinacao.municipio_id_sus,
                Vacinacao.municipio_uf,
                Vacinacao.cidadao_nome,
                Vacinacao.cidadao_nome_responsavel,
                Vacinacao.cidadao_cpf_dt_nascimento,
                Vacinacao.cidadao_idade_meses,
                Vacinacao.quadrimestre_completa_1_ano,
                Vacinacao.id_status_quadrimestre,
                Vacinacao.data_ou_prazo_1dose_polio,
                Vacinacao.data_ou_prazo_2dose_polio,
                Vacinacao.data_ou_prazo_3dose_polio,
                Vacinacao.id_status_polio,
                Vacinacao.id_cor_1dose_polio,
                Vacinacao.id_cor_2dose_polio,
                Vacinacao.id_cor_3dose_polio,
                Vacinacao.data_ou_prazo_1dose_penta,
                Vacinacao.data_ou_prazo_2dose_penta,
                Vacinacao.data_ou_prazo_3dose_penta,
                Vacinacao.id_status_penta,
                Vacinacao.id_cor_1dose_penta,
                Vacinacao.id_cor_2dose_penta,
                Vacinacao.id_cor_3dose_penta,
                Vacinacao.acs_nome,
                Vacinacao.equipe_ine,
                Vacinacao.equipe_nome,
                Vacinacao.criacao_data,
                Vacinacao.atualizacao_data,
                Vacinacao.dt_registro_producao_mais_recente,
            )
            .order_by(Vacinacao.cidadao_nome)
            .all()
        )
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error
