from app.models import db
from app.models.impulso_previne_publico.acoes_estrategicas_repasses import AcoesEstrategicasRepasses
from app.models.impulso_previne_publico.acoes_estrategicas_vigente_agrupada import AcoesEstrategicasVigenteAgrupada

session = db.session
from cachetools import TTLCache

cache_acoes_estrategicas_repasses = TTLCache(maxsize=38, ttl=24*60*60)
def acoes_estrategicas_repasses(municipio_uf):
    result = cache_acoes_estrategicas_repasses.get(municipio_uf)
    try:
        if result is None:
            result = session.query(
                    AcoesEstrategicasRepasses
                    ).filter_by(
                    municipio_uf=municipio_uf
                    ).with_entities(
                        AcoesEstrategicasRepasses.acao_nome,
                        AcoesEstrategicasRepasses.pagamento_total,
                        AcoesEstrategicasRepasses.codigo
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
            result = session.query(
                AcoesEstrategicasVigenteAgrupada).filter_by(
                municipio_uf=municipio_uf
                ).with_entities(
                    AcoesEstrategicasVigenteAgrupada.acao_nome,
                    AcoesEstrategicasVigenteAgrupada.acumulado_12meses,
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



