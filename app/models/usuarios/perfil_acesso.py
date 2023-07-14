from sqlalchemy import DATE, Column, Integer, String

from app.models import db

Base = db.Base
import uuid

from sqlalchemy.dialects.postgresql import UUID


class Perfil_lista(Base):
    __tablename__ = "perfil_acesso"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    perfil = Column(Integer, comment="Perfil de Acesso")
    descricao = Column(String, comment="Descrição do Perfil de Acesso")
    data_criacao = Column(DATE, nullable=False, comment="Data de Criação")
    data_atualizacao = Column(DATE, nullable=False, comment="Data de Atualização")
    __table_args__ = {"schema": "suporte"}
