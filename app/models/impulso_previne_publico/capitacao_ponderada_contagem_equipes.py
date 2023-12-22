from sqlalchemy import Column, Integer, String
from app.models import db
from app.models import db
Base = db.Base_impulso_previne_publico

class CadastrosEquipeContagem(Base):
    """Modelo da tabela capitacao_ponderada_contagem_equipes que alimenta o gráfico 'Suas equipes' """

    __tablename__ = 'capitacao_ponderada_contagem_equipes'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_uf = Column(String)
    periodo_codigo = Column(String,primary_key=True)
    equipe_status_tipo = Column(String)
    equipe_status = Column(String,primary_key=True)
    equipe_total = Column(Integer)
    __table_args__ = {'schema': 'impulso_previne_dados_abertos_replica'}


