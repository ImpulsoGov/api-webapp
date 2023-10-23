from sqlalchemy import Column, Date, Float, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID, VARCHAR 
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ProcedimentosPorHora(Base):
    __tablename__ = "caps_procedimentos_por_hora_resumo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    competencia = Column(Date)
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(VARCHAR)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    ocupacao = Column(Text)
    procedimentos_registrados_raas = Column(Numeric)
    procedimentos_registrados_raas_anterior = Column(Numeric)
    procedimentos_registrados_bpa = Column(Numeric)
    procedimentos_registrados_bpa_anterior = Column(Numeric)
    procedimentos_registrados_total = Column(Numeric)
    procedimentos_registrados_total_anterior = Column(Numeric)
    horas_disponibilidade_profissionais = Column(Numeric)
    horas_disponibilidade_profissionais_anterior = Column(Numeric)
    procedimentos_por_hora = Column(Numeric)
    procedimentos_por_hora_anterior = Column(Numeric)
    dif_procedimentos_registrados_raas_anterior = Column(Numeric)
    dif_procedimentos_registrados_bpa_anterior = Column(Numeric)
    dif_procedimentos_registrados_total_anterior = Column(Numeric)
    perc_dif_procedimentos_por_hora_anterior = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
