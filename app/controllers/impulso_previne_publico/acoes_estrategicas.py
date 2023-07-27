from app.models import DB_PRODUCAO
from app.models.impulso_previne_publico.acoes_estrategicas_repasses import AcoesEstrategicasRepasses
from app.models.impulso_previne_publico.acoes_estrategicas_vigente_agrupada import AcoesEstrategicasVigenteAgrupada

from cachetools import TTLCache

session = DB_PRODUCAO.session

cache_acoes_estrategicas_repasses = TTLCache(maxsize=38, ttl=24*60*60)
def acoes_estrategicas_repasses(municipio_uf):
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                    AcoesEstrategicasRepasses
                    ).filter_by(
                    municipio_uf=municipio_uf
                    ).with_entities(
                        AcoesEstrategicasRepasses.acao_nome,
                        AcoesEstrategicasRepasses.pagamento_total
                    ).order_by(
                        AcoesEstrategicasRepasses.data_inicio
                    ).all()
            cache_acoes_estrategicas_repasses[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros": [error]})
        return error


cache_acao_estrategica_agrupada = TTLCache(maxsize=38, ttl=24*60*60)
def acoes_estrategicas_vigente_agrupada(municipio_uf):
    result = cache_acao_estrategica_agrupada.get(municipio_uf)
    try:
        if result is None:
            result = DB_PRODUCAO.session.query(
                AcoesEstrategicasVigenteAgrupada).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
                    AcoesEstrategicasVigenteAgrupada.acao_nome,
                    AcoesEstrategicasVigenteAgrupada.nivel_repasse,
                    AcoesEstrategicasVigenteAgrupada.periodicidade,
                    AcoesEstrategicasVigenteAgrupada.requisitos
                ).order_by(
                    AcoesEstrategicasVigenteAgrupada.acao_nome
                ).all()
            cache_acao_estrategica_agrupada[municipio_uf] = result
        return result
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error



