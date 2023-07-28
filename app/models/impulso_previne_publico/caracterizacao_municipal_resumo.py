from sqlalchemy import Column, Integer, String
from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_publico')

class CaracterizacaoMunicipalResumo(Base):
    """Modelo da tabela caracterizacao_municipal_resumo que alimenta o painel Caracterização Municipal"""
    
    __tablename__ = 'caracterizacao_municipal_resumo'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_nome = Column(String)
    municipio_uf = Column(String)
    municipio_tipologia = Column(String)
    municipio_populacao_2020 = Column(Integer)
    periodo_codigo = Column(String)
    equipe_total = Column(Integer)
    cadastros_equipes_validas = Column(Integer)
    cadastros_equipes_validas_com_ponderacao = Column(Integer)
    cadastro_parametro = Column(Integer)
    __table_args__ = {'schema': 'impulso_previne'}

