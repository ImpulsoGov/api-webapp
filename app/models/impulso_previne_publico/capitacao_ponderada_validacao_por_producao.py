from sqlalchemy import Column, Integer, String, Numeric, DATE, PrimaryKeyConstraint
from app.models import db
from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_publico')

class ValidacaoProducao(Base):
    """Modelo da tabela capitacao_ponderada_validacao_por_producao que alimenta o gráfico 'Cadastros Preliminares Inválidos' """
    
    __tablename__ = 'capitacao_ponderada_validacao_por_producao'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_uf = Column(String)
    periodo_codigo = Column(String)
    periodo_data_inicio = Column(DATE,nullable=False,comment='Data de inicio')
    periodo_data_fim = Column(DATE,nullable=False,comment='Data final')
    cnes_id = Column(String)
    cnes_nome = Column(String)
    equipe_id_ine =  Column(String)
    equipe_nome = Column(Numeric)
    validacao_nome = Column(String)
    validacao_quantidade = Column(Integer)
    recomendacao = Column(String)
    __table_args__ = (
        PrimaryKeyConstraint('municipio_id_sus','periodo_data_inicio','equipe_id_ine','validacao_aplicacao','validacao_nome'),
        {'schema': 'impulso_previne_dados_abertos_replica'}
    )

