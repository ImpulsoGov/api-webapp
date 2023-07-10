from sqlalchemy import Column, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class InternacaoRelacaoRapsResumoAltas12m(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_altas_12m"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_ano = Column(Text)
    ate_mes = Column(Text)
    altas_atendimento_raps_antes_nao_apos_nao = Column(Numeric)
    altas_atendimento_raps_antes_sim_apos_nao = Column(Numeric)
    altas_atendimento_raps_antes_sim_apos_sim = Column(Numeric)
    altas_atendimento_raps_antes_nao_apos_sim = Column(Numeric)
    altas_atendimento_raps_6m_antes = Column(Numeric)
    altas_atendimento_raps_1m_apos = Column(Numeric)
    altas_total = Column(Numeric)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    perc_altas_atendimento_raps_6m_antes = Column(Numeric)
    perc_altas_atendimento_raps_1m_apos = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
