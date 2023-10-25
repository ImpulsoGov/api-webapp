from sqlalchemy import BOOLEAN, DATE, Column, DateTime, Integer, String
from app.models import db
Base = db.Base_impulso_previne_nominal


class Gestantes(Base):
    __tablename__ = "painel_enfermeiras_lista_nominal_gestantes"
    municipio_id_sus = Column(String, nullable=True)
    municipio_uf = Column(String, primary_key=True)
    estabelecimento_cnes = Column(String, nullable=True)
    estabelecimento_nome = Column(String, nullable=True)
    equipe_ine = Column(String, nullable=True)
    equipe_nome = Column(String, nullable=True)
    acs_nome = Column(String, nullable=True)
    acs_data_ultima_visita = Column(DATE, nullable=True)
    gestante_documento_cpf = Column(String, nullable=True)
    gestante_documento_cns = Column(String, nullable=True)
    gestante_nome = Column(String, nullable=True)
    gestante_data_de_nascimento = Column(DateTime, nullable=True)
    gestante_telefone = Column(String, nullable=True)
    gestante_endereco = Column(String, nullable=True)
    gestante_dum = Column(DateTime, nullable=True)
    gestante_idade_gestacional_atual = Column(Integer, nullable=True)
    gestante_idade_gestacional_primeiro_atendimento = Column(Integer, nullable=True)
    gestante_dpp = Column(DateTime, nullable=True)
    gestante_quadrimestre = Column(String, nullable=True)
    gestante_consulta_prenatal_data_limite = Column(DateTime, nullable=True)
    gestacao_dpp_dias_para = Column(Integer, nullable=True)
    gestante_consulta_prenatal_total = Column(Integer, nullable=True)
    gestantes_com_6_consultas = Column(String, nullable=True)
    gestante_consulta_prenatal_ultima_data = Column(DateTime, nullable=True)
    gestante_consulta_prenatal_ultima_dias_desde = Column(Integer, nullable=True)
    atendimento_odontologico_realizado = Column(String, nullable=True)
    atendimento_odontologico_realizado_identificacao = Column(String, nullable=True)
    exame_hiv_realizado = Column(BOOLEAN, nullable=True)
    exame_sifilis_realizado = Column(BOOLEAN, nullable=True)
    exame_sifilis_hiv_realizado = Column(BOOLEAN, nullable=True)
    exame_sifilis_hiv_realizado_identificacao = Column(String, nullable=True)
    possui_registro_aborto = Column(String, nullable=True)
    possui_registro_parto = Column(String, nullable=True)
    criacao_data = Column(DateTime, nullable=True)
    atualizacao_data = Column(DateTime, nullable=True)
    __table_args__ = {"schema": "impulso_previne_dados_nominais_replica"}


# Base.metadata.create_all(db.engine)
