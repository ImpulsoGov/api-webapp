from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, TIMESTAMP
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class UsuariosNovosResumo(Base):
    __tablename__ = "caps_usuarios_novos_resumo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuarios_novos = Column(Integer)
    usuarios_novos_anterior = Column(Integer)
    dif_usuarios_novos_anterior = Column(Integer)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
