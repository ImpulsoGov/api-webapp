from sqlalchemy import Column, Integer, String
from app.models import db
Base = db.Base

class User(Base):
    __tablename__ = 'teste_orm'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    idade = Column(Integer)

