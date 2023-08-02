from sqlalchemy import Column, Date, Float, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models import db
Base = db.Base_saude_mental


class ProcedimentosPorHora(Base):
    __tablename__ = "caps_procedimentos_por_hora_resumo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    ocupacao = Column(Text)
    procedimentos_registrados_raas = Column(Float)
    procedimentos_registrados_raas_anterior = Column(Float)
    procedimentos_registrados_bpa = Column(Float)
    procedimentos_registrados_bpa_anterior = Column(Float)
    procedimentos_registrados_total = Column(Float)
    procedimentos_registrados_total_anterior = Column(Float)
    horas_disponibilidade_profissionais = Column(Float)
    horas_disponibilidade_profissionais_anterior = Column(Float)
    procedimentos_por_hora = Column(Float)
    procedimentos_por_hora_anterior = Column(Float)
    dif_procedimentos_registrados_raas_anterior = Column(Float)
    dif_procedimentos_registrados_bpa_anterior = Column(Float)
    dif_procedimentos_registrados_total_anterior = Column(Float)
    perc_dif_procedimentos_por_hora_anterior = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
