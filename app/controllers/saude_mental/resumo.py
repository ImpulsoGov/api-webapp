from fastapi import HTTPException
from sqlalchemy import exc

from app.models.db import session
from app.models.saude_mental.resumo import ResumoTotaisPorMunicipio


def obter_resumo_totais_por_id_sus(municipio_id_sus: str):
    try:
        resumo_municipio = (
            session.query(ResumoTotaisPorMunicipio)
            .filter_by(unidade_geografica_id_sus=municipio_id_sus)
            .first()
        )

        if resumo_municipio is None:
            raise HTTPException(
                status_code=404,
                detail=("Resumo de totais do município não encontrado"),
            )

        return resumo_municipio
    except HTTPException as error:
        raise error
    except (exc.SQLAlchemyError, Exception) as error:
        print({"error": str(error)})
        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
