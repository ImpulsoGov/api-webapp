from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class ProcedimentoPorUsuarioTempoServiço(Base):
    __tablename__ = "caps_procedimentos_por_usuario_por_tempo_servico"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    tempo_servico_descricao = Column(Text)
    procedimentos_por_usuario = Column(Numeric)
    estabelecimento_linha_perfil = Column(Text)
    # estabelecimento_linha_idade = Column(Text)
    estabelecimento = Column(Text)
    periodo = Column(Text)
    nome_mes = Column(Text)
    __table_args__ = {"schema": "saude_mental"}
