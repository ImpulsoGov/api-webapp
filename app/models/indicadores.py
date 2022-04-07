from sqlalchemy import Column, Integer, String, Float
from app.models import db
Base = db.Base

class Indicadores(Base):
    __tablename__ = 'indicadores_resumo'
    id = Column(Integer,primary_key=True)
    estado_sigla = Column(String)
    estado_nome = Column(String)
    estado_nome_normalizado = Column(String)
    municipio_id_sus = Column(String)
    municipio_nome = Column(String)
    municipio_nome_normalizado = Column(String)
    indicadores_parametros_id = Column(Integer)
    indicadores_parametros_nome = Column(String)
    indicadores_parametros_nome_normalizado = Column(String)
    indicadores_parametros_ordem = Column(Integer)
    indicadores_parametros_meta = Column(Float)
    indicadores_parametros_peso = Column(Float)
    indicadores_resultados_porcentagem = Column(Float)
    diff_numerador_para_meta = Column(Integer)
    __table_args__ = {'schema': 'impulso_previne'}

