from sqlalchemy import Column, Date, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class ProcedimentoPorUsuarioResumo(Base):
    __tablename__ = "caps_procedimentos_por_usuario_por_tempo_servico_resumo"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    periodo_id = Column(UUID(as_uuid=True))
    nome_mes = Column(Text)
    estabelecimento = Column(Text)
    tempo_servico_maior_taxa = Column(Text)
    maior_taxa = Column(Numeric)
    __table_args__ = {"schema": "saude_mental"}
