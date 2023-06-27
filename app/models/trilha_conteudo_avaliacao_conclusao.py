from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String

from app.models import db

Base = db.Base
import uuid

from sqlalchemy.dialects.postgresql import UUID


class AvaliacaoConclusaoConteudo(Base):
    __tablename__ = "trilha_conteudo_avaliacao_conclusao"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    usuario_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica do usuario",
    )
    codigo_conteudo = Column(String, nullable=False, comment="Codigo do conteudo")
    avaliacao = Column(
        Integer,
        nullable=True,
        comment="Avaliação do usuario do conteudo 1 a 5 estrelas",
    )
    concluido = Column(Boolean, nullable=True, comment="Conteudo concluido pelo usuario")
    criacao_data = Column(TIMESTAMP, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(TIMESTAMP, nullable=False, comment="Data de Atualização")
    __table_args__ = {"schema": "impulso_previne"}
