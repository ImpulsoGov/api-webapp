from app.models import db
from app.models.impulso_previne_publico import indicadores

session = db.session
Indicadores = indicadores.Indicadores

from fastapi.responses import HTMLResponse


def consulta_indicadores(
    id_sus,
    municipio_nome,
    estado_sigla,
    estado_nome,
    indicadores_nome,
    indicadores_parametros_id,
):
    if estado_sigla != None:
        estado_sigla = estado_sigla.upper()
    params = {
        "municipio_id_sus": id_sus,
        "municipio_nome_normalizado": municipio_nome,
        "estado_sigla": estado_sigla,
        "estado_nome_normalizado": estado_nome,
        "indicadores_nome_normalizado": indicadores_nome,
        "indicadores_parametros_id": indicadores_parametros_id,
    }
    params = {
        coluna: parametro for coluna, parametro in params.items() if parametro != None
    }
    if len(params) == 0:
        return session.query(Indicadores).all()
    else:
        return session.query(Indicadores).filter_by(**params).all()
