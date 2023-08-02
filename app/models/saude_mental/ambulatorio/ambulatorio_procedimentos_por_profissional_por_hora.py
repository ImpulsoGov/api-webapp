from sqlalchemy import TIMESTAMP, Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models import db
Base = db.Base_saude_mental


class AmbulatorioProcedimentosPorProfissional(Base):
    __tablename__ = "ambulatorio_procedimentos_por_profissional_por_hora"
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
    profissional_nome = Column(Text)
    procedimentos_realizados = Column(Numeric)
    procedimentos_por_hora = Column(Numeric)
    disponibilidade_mensal = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
