from sqlalchemy import Column, Numeric, Text, Date, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

Base = db.Base


class InternacoesResumoAdmissoes12m(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_admissoes_12m"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_ano = Column(Text)
    ate_mes = Column(Text)
    internacoes_atendimento_raps_antes = Column(Numeric)
    internacoes_alcool_drogas = Column(Numeric)
    internacoes_transtornos = Column(Numeric)
    internacoes_total = Column(Numeric)
    perc_internacoes_atendimento_raps_antes = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
