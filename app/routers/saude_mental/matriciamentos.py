from fastapi import APIRouter

from app.controllers.saude_mental.matriciamentos import (
    obter_matriciamentos_caps_ultimo_ano_por_id_sus,
    obter_matriciamentos_municipio_ultimo_ano_por_id_sus,
)

router = APIRouter()


@router.get("/saude-mental/matriciamentos/caps")
async def obter_matriciamentos_caps(
    municipio_id_sus: str,
):
    return obter_matriciamentos_caps_ultimo_ano_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/matriciamentos/municipio")
async def obter_matriciamentos_municipio(
    municipio_id_sus: str,
):
    return obter_matriciamentos_municipio_ultimo_ano_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )
