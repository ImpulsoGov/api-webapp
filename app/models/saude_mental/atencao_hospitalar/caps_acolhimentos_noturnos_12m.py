from sqlalchemy import TIMESTAMP, Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

Base = db.Base


class AcolhimentoNoturno(Base):
    __tablename__ = "caps_acolhimentos_noturnos_12m"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_mes = Column(Text)
    ate_ano = Column(Text)
    acolhimentos_noturnos = Column(Numeric)
    acolhimentos_noturnos_diarias = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
