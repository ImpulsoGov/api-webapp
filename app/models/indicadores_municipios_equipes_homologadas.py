from sqlalchemy import Column, Integer, String, Float, Numeric, DATE
from app.models import db
Base = db.Base

class IndicadoresMuEquipesHomologadas(Base):
    __tablename__ = 'indicadores_municipios_equipes_homologadas'
    id = Column(Integer,primary_key=True)
    periodo_data_inicio = Column(DATE,nullable=False,comment='Data de inicio')
    periodo_data_fim = Column(DATE,nullable=False,comment='Data de finalizacao')
    periodo_codigo = Column(String)
    municipio_id_ibge = Column(String)
    municipio_id_sus = Column(String)
    municipio_nome = Column(String)
    municipio_uf = Column(String)
    indicador_ordem = Column(String)
    indicador_nome = Column(String)
    indicador_meta = Column(Float)
    indicador_peso = Column(Float)
    indicador_numerador = Column(Integer)
    indicador_denominador_informado = Column(Integer)
    indicador_denominador_estimado = Column(Integer)
    indicador_denominador_utilizado = Column(Integer)
    indicador_resultado =  Column(Integer) 
    __table_args__ = {'schema': 'impulso_previne'}
