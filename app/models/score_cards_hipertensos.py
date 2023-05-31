from sqlalchemy import Column, Integer, String,DATE, BOOLEAN, DateTime, TIMESTAMP
from app.models import DB_PRODUCAO
Base = DB_PRODUCAO.Base

class ScoreCardHipertensos(Base):
    __tablename__ = 'painel_hipertensos'
    municipio_id_sus = Column(String,nullable=True)
    equipe_ine = Column(String,nullable=True)
    equipe_nome = Column(String,nullable=True)
    id_faixa_etaria = Column(Integer,nullable=True) 
    id_tipo_de_diagnostico = Column(Integer,nullable=True)
    acs_nome = Column(String,primary_key=True,nullable=True)
    id_status_usuario = Column(Integer,nullable=True)
    total_usuarios_com_hipertensao = Column(Integer,nullable=True)
    total_com_consulta_afericao_pa_em_dia = Column(Integer,nullable=True)
    total_com_diagnostico_autorreferido = Column(Integer,nullable=True)
    total_com_diagnostico_clinico = Column(Integer,nullable=True)
    criacao_data = Column(TIMESTAMP,nullable=True)
    atualizacao_data = Column(TIMESTAMP,nullable=True)
    __table_args__ = {'schema': 'impulso_previne_dados_nominais'}

#Base.metadata.create_all(db.engine)