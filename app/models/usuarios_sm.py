from app.models import db

Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey


class UsuarioSM(Base):
    __tablename__ = "usuarios_sm"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de identificação única",
    )
    municipio_id_ibge = Column(
        String, nullable=False, comment="Municipio de atuação do usuário"
    )
    cargo_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.cargos.id"),
        nullable=False,
        default=uuid.uuid4,
        comment="Id do cargo do usuário",
    )
    telefone = Column(String, nullable=False, comment="Telefone de contato")
    whatsapp = Column(
        Boolean, nullable=False, comment="Telefone informado possui whatsapp?"
    )
    id_usuario = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.usuarios.id"),
        nullable=False,
        default=uuid.uuid4,
        comment="Id do usuário",
    )
    unidade_saude = Column(
        String, nullable=False, comment="Unidade de atuação do usuário"
    )
    criacao_data = Column(TIMESTAMP, nullable=False, comment="Data de criação")
    atualizacao_data = Column(TIMESTAMP, nullable=False, comment="Data de atualização")
    __table_args__ = {"schema": "suporte"}
