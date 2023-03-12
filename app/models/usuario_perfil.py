from xml.etree.ElementTree import Comment

from models import db
from sqlalchemy import DATE, Boolean, Column, ForeignKey, Integer, String

Base = db.Base
import uuid

from sqlalchemy.dialects.postgresql import UUID


class Perfil(Base):
    __tablename__ = "perfil_usuario"
    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.usuarios.id"),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    perfil = Column(Integer, nullable=True, comment="Perfil de Acesso")
    criacao_data = Column(DATE, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(
        DATE, nullable=False, comment="Data de Atualização"
    )
    __table_args__ = {"schema": "suporte"}
