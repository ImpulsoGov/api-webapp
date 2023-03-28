from sqlalchemy import Column, Integer, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID

from app.models import db

Base = db.Base


class MatriciamentosPorMunicipioUltimoAno(Base):
    __tablename__ = "matriciamentos_por_municipio_ultimo_ano"
    unidade_geografica_id = Column(UUID(as_uuid=True), primary_key=True)
    unidade_geografica_id_sus = Column(CHAR(length=6))
    ano = Column(Text)
    ate_mes = Column(Text)
    quantidade_registrada = Column(Numeric)
    estabelecimentos_na_meta = Column(Integer)
    estabelecimentos_fora_meta = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
