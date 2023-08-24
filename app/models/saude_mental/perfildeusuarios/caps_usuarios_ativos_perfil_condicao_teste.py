from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class UsuariosPerfilCondicao(Base):
    __tablename__ = "caps_usuarios_ativos_perfil"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuario_abuso_substancias = Column(Text)
    usuario_situacao_rua = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL, "extend_existing": True}
