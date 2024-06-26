from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import VARCHAR, UUID
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class AtendimentosIndividuaisPorCaps(Base):
    __tablename__ = "caps_atendimentos_individuais_por_caps"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    perc_apenas_atendimentos_individuais = Column(Numeric)
    perc_apenas_atendimentos_individuais_anterior = Column(Numeric)
    dif_perc_apenas_atendimentos_individuais = Column(Numeric)
    maior_taxa = Column(Numeric)
    estabelecimento = Column(Text)
    maior_taxa_estabelecimento_linha_perfil = Column(Text)
    maior_taxa_estabelecimento_linha_idade = Column(Text)
    maior_taxa_estabelecimento = Column(Text)
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
