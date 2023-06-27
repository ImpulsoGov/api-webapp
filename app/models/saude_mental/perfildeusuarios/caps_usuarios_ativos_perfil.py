from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class UsuariosPerfil(Base):
    __tablename__ = "caps_usuarios_ativos_perfil"
    id = Column(Text, primary_key=True)
    # unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    competencia = Column(Date)
    # atualizacao_data = Column(TIMESTAMP(timezone=True))
    # periodo_id = Column(UUID(as_uuid=True))
    # periodo_ordem = Column(Float)
    periodo = Column(Text)
    # nome_mes = Column(Text)
    estabelecimento = Column(Text)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    ativos_mes = Column(Integer)
    ativos_3meses = Column(Integer)
    tornandose_inativos = Column(Integer)
    usuario_raca_cor = Column(Text)
    usuario_sexo = Column(Text)
    usuario_abuso_substancias = Column(Text)
    usuario_situacao_rua = Column(Text)
    usuario_condicao_saude = Column(Text)
    usuario_faixa_etaria = Column(Text)
    usuario_tempo_servico = Column(Text)
    # usuario_tempo_servico_ordem = Column(Integer)
    # usuario_faixa_etaria_ordem = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
