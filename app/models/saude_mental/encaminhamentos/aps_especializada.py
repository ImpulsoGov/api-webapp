from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class EncaminhamentoApsEspecializada(Base):
    __tablename__ = "encaminhamentos_aps_especializada"
    id = Column(Text, primary_key=True, nullable=True)
    unidade_geografica_id = Column(UUID(as_uuid=True), nullable=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15), nullable=True)
    competencia = Column(Date, nullable=True)
    periodo_id = Column(UUID(as_uuid=True), nullable=True)
    conduta = Column(Text, nullable=True)
    quantidade_registrada = Column(Integer, nullable=True)
    quantidade_registrada_anterior = Column(Integer, nullable=True)
    dif_quantidade_registrada_anterior = Column(Integer, nullable=True)
    atualizacao_data = Column(TIMESTAMP(timezone=True), nullable=True)
    periodo = Column(Text, nullable=True)
    nome_mes = Column(Text, nullable=True)
    periodo_ordem = Column(Float, nullable=True)
    __table_args__ = {"schema": "saude_mental"}
