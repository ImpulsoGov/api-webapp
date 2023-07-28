from sqlalchemy import Column, String, PrimaryKeyConstraint
from app.models import db
from app.models._conexao_banco import conexao_banco
Base = conexao_banco('impulso_previne_publico')

class AcoesEstrategicasVigenteAgrupada(Base):
    """Modelo da tabela acoes_estrategicas_vigente_agrupada que alimenta o gráfico 'Ações Estratégicas implementadas em vigor' """
    
    __tablename__ = 'acoes_estrategicas_vigente_agrupada'
    municipio_uf = Column(String,primary_key=True)
    acao_nome = Column(String,primary_key=True)
    nivel_repasse = Column(String)
    periodicidade = Column(String)
    ultimo_pagamento = Column(String)
    requisitos = Column(String)
    __table_args__ =  {'schema': 'impulso_previne_dados_abertos_replica'}

