from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import CHAR, UUID

from app.models import db

Base = db.Base


class PerfilUsuariosAtendimentosIndividuaisCaps(Base):
    __tablename__ = "caps_usuarios_atendimentos_individuais_perfil"
    id = Column(Text, primary_key=True)
    # unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(CHAR(length=6))
    competencia = Column(Date)
    # periodo_id = Column(UUID(as_uuid=True))
    usuario_faixa_etaria_descricao = Column(Text)
    # usuario_faixa_etaria_ordem = Column(CHAR(length=7))
    usuario_condicao_saude = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuarios_apenas_atendimento_individual = Column(Numeric)
    usuarios_frequentantes = Column(Numeric)
    usuario_sexo = Column(Text)
    usuario_raca_cor = Column(Text)
    estabelecimento = Column(Text)
    periodo = Column(Text)
    # nome_mes = Column(Text)
    # periodo_ordem = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
