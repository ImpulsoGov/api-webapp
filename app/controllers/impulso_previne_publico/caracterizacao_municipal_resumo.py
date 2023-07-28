from app.models import DB_PRODUCAO
from app.models.impulso_previne_publico.caracterizacao_municipal_resumo import CaracterizacaoMunicipalResumo

from cachetools import TTLCache

session = DB_PRODUCAO.session

cache_caracterizacao_municipal_resumo = TTLCache(maxsize=38, ttl=24*60*60)
def caracterizacao_municipal_resumo(municipio_uf:str):
    result = cache_caracterizacao_municipal_resumo.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                CaracterizacaoMunicipalResumo).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
                    CaracterizacaoMunicipalResumo.municipio_id_sus,
                    CaracterizacaoMunicipalResumo.municipio_uf,
                    CaracterizacaoMunicipalResumo.municipio_tipologia,
                    CaracterizacaoMunicipalResumo.municipio_populacao_2020,
                    CaracterizacaoMunicipalResumo.equipe_total,
                    CaracterizacaoMunicipalResumo.cadastro_parametro,
                    CaracterizacaoMunicipalResumo.cadastros_equipes_validas,
                    CaracterizacaoMunicipalResumo.cadastros_equipes_validas_com_ponderacao,
                ).order_by(
                    CaracterizacaoMunicipalResumo.municipio_uf
                ).all()
            cache_caracterizacao_municipal_resumo[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error



