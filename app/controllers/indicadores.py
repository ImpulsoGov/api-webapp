from models import db,indicadores
session = db.session
Indicadores = indicadores.Indicadores

from .response_pages.indicadores import html as response_indicadores
from fastapi.responses import HTMLResponse

def consulta_indicadores(id_sus,municipio_nome,estado_sigla,estado_nome,indicadores_nome,indicadores_parametros_id):
    if estado_sigla != None : estado_sigla=estado_sigla.upper()
    params = {
        "municipio_id_sus":id_sus,
        "municipio_nome_normalizado":municipio_nome,
        "estado_sigla":estado_sigla,
        "estado_nome_normalizado":estado_nome,
        "indicadores_nome_normalizado":indicadores_nome,
        "indicadores_parametros_id":indicadores_parametros_id
    }
    params = {coluna:parametro for coluna, parametro in params.items() if parametro!=None}
    if len(params)==0: 
        return HTMLResponse(content=response_indicadores(), status_code=200)
    else:
        query = session.query(Indicadores).filter_by(**params)
        res = query.all()
        return res