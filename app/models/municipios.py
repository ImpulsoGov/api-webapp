from sqlalchemy import Boolean, Column, Integer, String

from app.models import db

Base = db.Base

class Municipios(Base):
    __tablename__ = 'municipios'
    id = Column(Integer,primary_key=True)
    estado_sigla = Column(String)
    estado_nome = Column(String)
    estado_nome_normalizado = Column(String)
    estado_id_ibge = Column(String)
    municipio_eh_capital = Column(Boolean)
    municipio_id_sus = Column(String)
    municipio_id_ibge = Column(String)
    municipio_nome = Column(String)
    municipio_nome_normalizado = Column(String)
    slug = Column(String)
    ddd  = Column(Integer)
    municipio_comarca_id_judiciario = Column(Integer)
    macrorregiao_nome = Column(String)
    macrorregiao_id_ibge = Column(String)
    mesorregiao_id_ibge = Column(Integer)
    mesorregiao_nome = Column(String)
    microrregiao_id_ibge = Column(Integer)
    microrregiao_nome  = Column(String)
    regiao_saude_id = Column(Integer)
    regiao_saude_nome  = Column(String)
    regiao_imediata_id_ibge = Column(Integer)
    regiao_imediata_nome  = Column(String)
    regiao_intermediaria_id_ibge = Column(Integer)
    regiao_intermediaria_nome = Column(String)
    __table_args__ = {'schema': 'suporte'}