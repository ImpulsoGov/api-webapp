from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class EncaminhamentoApsCaps(Base):
    __tablename__ = "consultorio_na_rua_atendimentos_ultimos_12meses"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    quantidade_registrada = Column(Integer)
    quantidade_registrada_anterior = Column(Integer)
    dif_quantidade_registrada_anterior = Column(Integer)
    a_partir_de = Column(Text)
    ate = Column(Text)
    a_partir_do_ano = Column(Text)
    ate_ano = Column(Text)
    a_partir_do_mes = Column(Text)
    ate_mes = Column(Text)
    tipo_producao = Column(Text)
    __table_args__ = {"schema": "saude_mental"}