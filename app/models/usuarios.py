from xml.etree.ElementTree import Comment
from sqlalchemy import Column, Integer, String,Boolean,DATE
from app.models import db
Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,comment='Chave de Identificação Unica')   
    nome_usuario = Column(String,nullable=False,comment='Nome Completo do Usuario')
    hash_senha = Column(String,nullable=False,comment='Hash da senha de acesso')
    mail = Column(String,nullable=False,comment='e-mail do usuario')
    cpf = Column(String,nullable=False,comment='ID Cadastro de Pessoa Fisica')
    criacao_data = Column(DATE,nullable=False,comment='Data de Criação')
    atualizacao_data = Column(DATE,nullable=False,comment='Data de Atualização')
    __table_args__ = {'schema': 'suporte'}