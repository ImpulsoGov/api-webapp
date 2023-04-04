from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base

class AbandonoPerfil(Base):
    __tablename__ = "caps_adesao_usuarios_perfil"
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
    usuario_sexo = Column(Text)
    quantidade_registrada = Column(Integer)
    estatus_adesao_mes = Column(Text)
    estatus_adesao_final = Column(Text)
    grupo_descricao_curta_cid10 = Column(Text)
    usuario_faixa_etaria_descricao = Column(Text)
    usuario_faixa_etaria_ordem = Column(Text)
    __table_args__ = {"schema": "saude_mental"}