from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class AbandonoPorGeneroEIdade(Base):
    __tablename__ = "caps_adesao_usuarios_perfil_genero_idade"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR)
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuario_faixa_etaria = Column(Text)
    estatus_adesao_mes = Column(Text)
    estatus_adesao_final = Column(Text)
    quantidade_registrada = Column(Numeric)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    usuario_sexo = Column(Text)
    estabelecimento = Column(VARCHAR)
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
