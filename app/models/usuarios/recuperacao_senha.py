from sqlalchemy import Column, TIMESTAMP, Integer, String
from app.models import db

Base = db.Base_usuarios


class Recuperar(Base):
    __tablename__ = "recuperacao_senha"
    mail = Column(String, primary_key=True)
    cpf = Column(String, nullable=False)
    codigo_recuperacao = Column(
        Integer, nullable=False, comment="Codigo de Recuperação de senha"
    )
    criacao_data = Column(TIMESTAMP, nullable=False, comment="Data de Criação")
    __table_args__ = {"schema": "suporte"}
