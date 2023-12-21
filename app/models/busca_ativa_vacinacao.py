from sqlalchemy import Column, Integer, String, DateTime
from app.models import DB_PRODUCAO
Base = DB_PRODUCAO.Base

class Vacinacao(Base):
    __tablename__ = 'painel_vacinacao_lista_nominal'
    municipio_id_sus = Column(String,nullable=True)
    municipio_uf = Column(String,nullable=True)
    cidadao_nome = Column(String,nullable=True)
    cidadao_nome_responsavel = Column(String,nullable=True)
    cidadao_cpf_dt_nascimento = Column(String,nullable=True, primary_key=True)
    cidadao_idade_meses = Column(Integer,nullable=True)
    quadrimestre_completa_1_ano = Column(String,nullable=True)
    id_status_quadrimestre = Column(Integer,nullable=True)
    data_ou_prazo_1dose_polio = Column(DateTime,nullable=True)
    data_ou_prazo_2dose_polio = Column(DateTime,nullable=True)
    data_ou_prazo_3dose_polio = Column(DateTime,nullable=True)
    id_status_polio = Column(Integer,nullable=True)
    id_cor_1dose_polio = Column(Integer,nullable=True)
    id_cor_2dose_polio = Column(Integer,nullable=True)
    id_cor_3dose_polio = Column(Integer,nullable=True)
    data_ou_prazo_1dose_penta = Column(DateTime,nullable=True)
    data_ou_prazo_2dose_penta = Column(DateTime,nullable=True)
    data_ou_prazo_3dose_penta = Column(DateTime,nullable=True)
    id_status_penta = Column(Integer,nullable=True)
    id_cor_1dose_penta = Column(Integer,nullable=True)
    id_cor_2dose_penta = Column(Integer,nullable=True)
    id_cor_3dose_penta = Column(Integer,nullable=True)
    acs_nome = Column(String,nullable=True)
    equipe_ine = Column(String,nullable=True)
    equipe_nome = Column(String,nullable=True)
    criacao_data = Column(DateTime,nullable=True)
    atualizacao_data = Column(DateTime,nullable=True)
    dt_registro_producao_mais_recente = Column(DateTime,nullable=True)   
    __table_args__ = {'schema': 'impulso_previne_dados_nominais'}

#Base.metadata.create_all(db.engine)
    
