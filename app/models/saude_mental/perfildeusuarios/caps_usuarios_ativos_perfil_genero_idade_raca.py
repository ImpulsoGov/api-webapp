from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class UsuariosPerfilIdadeRaca(Base):
    __tablename__ = "caps_usuarios_ativos_perfil"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo = Column(Text)
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuario_raca_cor = Column(Text)
    usuario_sexo = Column(Text)
    usuario_faixa_etaria = Column(Text)
    usuario_faixa_etaria_ordem = Column(Integer)
    __table_args__ = {"schema": "saude_mental", "extend_existing": True}
