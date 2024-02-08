from app.models import db
from app.models.impulso_previne_publico.caracterizacao_municipal_resumo import (
    CaracterizacaoMunicipalResumo,
)

session = db.session


def caracterizacao_municipal_resumo(municipio_uf: str):
    try:
        return (
            session.query(CaracterizacaoMunicipalResumo)
            .filter_by(municipio_uf=municipio_uf)
            .with_entities(
                CaracterizacaoMunicipalResumo.municipio_id_sus,
                CaracterizacaoMunicipalResumo.municipio_uf,
                CaracterizacaoMunicipalResumo.municipio_tipologia,
                CaracterizacaoMunicipalResumo.municipio_populacao_2020,
                CaracterizacaoMunicipalResumo.equipe_total,
                CaracterizacaoMunicipalResumo.cadastro_parametro,
                CaracterizacaoMunicipalResumo.cadastros_equipes_validas,
                CaracterizacaoMunicipalResumo.cadastros_equipes_validas_com_ponderacao,
            )
            .all()
        )
    except Exception as error:
        print({"erros": [error]})
        return error
