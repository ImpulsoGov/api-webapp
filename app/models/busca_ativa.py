from sqlite3 import Date
from sqlalchemy import Column, Integer, String,DATE, BOOLEAN
from app.models import DB_ANALITICO,busca_ativa
Base = DB_ANALITICO.Base

class Gestantes(Base):
    __tablename__ = 'painel_enfermeiras_lista_nominal_gestantes'
    municipio_uf = Column(String, primary_key=True)
    municipio_id_sus = Column(String,nullable=True)
    municipio_uf = Column(String,nullable=True)
    estabelecimento_cnes = Column(String,nullable=True)
    estabelecimento_nome = Column(String,nullable=True)
    equipe_ine = Column(String,nullable=True)
    equipe_nome = Column(String,nullable=True)
    acs_nome = Column(String,nullable=True)
    acs_data_ultima_visita = Column(DATE,nullable=True)
    gestante_documento_cpf = Column(String,nullable=True)
    gestante_documento_cns = Column(String,nullable=True)
    gestante_nome = Column(String,nullable=True)
    gestante_data_de_nascimento = Column(Date,nullable=True)
    gestante_telefone = Column(String,nullable=True)
    gestante_endereco = Column(String,nullable=True)
    gestante_dum = Column(Date,nullable=True)
    gestante_idade_gestacional_atual = Column(Integer,nullable=True)
    gestante_idade_gestacional_primeiro_atendimento = Column(Integer,nullable=True)
    gestante_dpp  = Column(Date,nullable=True)
    gestante_consulta_prenatal_data_limite = Column(Date,nullable=True)
    gestante_dpp_dias_para = Column(Integer,nullable=True)
    gestante_consulta_prenatal_total = Column(Integer,nullable=True)
    gestante_consulta_prenatal_ultima_data = Column(Date,nullable=True)
    gestante_consulta_prenatal_ultima_dias_desde = Column(Integer,nullable=True)
    atendimento_odontologico_realizado = Column(BOOLEAN,nullable=True)
    exame_hiv_realizado  = Column(BOOLEAN,nullable=True)
    exame_sifilis_realizado  = Column(BOOLEAN,nullable=True)
    exame_sifilis_hiv_realizado  = Column(BOOLEAN,nullable=True)
    possui_registro_aborto  = Column(String,nullable=True)
    possui_registro_parto  = Column(String,nullable=True)
    criacao_data = Column(Date,nullable=True)
    atualizacao_data = Column(Date,nullable=True)
    __table_args__ = {'schema': 'busca_ativa'}

#Base.metadata.create_all(db.engine)