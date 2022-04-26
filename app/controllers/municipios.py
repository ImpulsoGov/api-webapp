from app.models import db,municipios
session = db.session
Municipios = municipios.Municipios
from .response_pages.municipios import html as response_municipios
from fastapi.responses import HTMLResponse

def consulta_municipio(id_sus,municipio_nome,estado_sigla,estado_nome):
    if estado_sigla != None : estado_sigla=estado_sigla.upper()
    params_full = {
        "municipio_id_sus":id_sus,
        "municipio_nome_normalizado":municipio_nome,
        "estado_sigla":estado_sigla,
        "estado_nome_normalizado":estado_nome,
    }
    params = {coluna:parametro for coluna, parametro in params_full.items() if parametro!=None}
    if len(params)==0: 
        query = session.query(Municipios)
        res = query.all()
        return res
    elif params_full["estado_sigla"] != None or params_full["estado_nome_normalizado"] != None:
        query = session.query(Municipios).with_entities(
                    Municipios.id,
                    Municipios.estado_sigla,
                    Municipios.estado_nome,
                    Municipios.estado_id_ibge,
                    Municipios.municipio_eh_capital,
                    Municipios.municipio_id_sus,
                    Municipios.municipio_id_ibge,
                    Municipios.municipio_nome,
                    Municipios.municipio_nome_normalizado
        ).filter_by(**params)
        res = query.all()
        return res
    else:
        query = session.query(Municipios).filter_by(**params)
        res = query.all()
        return res
