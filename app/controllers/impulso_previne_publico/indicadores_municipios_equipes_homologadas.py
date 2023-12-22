from app.models import db
from app.models.impulso_previne_publico import indicadores_municipios_equipes_homologadas
session = db.session
IndicadoresMunicipiosEquipesHomologadas = indicadores_municipios_equipes_homologadas.IndicadoresMunicipiosEquipesHomologadas

def consultar_indicadores_municipios_equipes_homologadas( municipio_uf=None):
    try: 
        return session.query(IndicadoresMunicipiosEquipesHomologadas).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error