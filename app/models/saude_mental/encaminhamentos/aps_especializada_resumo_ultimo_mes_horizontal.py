from sqlalchemy import Column, Date, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class EncaminhamentoApsEspecializadaResumoUltimoMesHorizontal(Base):
    __tablename__ = "encaminhamentos_aps_especializada_resumo_ultimo_mes_horizontal"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    encaminhamentos_especializada = Column(Numeric)
    atendimentos_sm_aps = Column(Numeric)
    perc_encaminhamentos_especializada = Column(Numeric)
    dif_encaminhamentos_especializada_anterior = Column(Numeric)
    nome_mes = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
