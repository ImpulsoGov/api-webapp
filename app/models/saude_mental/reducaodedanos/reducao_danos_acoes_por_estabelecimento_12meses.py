from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ReducaoDanos12meses(Base):
    __tablename__ = "reducao_danos_acoes_por_estabelecimento_12meses"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    quantidade_registrada = Column(Integer)
    quantidade_registrada_anterior = Column(Integer)
    dif_quantidade_registrada_anterior = Column(Integer)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    profissional_vinculo_ocupacao = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    estabelecimento = Column(Text)
    a_partir_de = Column(Text)
    ate = Column(Text)
    a_partir_do_ano = Column(Text)
    ate_ano = Column(Text)
    a_partir_do_mes = Column(Text)
    ate_mes = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
