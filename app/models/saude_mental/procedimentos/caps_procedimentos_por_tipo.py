from sqlalchemy import Column, Date, Float, Integer, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ProcedimentosPorTipo(Base):
    __tablename__ = "caps_procedimentos_por_tipo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    competencia = Column(Date)
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(VARCHAR)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    procedimento = Column(Text)
    procedimentos_registrados_raas = Column(Numeric)
    procedimentos_registrados_bpa = Column(Numeric)
    procedimentos_registrados_total = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
