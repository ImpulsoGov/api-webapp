from sqlalchemy import TIMESTAMP, Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class InternacoesResumoAdmissoes(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_admissoes"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_mes = Column(Text)
    ate_ano = Column(Text)
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    competencia = Column(Date)
    internacoes_atendimento_raps_antes = Column(Numeric)
    internacoes_alcool_drogas = Column(Numeric)
    internacoes_transtornos = Column(Numeric)
    internacoes_total = Column(Numeric)
    perc_internacoes_atendimento_raps_antes = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
