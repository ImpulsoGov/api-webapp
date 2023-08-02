from sqlalchemy import Column, Date, Float, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

from app.models import db
Base = db.Base_saude_mental


class UsuarioNovoPorCondicao(Base):
    __tablename__ = "caps_usuarios_novos_perfil_condicao"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=6))
    periodo_id = Column(UUID(as_uuid=True))
    competencia = Column(Date)
    estabelecimento_linha_perfil = Column(Text)
    estabelecimento_linha_idade = Column(Text)
    usuario_situacao_rua = Column(Text)
    usuario_abuso_substancias = Column(Text)
    usuarios_novos = Column(Numeric)
    usuarios_novos_anterior = Column(Numeric)
    dif_usuarios_novos_anterior = Column(Numeric)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    estabelecimento = Column(VARCHAR)
    periodo = Column(Text)
    nome_mes = Column(Text)
    periodo_ordem = Column(Float)
    __table_args__ = {"schema": "saude_mental"}
