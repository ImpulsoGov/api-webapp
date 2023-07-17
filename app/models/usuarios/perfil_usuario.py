from sqlalchemy import DATE, Column, ForeignKey

from app.models import db
from app.models.usuarios.usuarios import Usuario

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('suporte')
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relation


class Perfil(Base):
    __tablename__ = "perfil_usuario"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    usuario_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.usuarios.id"),
        default=uuid.uuid4,
        comment="Usuario ID",
    )
    perfil_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suporte.perfil_acesso.id"),
        nullable=False,
        default=uuid.uuid4,
        comment="Perfil de Acesso ID",
    )
    criacao_data = Column(DATE, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(DATE, nullable=False, comment="Data de Atualização")
    usuario = relation(Usuario, backref="perfil_usuario")
    __table_args__ = {"schema": "suporte"}


# Base.metadata.create_all(db.engine)
