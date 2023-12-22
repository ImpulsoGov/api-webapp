from sqlalchemy import Column, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class InternacaoRelacaoRapsResumoAdmissoes12m(Base):
    __tablename__ = "internacoes_relacao_raps_resumo_admissoes_12m"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    a_partir_de_ano = Column(Text)
    a_partir_de_mes = Column(Text)
    ate_ano = Column(Text)
    ate_mes = Column(Text)
    internacoes_atendimento_raps_antes = Column(Numeric)
    internacoes_alcool_drogas = Column(Numeric)
    internacoes_total = Column(Numeric)
    internacoes_transtornos = Column(Numeric)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    perc_internacoes_atendimento_raps_antes = Column(Numeric)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
