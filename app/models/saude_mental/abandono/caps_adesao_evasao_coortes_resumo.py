from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class AbandonoCoortes(Base):
    __tablename__ = "_caps_adesao_evasao_coortes_resumo_1"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    a_partir_do_ano = Column(Text)
    a_partir_do_mes = Column(Text)
    ate_mes = Column(Text)
    ate_ano = Column(Text)
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    predominio_sexo = Column(Text)
    maior_taxa_estabelecimento_linha_perfil = Column(Text)
    maior_taxa_estabelecimento_linha_idade = Column(Text)
    maior_taxa_estabelecimento = Column(Text)
    predominio_faixa_etaria = Column(Text)
    predominio_condicao_grupo_descricao_curta_cid10 = Column(Text)
    maior_taxa_perc = Column(Float)
    maior_taxa_usuarios_nao_aderiram = Column(Integer)
    maior_taxa_usuarios_total = Column(Integer)
    usuarios_coorte_nao_aderiram_perc = Column(Float)
    usuarios_coorte_nao_aderiram = Column(Integer)
    usuarios_coorte_total = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
