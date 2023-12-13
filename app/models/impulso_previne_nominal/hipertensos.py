from sqlalchemy import BOOLEAN, DATE, TIMESTAMP, Column, DateTime, Integer, String
from app.models import DB_PRODUCAO

Base = DB_PRODUCAO.Base


class Hipertensos(Base):
    __tablename__ = "painel_enfermeiras_lista_nominal_hipertensos"
    municipio_id_sus = Column(String, nullable=True)
    municipio_uf = Column(String, primary_key=True)
    quadrimestre_atual = Column(String, nullable=True)
    realizou_afericao_ultimos_6_meses = Column(BOOLEAN, nullable=True)
    dt_afericao_pressao_mais_recente = Column(String, nullable=True)
    realizou_consulta_ultimos_6_meses = Column(String, nullable=True)
    dt_consulta_mais_recente = Column(DATE, nullable=True)
    prazo_proxima_afericao_pa = Column(String, nullable=True)
    prazo_proxima_consulta = Column(String, nullable=True)
    consulta_e_afericao_em_dia = Column(Integer, nullable=True)
    status_em_dia = Column(String, nullable=True)
    status_usuario = Column(String, nullable=True)
    identificacao_condicao_hipertensao = Column(String, nullable=True)
    cidadao_cpf = Column(String, nullable=True)
    cidadao_cpf_dt_nascimento = Column(String, nullable=True)
    cidadao_cns = Column(String, nullable=True)
    cidadao_nome = Column(String, nullable=True)
    cidadao_nome_social = Column(String, nullable=True)
    cidadao_sexo = Column(String, nullable=True)
    dt_nascimento = Column(DATE, nullable=True)
    cidadao_faixa_etaria = Column(String, nullable=True)
    estabelecimento_cnes_atendimento = Column(String, nullable=True)
    estabelecimento_cnes_cadastro = Column(String, nullable=True)
    estabelecimento_nome_atendimento = Column(String, nullable=True)
    estabelecimento_nome_cadastro = Column(String, nullable=True)
    equipe_ine_atendimento = Column(String, nullable=True)
    equipe_ine_cadastro = Column(String, nullable=True)
    equipe_nome_atendimento = Column(String, nullable=True)
    equipe_nome_cadastro = Column(String, nullable=True)
    acs_nome_cadastro = Column(String, nullable=True)
    acs_nome_visita = Column(String, nullable=True)
    possui_hipertensao_autorreferida = Column(BOOLEAN, nullable=True)
    possui_hipertensao_diagnosticada = Column(BOOLEAN, nullable=True)
    apenas_autorreferida = Column(Integer, nullable=True)
    diagnostico_clinico = Column(Integer, nullable=True)
    data_ultimo_cadastro = Column(DATE, nullable=True)
    dt_ultima_consulta = Column(DATE, nullable=True)
    se_faleceu = Column(Integer, nullable=True)
    se_mudou = Column(Integer, nullable=True)
    criacao_data = Column(TIMESTAMP, nullable=True)
    atualizacao_data = Column(TIMESTAMP, nullable=True)
    dt_registro_producao_mais_recente = Column(DATE, nullable=True)
    __table_args__ = {"schema": "impulso_previne_dados_nominais"}


# Base.metadata.create_all(db.engine)
