from sqlalchemy import Column, Integer, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class MatriciamentoPorMunicipioUltimoAno(Base):
    __tablename__ = "matriciamentos_por_municipio_ultimo_ano"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
    ano = Column(Text)
    ate_mes = Column(Text)
    quantidade_registrada = Column(Numeric)
    estabelecimentos_na_meta = Column(Integer)
    estabelecimentos_fora_meta = Column(Integer)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
