from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

from app.models import db
Base = db.Base_saude_mental


class AbandonoMensal(Base):
    __tablename__ = "caps_adesao_evasao_mensal"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuarios_recentes_evadiram = Column(Integer)
    usuarios_recentes_total = Column(Integer)
    usuarios_evasao_perc = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
