from sqlalchemy import Column, Date, Float, Integer, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR

from app.models import db

from app.models._conexao_banco import conexao_banco
Base = conexao_banco('saude_mental')


class UsuariosNovosPerfil(Base):
    __tablename__ = "caps_usuarios_novos_perfil"
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
    usuario_raca_cor = Column(Text)
    usuario_sexo = Column(Text)
    usuario_situacao_rua = Column(Text)
    usuario_condicao_saude = Column(Text)
    usuario_faixa_etaria = Column(Text)
    # usuario_faixa_etaria_ordem = Column(Integer)
    # usuario_idade = Column(Float)
    usuario_abuso_substancias = Column(Text)
    usuarios_novos = Column(Integer)
    # usuarios_novos_anterior = Column(Integer)
    # dif_usuarios_novos_anterior = Column(Integer)
    __table_args__ = {"schema": "saude_mental"}
