from app.models import db,indicadores_municipios_equipes_homologadas
from datetime import datetime
import json
session = db.session
IndicadoresMuEquipesHomologadas = indicadores_municipios_equipes_homologadas.IndicadoresMuEquipesHomologadas

def consulta_indicadores_municipios_equipes_homologadas( municipio_uf=None):
    if municipio_uf :
        return session.query(IndicadoresMuEquipesHomologadas).filter_by(municipio_uf=municipio_uf).all()
    else: 
        return session.query(IndicadoresMuEquipesHomologadas).all()