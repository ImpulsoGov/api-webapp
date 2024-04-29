from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental

class EstabelecimentosAusentesPorPeriodo(Base):
    __tablename__ = "configuracoes_estabelecimentos_ausentes_por_periodos"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    estabelecimento = Column(Text)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    tabela_referencia = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
