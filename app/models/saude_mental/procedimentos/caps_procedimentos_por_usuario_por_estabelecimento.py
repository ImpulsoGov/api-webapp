from sqlalchemy import Column, Date, Float, Integer, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ProcedimentoPorUsuarioEstabelecimento(Base):
    __tablename__ = "caps_procedimentos_por_usuario_por_estabelecimento"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    competencia = Column(Date)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    procedimentos_por_usuario = Column(Numeric)
    maior_taxa = Column(Float)
    dif_procedimentos_por_usuario_anterior_perc = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
