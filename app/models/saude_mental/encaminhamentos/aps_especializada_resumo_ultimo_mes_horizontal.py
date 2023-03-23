from sqlalchemy import Column, Date, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

Base = db.Base


class EncaminhamentosApsEspecializadaResumoUltimoMesHorizontal(Base):
    __tablename__ = (
        "encaminhamentos_aps_especializada_resumo_ultimo_mes_horizontal"
    )
    unidade_geografica_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=True
    )
    unidade_geografica_id_sus = Column(VARCHAR(length=15), nullable=True)
    competencia = Column(Date, nullable=True)
    periodo_id = Column(UUID(as_uuid=True), nullable=True)
    encaminhamentos_especializada = Column(Numeric, nullable=True)
    atendimentos_sm_aps = Column(Numeric, nullable=True)
    perc_encaminhamentos_especializada = Column(Numeric, nullable=True)
    dif_encaminhamentos_especializada_anterior = Column(Numeric, nullable=True)
    nome_mes = Column(Text, nullable=True)
    __table_args__ = {"schema": "saude_mental"}
