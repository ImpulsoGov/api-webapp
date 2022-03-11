from sqlalchemy import Column, Integer, String,Boolean
from models import db
Base = db.Base

class Municipios(Base):
    __tablename__ = 'municipios'
    id_sus = Column(String,primary_key=True)
    slug = Column(String)
    id_ibge = Column(String)
    id_tse = Column(String)
    id_rfb = Column(String)
    id_bacen = Column(String)
    nome = Column(String)
    eh_capital_uf = Column(Boolean)
    comarca_id_judiciario = Column(Integer)
    regiao_saude_id = Column(Integer)
    regiao_saude_nome  = Column(String)
    regiao_imediata_id_ibge = Column(Integer)
    regiao_imediata_nome  = Column(String)
    regiao_intermediaria_id_ibge = Column(Integer)
    regiao_intermediaria_nome = Column(String)
    microrregiao_id_ibge = Column(Integer)
    microrregiao_nome  = Column(String)
    mesorregiao_id_ibge = Column(Integer)
    mesorregiao_nome = Column(String)
    ddd  = Column(Integer)
    uf_id_ibge = Column(String)
    uf_sigla = Column(String)
    uf_nome = Column(String)
    macrorregiao_nome = Column(String)
    macrorregiao_id_ibge = Column(String)
    uf_normalizado = Column(String)
    municipio_nome_normalizado = Column(String)
    __table_args__ = {'schema': 'suporte'}
