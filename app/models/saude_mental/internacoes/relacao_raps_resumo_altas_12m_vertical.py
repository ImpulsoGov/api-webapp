from sqlalchemy import Column, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

Base = db.Base


class InternacaoRelacaoRapsResumoAltas12mVertical(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_altas_12m_vertical"
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15), primary_key=True)
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_ano = Column(Text)
    ate_mes = Column(Text)
    atendimento_raps_1m_apos = Column(Text)
    prop_altas = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
