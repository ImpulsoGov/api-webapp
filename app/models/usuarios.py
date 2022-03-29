from sqlalchemy import Column, Integer, String,Boolean
from models import db
Base = db.Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome_usuario = Column(String)
    hash_senha = Column(String)
    mail = Column(String)
    perfil = Column(String)
    cpf = Column(String)
    __table_args__ = {'schema': 'suporte'}