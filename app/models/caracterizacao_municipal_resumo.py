from sqlalchemy import Column, Integer, String
from app.models import db
Base = db.Base

class CaracterizacaoMunicipal(Base):
    __tablename__ = 'caracterizacao_municipal_resumo'
    periodo_codigo = Column(String)
    municipio_id_sus = Column(String,primary_key=True)
    municipio_nome = Column(String)
    municipio_uf = Column(String)
    municipio_tipologia = Column(String)
    municipio_populacao_2020 = Column(Integer)
    equipe_total = Column(Integer)
    cadastro_parametro = Column(Integer)
    cadastros_equipes_validas = Column(Integer)
    cadastros_equipes_validas_com_ponderacao =  Column(Integer)
    __table_args__ = {'schema': 'impulso_previne_dados_abertos_replica'}
