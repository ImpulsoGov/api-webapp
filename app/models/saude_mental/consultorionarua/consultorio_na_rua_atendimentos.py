
from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class ConsultorionaruaAtendimentos(Base):
    __tablename__ = "consultorio_na_rua_atendimentos"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    quantidade_registrada = Column(Integer)
    quantidade_registrada_anterior = Column(Integer)
    dif_quantidade_registrada_anterior = Column(Integer)
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    tipo_producao = Column(Text)
    competencia = Column(Text)
    nome_mes = Column(Text)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    __table_args__ = {"schema": "saude_mental"}