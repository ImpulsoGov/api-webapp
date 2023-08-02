from sqlalchemy import Column, Integer, String, DATE
from app.models import db
from app.models import db
Base = db.Base_impulso_previne_publico

class ValidacaoProducaoAplicacao(Base):
    """Modelo da tabela capitacao_ponderada_validacao_por_producao_por_aplicacao que alimenta o gráficos 'Validação das fichas de produção de cadastro' e 'Aplicações de fichas de cadastro' """
    
    __tablename__ = 'capitacao_ponderada_validacao_por_producao_por_aplicacao'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_uf = Column(String)
    periodo_codigo = Column(String)
    periodo_data_inicio = Column(DATE,nullable=False,comment='Data de inicio',primary_key=True)
    periodo_data_fim = Column(DATE,nullable=False,comment='Data final')
    cnes_id = Column(String)
    cnes_nome = Column(String)
    equipe_id_ine =  Column(String,primary_key=True)
    equipe_nome = Column(String)
    validacao_aplicacao = Column(String,primary_key=True)
    validacao_nome = Column(String,primary_key=True)
    validacao_quantidade = Column(Integer)
    recomendacao = Column(String)
    __table_args__ =  {'schema': 'impulso_previne_dados_abertos_replica'}


