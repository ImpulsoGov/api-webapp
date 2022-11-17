from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from app.models import db
Base = db.Base

class Individuos(Base):
    __tablename__ = 'tapirai_355350_fat_cadastro_individual'
    id = Column(String)
    familia_id = Column(String)
    domicilio_id = Column(String)
    id_origem = Column(String)
    ibge = Column(String)
    data_registro = Column(String)
    unidade_saude_cnes = Column(String)
    unidade_saude_nome = Column(String)
    equipe_ine = Column(String)
    equipe_nome = Column(String)
    cbo_cadastrante_numero = Column(String)
    cbo_cadastrante_nome = Column(String)
    profissional_cadastrante_cns = Column(String)
    profissional_cadastrante_nome = Column(String)
    micro_area = Column(String)
    cpf = Column(String)
    cns = Column(String)
    data_nascimento = Column(String)
    sexo = Column(String)
    nome = Column(String)
    nome_social = Column(String)
    nome_mae = Column(String)
    nome_pai = Column(String)
    responsavel_cpf = Column(String)
    responsavel_cns = Column(String)
    numero_celular = Column(String)
    email = Column(String)
    raca_cor = Column(String)
    etnia = Column(String)
    identidade_genero = Column(String)
    faixa_etaria = Column(String)
    tipo_parentesco_com_responsavel_familia = Column(String)
    escolaridade = Column(String)
    situacao_trabalho = Column(String)
    orientacao_sexual = Column(String)
    condicao_peso = Column(String)
    tempo_morador_rua = Column(String)
    hipertensao = Column(String)
    diabetes = Column(String)
    insuficiencia_renal = Column(String)
    hiv = Column(String)
    acamado = Column(String)
    deficiencia = Column(String)
    uso_alcool_drogas = Column(String)
    bolsa_familia = Column(String)
    responsavel = Column(String)
    __table_args__ = {'schema': 'territorios'}