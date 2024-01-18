from app.models import db
from app.models.impulso_previne_publico import (
    indicadores_desempenho_score_equipes_validas,
)

session = db.session
IndicadoresDesempenho = (
    indicadores_desempenho_score_equipes_validas.IndicadoresDesempenho
)


def consultar_indicadores_desempenho(municipio_uf):
    try:
        return (
            session.query(IndicadoresDesempenho)
            .filter_by(municipio_uf=municipio_uf)
            .all()
        )
    except Exception as error:
        print({"erros": [error]})
        return error
