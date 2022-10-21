from sqlalchemy import Column, Integer, String,DATE
from app.models import DB_ANALITICO,busca_ativa
Base = DB_ANALITICO.Base

class Gestantes(Base):
    __tablename__ = 'painel_enfermeiras_lista_nominal_gestantes'
    municipio_uf = Column(String, primary_key=True)   
    estabelecimento_nome = Column(String,nullable=True)   
    equipe_nome = Column(String,nullable=True)   
    __table_args__ = {'schema': 'busca_ativa'}

#Base.metadata.create_all(db.engine)