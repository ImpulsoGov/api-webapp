from app.models import db,indicadores_municipios_equipes_homologadas
session = db.session
IndicadoresMuEquipesHomologadas = indicadores_municipios_equipes_homologadas.IndicadoresMuEquipesHomologadas

from .response_pages.indicadores import html as response_indicadores
from fastapi.responses import HTMLResponse

def consulta_indicadores_municipios_equipes_homologadas(id_sus,municipio_nome,municipio_uf,indicador_nome,indicador_resultado):
    if estado_sigla != None : estado_sigla=estado_sigla.upper()
    params = {
        "municipio_id_sus":id_sus,
        "municipio_nome":municipio_nome,
        "municipio_uf":municipio_uf,
        "indicador_nome":indicador_nome,
        "indicador_resultado":indicador_resultado
    
    }
    params = {coluna:parametro for coluna, parametro in params.items() if parametro!=None}
    if len(params)==0: 
        return session.query(IndicadoresMuEquipesHomologadas).all()
    else:
        return session.query(IndicadoresMuEquipesHomologadas).filter_by(**params).all()