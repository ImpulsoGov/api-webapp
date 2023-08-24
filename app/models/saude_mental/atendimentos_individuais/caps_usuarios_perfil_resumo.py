from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ResumoPerfilUsuariosAtendimentosIndividuaisCaps(Base):
    __tablename__ = "caps_usuarios_atendimentos_individuais_perfil_resumo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    sexo_predominante = Column(Text)
    usuarios_sexo_predominante = Column(Numeric)
    faixa_etaria_predominante = Column(Text)
    usuarios_faixa_etaria_predominante = Column(Numeric)
    cid_grupo_predominante = Column(Text)
    usuarios_cid_predominante = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
