import uuid

from sqlalchemy import DATE, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relation

from app.models import db
from app.models.usuarios import usuarios

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_nominal')


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
    usuario_id_rel = relation(usuarios.Usuario, backref="forum_ip")
    __table_args__ = {"schema": "impulso_previne"}


# Base.metadata.create_all(db.engine)
