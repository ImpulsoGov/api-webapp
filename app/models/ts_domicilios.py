from sqlalchemy import DATE, Column, ForeignKey, Integer, String

from app.models import db

Base = db.Base


class Domicilios(Base):
    __tablename__ = "domicilios"
    id = Column(String, primary_key=True)
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
    logradouro_tipo = Column(String)
    logradouro_nome = Column(String)
    logradouro_numero = Column(String)
    logradouro_complemento = Column(String)
    bairro = Column(String)
    cep = Column(String)
    uf = Column(String)
    endereco = Column(String)
    endereco_georeferenciado = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    coordenadas_processadas = Column(String)
    quantidade_moradores = Column(String)
    numero_comodos = Column(String)
    tipo_imovel = Column(String)
    tipo_situacao_moradia = Column(String)
    tipo_localizacao = Column(String)
    tipo_domicilio = Column(String)
    tipo_posse_terra = Column(String)
    tipo_acesso_domicilio = Column(String)
    tipo_material_parede = Column(String)
    tipo_abastecimento_agua = Column(String)
    tipo_tratamento_agua = Column(String)
    tipo_escoamento_sanitario = Column(String)
    tipo_destino_lixo = Column(String)
    dispoe_energia = Column(String)
    ponto_referencia = Column(String)
    telefone_residencia = Column(String)
    telefone_contato = Column(String)
    instituicao_telefone = Column(String)
    __table_args__ = {"schema": "territorios"}
