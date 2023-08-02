from sqlalchemy import Column, Date, Integer, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID

from app.models import db

from app.models import db
Base = db.Base_saude_mental


class MatriciamentoPorCapsUltimoAno(Base):
    __tablename__ = "matriciamentos_por_caps_ultimo_ano"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
    competencia = Column(Date)
    ano = Column(Text)
    ate_mes = Column(Text)
    quantidade_registrada = Column(Integer)
    faltam_no_ano = Column(Integer)
    media_mensal_para_meta = Column(Numeric)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    estabelecimento = Column(Text)
    __table_args__ = {"schema": "saude_mental"}
