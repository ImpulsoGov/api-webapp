from sqlalchemy import Column, Date, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class EncaminhamentoApsCapsResumoUltimoMesHorizontal(Base):
    __tablename__ = "encaminhamentos_aps_caps_resumo_ultimo_mes_horizontal"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    nome_mes = Column(Text)
    encaminhamentos_caps = Column(Numeric)
    atendimentos_sm_aps = Column(Numeric)
    perc_encaminhamentos_caps = Column(Numeric)
    dif_encaminhamentos_caps_anterior = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
