from sqlalchemy import DATE, Column, ForeignKey, Integer, String

from app.models import db

Base = db.Base_PRODUCAO


class Estabelecimentos(Base):
    __tablename__ = "estabelecimentos"
    ibge = Column(String)
    cnes = Column(String, primary_key=True)
    nome_fantasia = Column(String)
    tipo_estabelecimento = Column(String)
    horario = Column(String)
    natureza_juridica = Column(String)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cnpj_proprio = Column(String)
    cnpj_mantenedora = Column(String)
    tipo_gestao = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    __table_args__ = {"schema": "territorios"}


# Base.metadata.create_all(db.engine)
