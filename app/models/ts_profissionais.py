from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from app.models import db
Base = db.Base

class Profissionais(Base):
    __tablename__ = 'profissionais'
    ibge = Column(String)
    cnes = Column(String)
    estabelecimento = Column(String)
    ine = Column(String)
    nome_equipe = Column(String)
    tipo_equipe = Column(String)
    nome = Column(String)
    cns = Column(String, primary_key=True)   
    cbo = Column(String)
    descricao_natureza_juridica = Column(String)
    gestao = Column(String)
    sus = Column(String)
    residente = Column(String)
    preceptor = Column(String)
    vinculo_estabelecimento = Column(String)
    vinculo_empregador = Column(String)
    detalhamento_vinculo = Column(String)
    ch_outros = Column(String)
    ch_hosp = Column(String)
    ch_amb = Column(String)
    ch_total = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    __table_args__ = {'schema': 'territorios'}