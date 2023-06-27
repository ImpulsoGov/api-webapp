from xml.etree.ElementTree import Comment
from sqlalchemy import Column, Integer, String, Boolean, DATE, ForeignKey
from app.models import db

Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class UsuarioIP(Base):
    __tablename__ = "usuarios_ip"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    municipio = Column(String, nullable=False, comment="Municipio de atuação do usuario")
    cargo = Column(String, nullable=False, comment="Cargo atuação do usuario")
    telefone = Column(String, nullable=False, comment="Telefone de contato")
    whatsapp = Column(Boolean, nullable=False, comment="Numero informado possui whatsapp")
    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.usuarios.id"),
        nullable=False,
        default=uuid.uuid4,
        comment="Perfil de Acesso ID",
    )
    equipe = Column(String, nullable=False, comment="equipe de atuação do usuario")
    criacao_data = Column(DATE, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(DATE, nullable=False, comment="Data de Atualização")
    __table_args__ = {"schema": "suporte"}
