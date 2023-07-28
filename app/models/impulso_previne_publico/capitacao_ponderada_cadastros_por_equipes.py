from sqlalchemy import Column, Integer, String, Float, Numeric, DATE,PrimaryKeyConstraint
from app.models import db
from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_publico')

class CadastrosEquipes(Base):
    """Modelo da tabela capitacao_ponderada_cadastros_por_equipes que alimenta os gráficos 'Evolução dos cadastros' e 'Desempenho das equipes' """
    
    __tablename__ = 'capitacao_ponderada_cadastros_por_equipes'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_nome = Column(String)
    municipio_uf = Column(String)
    periodo_codigo = Column(String)
    data_inicio = Column(DATE,nullable=False,comment='Data de inicio')
    tipologia = Column(String)
    uf_nome = Column(String)
    cnes_id = Column(String,primary_key=True)
    cnes_nome = Column(String)
    equipe_id_ine =  Column(String,primary_key=True)
    equipe_nome = Column(String)
    equipe_status = Column(String)
    municipio_ultimo_parametro = Column(Integer)
    cadastro_total = Column(Integer)
    cadastros_com_pontuacao = Column(Integer)
    equipe_parametro = Column(Integer)
    cobertura_parametro_porcentagem = Column(Float)
    criacao_data = Column(DATE,nullable=False,comment='Data de Criação')
    atualizacao_data = Column(DATE,nullable=False,comment='Data de Atualizacao')
    __table_args__ = (
        {'schema': 'impulso_previne_dados_abertos_replica'}
    )


