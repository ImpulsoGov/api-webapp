from sqlalchemy import Column, Numeric, Text, Date, Float, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

Base = db.Base


class AmbulatorioUsuariosPerfil(Base):
    __tablename__ = "ambulatorio_usuarios_perfil"
    id = Column(Text, primary_key=True)
    unidade_geografica_id = Column(UUID(as_uuid=True))
    unidade_geografica_id_sus = Column(VARCHAR(length=15))
    competencia = Column(Date)
    atualizacao_data = Column(TIMESTAMP(timezone=True))
    periodo_id = Column(UUID(as_uuid=True))
    periodo_ordem = Column(Float)
    periodo = Column(Text)
    nome_mes = Column(Text)
    usuario_faixa_etaria = Column(Text)
    usuario_faixa_etaria_ordem = Column(Text)
    cid_grupo_descricao_curta = Column(Text)
    usuario_sexo = Column(Text)
    usuarios_unicos_mes = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
