from sqlalchemy import DATE, Column, Integer, String, TIMESTAMP
from app.models import db

Base = db.Base_PRODUCAO_APLICACOES


class Gestantes(Base):
    __tablename__ = "painel_gestantes_lista_nominal"
    chave_id_gestacao = Column(String, primary_key=True, nullable=True)
    municipio_id_sus = Column(String, nullable=True)
    equipe_ine = Column(String, nullable=True)
    equipe_nome = Column(String, nullable=True)
    cidadao_nome = Column(String, nullable=True)
    cidadao_cpf_dt_nascimento = Column(String, nullable=True)
    gestacao_data_dpp = Column(String, nullable=True)
    gestacao_quadrimestre = Column(String, nullable=True)
    gestacao_idade_gestacional_atual = Column(Integer, nullable=True)
    gestacao_idade_gestacional_primeiro_atendimento = Column(Integer, nullable=True)
    consulta_prenatal_ultima_data = Column(DATE, nullable=True)
    consultas_pre_natal_validas = Column(Integer, nullable=True)
    id_atendimento_odontologico = Column(Integer, nullable=True)
    id_exame_hiv_sifilis = Column(Integer, nullable=True)
    id_status_usuario = Column(Integer, nullable=True)
    id_registro_parto = Column(Integer, nullable=True)
    id_registro_aborto = Column(Integer, nullable=True)
    acs_nome = Column(String, nullable=True)
    atualizacao_data = Column(TIMESTAMP, nullable=True)
    criacao_data = Column(DATE, nullable=True)
    municipio_uf = Column(String, nullable=True)
    dt_registro_producao_mais_recente = Column(DATE, nullable=True)
    __table_args__ = {"schema": "impulso_previne_dados_nominais"}


# Base.metadata.create_all(db.engine)
