from sqlalchemy import Column, Integer, String, Float, Numeric, DATE
from app.models import db

Base = db.Base_impulso_previne_publico


class IndicadoresDesempenho(Base):
    __tablename__ = "indicadores_desempenho_score_equipes_validas"
    municipio_id_ibge = Column(String)
    municipio_id_sus = Column(String, primary_key=True)
    municipio_nome = Column(String)
    municipio_uf = Column(String)
    periodo_codigo = Column(String)
    periodo_data_inicio = Column(DATE, nullable=False, comment="Data de inicio")
    periodo_data_fim = Column(DATE, nullable=False, comment="Data de finalizacao")
    indicador_ordem = Column(String)
    indicador_prioridade = Column(Integer)
    indicador_nome = Column(String)
    indicador_peso = Column(Float)
    indicador_validade_resultado = Column(Float)
    indicador_acoes_por_usuario = Column(Float)
    indicador_numerador = Column(Integer)
    indicador_denominador_estimado = Column(Integer)
    indicador_denominador_utilizado_informado = Column(String)
    indicador_denominador_utilizado = Column(Float)
    indicador_denominador_utilizado_tipo = Column(String)
    indicador_denominador_informado_diferenca_utilizado = Column(Numeric)
    indicador_denominador_informado_diferenca_utilizado_formatado = Column(String)
    indicador_nota = Column(Numeric)
    indicador_nota_porcentagem = Column(Integer)
    indicador_meta = Column(Float)
    indicador_diferenca_meta = Column(Float)
    indicador_recomendacao = Column(String)
    delta = Column(Numeric)
    delta_formatado = Column(String)
    indicador_usuarios_100_porcento_meta = Column(Numeric)
    indicador_usuarios_cadastrados_sem_atendimento = Column(Numeric)
    indicador_usuarios_cadastrar_para_meta = Column(Numeric)
    indicador_score = Column(Integer)
    criacao_data = Column(DATE, nullable=False, comment="Data de Criação")
    atualizacao_data = Column(DATE, nullable=False, comment="Data de Atualizacao")
    indicador_denominador_informado = Column(Integer)
    __table_args__ = {"schema": "impulso_previne_dados_abertos_replica"}
