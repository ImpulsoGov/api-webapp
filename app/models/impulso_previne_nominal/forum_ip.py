import uuid

from sqlalchemy import DATE, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relation

from app.models import db
from app.models.usuarios.usuarios import Usuario

from app.models import db
Base = db.Base_impulso_previne_nominal


class Forum_ip(Base):
    __tablename__ = "forum_ip"
    id = Column(Integer, primary_key=True, comment="Topico ID")
    titulo = Column(String, nullable=False, comment="Titulo do Topico")
    texto = Column(String, nullable=False, comment="Texto inicial do Topico")
    respostas = Column(JSONB, comment="Respostas do Topico")
    usuario = Column(String, nullable=False, comment="Nome do Usuario")
    usuario_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.usuarios.id"),
        default=uuid.uuid4,
        comment="Usuario ID",
    )
    data_criacao = Column(DATE, nullable=False, comment="Data de Criação")
    data_atualizacao = Column(DATE, nullable=False, comment="Data de Atualização")
    __table_args__ = {"schema": "impulso_previne"}


# Base.metadata.create_all(db.engine)
