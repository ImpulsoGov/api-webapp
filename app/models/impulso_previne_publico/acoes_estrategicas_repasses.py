from sqlalchemy import Column, Integer, String, DATE

from app.models import db
Base = db.Base_impulso_previne_publico

class AcoesEstrategicasRepasses(Base):
    """Modelo da tabela acoes_estrategicas_repasses que alimenta o gráfico 'Histórico de repasses' """
    
    __tablename__ = 'acoes_estrategicas_repasses'
    municipio_uf = Column(String,primary_key=True)
    codigo = Column(String,primary_key=True)
    data_inicio = Column(DATE,nullable=False,comment='Data de inicio')
    acao_nome = Column(String,primary_key=True)
    pagamento_total = Column(Integer)
    atualizacao_data = Column(DATE,nullable=False,comment='Data de Atualizacao')
    __table_args__ = {'schema': 'impulso_previne_dados_abertos_replica'}
