from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base

class ProcedimentoPorUsuarioTempoServiço(Base):
    __tablename__ = "caps_procedimentos_por_usuario_por_tempo_servico"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    maior_taxa = Column(Float)
    tempo_servico_maior_taxa = Column(Text)
    __table_args__ = {"schema": "saude_mental"}
