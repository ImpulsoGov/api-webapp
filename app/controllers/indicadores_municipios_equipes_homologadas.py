from app.models import db,indicadores_municipios_equipes_homologadas
session = db.session
IndicadoresMunicipiosEquipesHomologadas = indicadores_municipios_equipes_homologadas.IndicadoresMunicipiosEquipesHomologadas

def consultar_indicadores_municipios_equipes_homologadas( municipio_uf=None):
    if municipio_uf :
        return session.query(IndicadoresMunicipiosEquipesHomologadas).filter_by(municipio_uf=municipio_uf).all()
    else: 
        return session.query(IndicadoresMunicipiosEquipesHomologadas).all()