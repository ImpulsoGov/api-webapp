from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base

class ProcedimentoPorUsuarioEstabelecimento(Base):
    __tablename__ = "caps_procedimentos_por_usuario_por_estabelecimento"
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
    procedimentos_exceto_acolhimento = Column(Float)
    procedimentos_exceto_acolhimento_anterior = Column(Float)
    ativos_mes = Column(Float)
    ativos_mes_anterior = Column(Float)
    procedimentos_por_usuario = Column(Float)
    procedimentos_por_usuario_anterior = Column(Float)
    maior_taxa = Column(Float)
    maior_taxa_anterior = Column(Float)
    dif_procedimentos_por_usuario_anterior_perc = Column(Float)
    __table_args__ = {"schema": "saude_mental"}