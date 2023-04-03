from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class UsuariosPerfilEstabelecimento(Base):
    __tablename__ = "caps_usuarios_ativos_por_estabelecimento_resumo"
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
    dif_ativos_mes_anterior = Column(Integer)
    dif_ativos_3meses_anterior = Column(Integer)
    dif_tornandose_inativos_anterior = Column(Integer)
    sexo_predominante = Column(Text)
    usuarios_idade_media = Column(Float)
    ativos_mes = Column(Integer)
    ativos_3meses = Column(Integer)
    tornandose_inativos = Column(Integer)
    ativos_mes_anterior = Column(Integer)
    ativos_3meses_anterior = Column(Integer)
    tornandose_inativos_anterior = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}