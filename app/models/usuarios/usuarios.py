from xml.etree.ElementTree import Comment

from sqlalchemy import DATE, Boolean, Column, Integer, String

# from app.models import db
# Base = db.Base
import uuid

from sqlalchemy.dialects.postgresql import UUID

from app.models import db
Base = db.Base_usuarios

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Chave de Identificação Unica",
    )
    nome_usuario = Column(String, nullable=False, comment="Nome Completo do Usuario")
    hash_senha = Column(String, nullable=True, comment="Hash da senha de acesso")
    mail = Column(String, nullable=False, comment="e-mail do usuario")
    cpf = Column(String, nullable=False, comment="ID Cadastro de Pessoa Fisica")
    perfil_ativo = Column(Boolean, comment="Perfil Ativo")
    criacao_data = Column(DATE, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(DATE, nullable=False, comment="Data de Atualização")
    __table_args__ = {"schema": "suporte"}
