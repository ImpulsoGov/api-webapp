from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class ProcedimentosPorTipo(Base):
    __tablename__ = "caps_procedimentos_por_tipo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    procedimento = Column(Text)
    procedimentos_registrados_raas = Column(Integer)
    procedimentos_registrados_bpa = Column(Integer)
    procedimentos_registrados_total = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
