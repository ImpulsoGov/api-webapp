from sqlalchemy import Column, Date, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class EncaminhamentoApsEspecializadaResumoUltimoMesVertical(Base):
    __tablename__ = "encaminhamentos_aps_especializada_resumo_ultimo_mes_vertical"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    nome_mes = Column(Text)
    encaminhamento = Column(Text)
    prop_atendimentos = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
