from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from app.models import db
from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_publico')

class CadastrosEquipeContagem(Base):
    """Modelo da tabela capitacao_ponderada_contagem_equipes que alimenta o gráfico 'Suas equipes' """

    __tablename__ = 'capitacao_ponderada_contagem_equipes'
    municipio_id_sus = Column(String,primary_key=True)
    municipio_uf = Column(String)
    periodo_codigo = Column(String,primary_key=True)
    equipe_status_tipo = Column(String)
    equipe_status = Column(String,primary_key=True)
    equipe_total = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint('municipio_id_sus','periodo_codigo','equipe_status'),
        {'schema': 'impulso_previne_dados_abertos_replica'}
    )


