from sqlalchemy import Column, Integer, TIMESTAMP, String
from app.models import db

Base = db.Base_PRODUCAO
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Trilhas_acesso(Base):
    __tablename__ = "trilhas_acessos"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    usuario_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment="Chave de Identificação Unica do Usuario",
    )
    trilha_id = Column(
        String,
        nullable=False,
        comment="Chave de Identificação Unica da trilha de capacitação",
    )
    criacao_data = Column(TIMESTAMP, nullable=False, comment="Data de Criação")
    modulo = Column(
        Integer,
        nullable=False,
        comment="Chave de Identificação do modulo da trilha de capacitação autorizado para o usuario",
    )
    __table_args__ = {"schema": "impulso_previne"}
