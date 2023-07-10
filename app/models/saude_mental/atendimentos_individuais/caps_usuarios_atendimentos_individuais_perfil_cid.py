from sqlalchemy import VARCHAR, Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, TIMESTAMP, UUID

from app.models import db

Base = db.Base


class AtendimentoIndividualPorCID(Base):
    __tablename__ = "caps_usuarios_atendimentos_individuais_perfil_cid"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuario_condicao_saude = Column(Text)
    usuarios_apenas_atendimento_individual = Column(Numeric)
    usuarios_frequentantes = Column(Numeric)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    estabelecimento = Column(VARCHAR)
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
