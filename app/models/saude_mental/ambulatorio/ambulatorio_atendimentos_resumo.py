from sqlalchemy import Column, Numeric, Text, Date, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base

class AmbulatorioAtendimentoResumo(Base):
    __tablename__ = "ambulatorio_atendimentos_resumo"
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
    ocupacao = Column(Text)
    procedimentos_realizados = Column(Numeric)
    procedimentos_realizados_anterior = Column(Numeric)
    procedimentos_por_hora = Column(Numeric)
    procedimentos_por_hora_anterior = Column(Numeric)
    dif_procedimentos_por_hora_anterior = Column(Numeric)
    dif_procedimentos_realizados_anterior = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
