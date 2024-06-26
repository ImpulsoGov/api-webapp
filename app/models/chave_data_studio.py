from sqlalchemy import TIMESTAMP, Column, String

from app.models import db

Base = db.Base_PRODUCAO


class ChaveDS(Base):
    __tablename__ = "chave_data_studio"
    chave = Column(String, primary_key=True, nullable=False)
    criacao_data = Column(TIMESTAMP, nullable=False)
    __table_args__ = {"schema": "suporte"}
