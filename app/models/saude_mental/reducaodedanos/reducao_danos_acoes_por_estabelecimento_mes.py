from sqlalchemy import Column, Date, Float, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ReducaoDanos(Base):
    __tablename__ = "reducao_danos_acoes_por_estabelecimento_mes"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(VARCHAR(length=6))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    quantidade_registrada = Column(Numeric)
    quantidade_registrada_anterior = Column(Numeric)
    dif_quantidade_registrada_anterior = Column(Numeric)
    nome_mes = Column(Text)
    profissional_vinculo_ocupacao = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
