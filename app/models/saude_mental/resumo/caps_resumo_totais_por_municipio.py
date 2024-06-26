from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import NUMERIC, VARCHAR
from app.models.saude_mental.schema import SCHEMA_SAUDE_MENTAL

from app.models import db

Base = db.Base_saude_mental


class ResumoTotaisPorMunicipio(Base):
    __tablename__ = "caps_resumo_totais_por_municipio"
    id = Column(Text, primary_key=True)
    unidade_geografica_id_sus = Column(VARCHAR)
    tornandose_inativos = Column(NUMERIC)
    dif_tornandose_inativos_anterior = Column(NUMERIC)
    ativos_mes = Column(NUMERIC)
    dif_ativos_mes_anterior = Column(NUMERIC)
    periodo_ativos = Column(Text)
    nome_mes_ativos = Column(Text)
    usuarios_novos = Column(NUMERIC)
    dif_usuarios_novos_anterior = Column(NUMERIC)
    periodo_novos = Column(Text)
    nome_mes_novos = Column(Text)
    usuarios_coorte_nao_aderiram = Column(NUMERIC)
    maior_taxa_estabelecimento_nao_adesao = Column(VARCHAR)
    maior_taxa_nao_adesao = Column(NUMERIC)
    predominio_sexo = Column(Text)
    predominio_faixa_etaria = Column(Text)
    predominio_condicao_grupo_descricao_curta_cid10 = Column(Text)
    a_partir_do_mes = Column(Text)
    a_partir_do_ano = Column(Text)
    ate_mes = Column(Text)
    ate_ano = Column(Text)
    perc_apenas_atendimentos_individuais = Column(NUMERIC)
    dif_perc_apenas_atendimentos_individuais = Column(NUMERIC)
    maior_taxa_atendimentos_individuais = Column(NUMERIC)
    maior_taxa_estabelecimento_atendimentos_individuais = Column(VARCHAR)
    periodo_atendimentos_individuais = Column(Text)
    nome_mes_atendimentos_individuais = Column(Text)
    sexo_atendimentos_individuais = Column(Text)
    faixa_etaria_atendimentos_individuais = Column(Text)
    cid_grupo_atendimentos_individuais = Column(Text)
    usuarios_cid_atendimentos_individuais = Column(NUMERIC)
    periodo_atendimentos_individuais_perfil = Column(Text)
    nome_mes_atendimentos_individuais_perfil = Column(Text)
    maior_taxa_procedimentos_por_usuario = Column(NUMERIC)
    maior_taxa_estabelecimento_procedimentos_por_usuario = Column(VARCHAR)
    procedimentos_por_usuario = Column(NUMERIC)
    dif_procedimentos_por_usuario_anterior_perc = Column(NUMERIC)
    periodo_proced_usuario = Column(Text)
    nome_mes_proced_usuario = Column(Text)
    tempo_servico_maior_taxa = Column(Text)
    maior_taxa_procedimentos_tempo_servico = Column(NUMERIC)
    procedimentos_registrados_total = Column(NUMERIC)
    dif_procedimentos_registrados_total_anterior = Column(NUMERIC)
    procedimentos_registrados_bpa = Column(NUMERIC)
    dif_procedimentos_registrados_bpa_anterior = Column(NUMERIC)
    procedimentos_registrados_raas = Column(NUMERIC)
    dif_procedimentos_registrados_raas_anterior = Column(NUMERIC)
    periodo_procedimentos_hora = Column(Text)
    nome_mes_procedimentos_hora = Column(Text)
    __table_args__ = {"schema": SCHEMA_SAUDE_MENTAL}
