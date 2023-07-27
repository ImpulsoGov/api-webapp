from app.models import DB_PRODUCAO
from app.models.impulso_previne_publico.capitacao_ponderada_cadastros_por_equipes import CadastrosEquipes
from app.models.impulso_previne_publico.capitacao_ponderada_contagem_equipes import CadastrosEquipeContagem
from app.models.impulso_previne_publico.capitacao_ponderada_validacao_por_producao import ValidacaoProducao 
from app.models.impulso_previne_publico.capitacao_ponderada_validacao_por_producao_por_aplicacao import ValidacaoProducaoAplicacao 

from cachetools import TTLCache

session = DB_PRODUCAO.session

cache_capitacao_ponderada_cadastros_por_equipe = TTLCache(maxsize=38, ttl=24*60*60)
def capitacao_ponderada_cadastros_por_equipe(
        municipio_uf:str,
        ):
    result = capitacao_ponderada_cadastros_por_equipe.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                CadastrosEquipes
                ).filter_by(
                municipio_uf=municipio_uf,

                ).with_entities(
                    CadastrosEquipes.equipe_id_ine,
                    CadastrosEquipes.equipe_nome,
                    CadastrosEquipes.equipe_status,
                    CadastrosEquipes.data_inicio,
                    CadastrosEquipes.cadastro_total,
                    CadastrosEquipes.cadastros_com_pontuacao,
                    CadastrosEquipes.municipio_ultimo_parametro,
                    CadastrosEquipes.municipio_ultimo_parametro
                ).order_by(
                    CadastrosEquipes.data_inicio
                ).all()
            capitacao_ponderada_cadastros_por_equipe[municipio_uf] = result
            return result
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error


cache_capitacao_ponderada_cadastros_status = TTLCache(maxsize=38, ttl=24*60*60)
def capitacao_ponderada_cadastros_status( municipio_uf:str):
    result = capitacao_ponderada_cadastros_status.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                CadastrosEquipeContagem).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
                    CadastrosEquipeContagem.equipe_status_tipo,
                    CadastrosEquipeContagem.equipe_status
                ).order_by(
                    CadastrosEquipeContagem.equipe_status_tipo
                ).all()
            capitacao_ponderada_cadastros_status[municipio_uf] = result
            return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

cache_capitacao_ponderada_validacao_por_producao = TTLCache(maxsize=38, ttl=24*60*60)
def capitacao_ponderada_validacao_por_producao(
        municipio_uf:str,
        ):
    result = capitacao_ponderada_validacao_por_producao.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                ValidacaoProducao
                ).filter_by(
                municipio_uf=municipio_uf,

                ).with_entities(
                    ValidacaoProducao.equipe_id_ine,
                    ValidacaoProducao.equipe_nome,
                    ValidacaoProducao.periodo_data_inicio,
                    ValidacaoProducao.validacao_nome,
                    ValidacaoProducao.validacao_quantidade,
                    ValidacaoProducao.recomendacao
                ).order_by(
                    ValidacaoProducao.validacao_nome
                ).all()
            capitacao_ponderada_validacao_por_producao[municipio_uf] = result
            return result
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error
    

cache_capitacao_ponderada_validacao_por_producao_por_aplicacao = TTLCache(maxsize=38, ttl=24*60*60)
def capitacao_ponderada_validacao_por_producao_por_aplicacao(
        municipio_uf:str,
        ):
    result = capitacao_ponderada_validacao_por_producao_por_aplicacao.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                ValidacaoProducaoAplicacao
                ).filter_by(
                municipio_uf=municipio_uf,

                ).with_entities(
                    ValidacaoProducaoAplicacao.equipe_id_ine,
                    ValidacaoProducaoAplicacao.equipe_nome,
                    ValidacaoProducaoAplicacao.cnes_id,
                    ValidacaoProducaoAplicacao.cnes_nome,
                    ValidacaoProducaoAplicacao.validacao_aplicacao,
                    ValidacaoProducaoAplicacao.validacao_nome,
                    ValidacaoProducaoAplicacao.validacao_quantidade,
                    ValidacaoProducaoAplicacao.periodo_data_inicio
                ).order_by(
                    ValidacaoProducaoAplicacao.periodo_data_inicio
                ).all()
            capitacao_ponderada_validacao_por_producao_por_aplicacao[municipio_uf] = result
            return result
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error


