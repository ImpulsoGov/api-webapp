from sqlalchemy import TIMESTAMP, Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class InternacoesResumoAltas(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_altas"
    id = Column(Text, primary_key=True)
    periodo = Column(Text)
    competencia = Column(Date)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    altas_atendimento_raps_antes_nao_apos_nao = Column(Numeric)
    altas_atendimento_raps_antes_sim_apos_nao = Column(Numeric)
    altas_atendimento_raps_antes_sim_apos_sim = Column(Numeric)
    altas_atendimento_raps_antes_nao_apos_sim = Column(Numeric)
    altas_atendimento_raps_6m_antes = Column(Numeric)
    altas_atendimento_raps_1m_apos = Column(Numeric)
    altas_atendimento_raps_6m_antes = Column(Numeric)
    altas_total = Column(Numeric)
    perc_altas_atendimento_raps_6m_antes = Column(Numeric)
    perc_altas_atendimento_raps_1m_apos = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
