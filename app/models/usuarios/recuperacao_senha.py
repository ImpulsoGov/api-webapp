from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.models import db

Base = db.Base
import uuid


class Recuperar(Base):
    __tablename__ = "recuperacao_senha"
    mail = Column(String, primary_key=True)
    codigo_recuperacao = Column(
        Integer, nullable=False, comment="Codigo de Recuperação de senha"
    )
    criacao_data = Column(DateTime, nullable=False, comment="Data de Criação")
    __table_args__ = {"schema": "suporte"}
