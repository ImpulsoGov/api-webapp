from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class EncaminhamentoApsEspecializada(Base):
    __tablename__ = "encaminhamentos_aps_especializada"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    conduta = Column(Text)
    quantidade_registrada = Column(Integer)
    quantidade_registrada_anterior = Column(Integer)
    dif_quantidade_registrada_anterior = Column(Integer)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
