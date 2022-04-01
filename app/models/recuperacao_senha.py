from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String
from models import db
Base = db.Base
import uuid


class Recuperar(Base):
    __tablename__ = 'recuperacao_senha'
    mail = Column(String, primary_key=True)   
    codigo_recuperacao = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,comment='Codigo de Recuperação de senha')   
    __table_args__ = {'schema': 'suporte'}