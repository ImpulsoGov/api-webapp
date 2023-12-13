from sqlalchemy import DATE, Column, TIMESTAMP, String
from app.models import DB_PRODUCAO

Base = DB_PRODUCAO.Base


class CadastrosDuplicadosGestantes(Base):
    __tablename__ = "painel_cadastros_gestantes_duplicadas"
    municipio_id_sus = Column(String, nullable=True)
    municipio_uf = Column(String, nullable=True)
    gestante_nome = Column(String, nullable=True)
    gestante_data_de_nascimento = Column(DATE, nullable=True)
    gestante_documento_cpf = Column(String, nullable=True)
    gestante_documento_cns = Column(String, primary_key=True, nullable=True)
    periodo_data_transmissao = Column(DATE, nullable=True)
    gestante_dum = Column(DATE, nullable=True)
    gestante_dpp = Column(DATE, nullable=True)
    duplicacao_motivo = Column(String, nullable=True)
    atualizacao_data = Column(TIMESTAMP, nullable=True)
    equipe_ine = Column(String, nullable=True)
    equipe_nome = Column(String, nullable=True)
    estabelecimento_cnes = Column(String, nullable=True)
    estabelecimento_nome = Column(String, nullable=True)
    acs_nome = Column(String, nullable=True)
    __table_args__ = {"schema": "impulso_previne_dados_nominais"}


# Base.metadata.create_all(db.engine)
