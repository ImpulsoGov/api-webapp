from app.models import db
from app.models.impulso_previne_publico import (
    indicadores_municipios_equipes_homologadas,
)

session = db.session
IndicadoresMunicipiosEquipesHomologadas = (
    indicadores_municipios_equipes_homologadas.IndicadoresMunicipiosEquipesHomologadas
)


def consultar_indicadores_municipios_equipes_homologadas(municipio_uf=None):
    try:
        return (
            session.query(IndicadoresMunicipiosEquipesHomologadas)
            .filter_by(municipio_uf=municipio_uf)
            .with_entities(
                IndicadoresMunicipiosEquipesHomologadas.periodo_data_inicio,
                IndicadoresMunicipiosEquipesHomologadas.periodo_data_fim,
                IndicadoresMunicipiosEquipesHomologadas.periodo_codigo,
                IndicadoresMunicipiosEquipesHomologadas.municipio_id_ibge,
                IndicadoresMunicipiosEquipesHomologadas.municipio_id_sus,
                IndicadoresMunicipiosEquipesHomologadas.municipio_nome,
                IndicadoresMunicipiosEquipesHomologadas.municipio_uf,
                IndicadoresMunicipiosEquipesHomologadas.indicador_ordem,
                IndicadoresMunicipiosEquipesHomologadas.indicador_nome,
                IndicadoresMunicipiosEquipesHomologadas.indicador_meta,
                IndicadoresMunicipiosEquipesHomologadas.indicador_peso,
                IndicadoresMunicipiosEquipesHomologadas.indicador_numerador,
                IndicadoresMunicipiosEquipesHomologadas.indicador_denominador_informado,
                IndicadoresMunicipiosEquipesHomologadas.indicador_denominador_estimado,
                IndicadoresMunicipiosEquipesHomologadas.indicador_denominador_utilizado,
                IndicadoresMunicipiosEquipesHomologadas.indicador_resultado,
            )
            .all()
        )
    except Exception as error:
        print({"erros": [error]})
        return error
