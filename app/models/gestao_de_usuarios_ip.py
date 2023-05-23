from sqlalchemy import Column, Text, VARCHAR

from sqlalchemy.dialects.postgresql import UUID
from app.models import db

Base = db.Base


class GestaoUsuariosIP(Base):
    __tablename__ = "gestao_de_usuarios_ip"
    id_usuario = Column(UUID(as_uuid=True))
    municipio = Column(VARCHAR)
    equipe = Column(VARCHAR)
    cargo = Column(VARCHAR)
    nome_usuario = Column(VARCHAR)
    mail = Column(VARCHAR, primary_key=True)
    telefone = Column(VARCHAR)
    autorizacoes = Column(Text)
    cpf = Column(VARCHAR)
    __table_args__ = {"schema": "suporte"}
