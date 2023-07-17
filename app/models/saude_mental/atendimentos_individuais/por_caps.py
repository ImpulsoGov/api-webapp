from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class AtendimentosIndividuaisPorCaps(Base):
    __tablename__ = "caps_atendimentos_individuais_por_caps"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
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
    __table_args__ = {"schema": "saude_mental"}
