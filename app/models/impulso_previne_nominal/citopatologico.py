from sqlalchemy import Column, Integer, String, DATE, BOOLEAN, DateTime, TIMESTAMP
from app.models import db

Base = db.Base_PRODUCAO_APLICACOES


class Citopatologico(Base):
    __tablename__ = "painel_citopatologico_lista_nominal"
    municipio_id_sus = Column(String, nullable=True)
    municipio_uf = Column(String, primary_key=True)
    paciente_nome = Column(String, nullable=True)
    cidadao_cpf_dt_nascimento = Column(String, nullable=True)
    vencimento_da_coleta = Column(String, nullable=True)
    prazo_proxima_coleta = Column(String, nullable=True)
    idade = Column(Integer, nullable=True)
    acs_nome = Column(String, nullable=True)
    estabelecimento_cnes = Column(String, nullable=True)
    estabelecimento_nome = Column(String, nullable=True)
    equipe_ine = Column(String, nullable=True)
    ine_master = Column(String, nullable=True)
    equipe_nome = Column(String, nullable=True)
    id_status_usuario = Column(Integer, nullable=True)
    id_faixa_etaria = Column(Integer, nullable=True)
    criacao_data = Column(TIMESTAMP, nullable=True)
    atualizacao_data = Column(TIMESTAMP, nullable=True)
    dt_registro_producao_mais_recente = Column(DATE, nullable=True)
    __table_args__ = {"schema": "impulso_previne_dados_nominais"}


# Base.metadata.create_all(db.engine)
