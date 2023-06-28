from fastapi import APIRouter

from app.controllers.saude_mental.resumo import obter_resumo_totais_por_id_sus

router = APIRouter()


@router.get("/saude-mental/resumo/caps")
async def obter_resumo_por_municipio_id_sus(
    municipio_id_sus: str,
):
    return obter_resumo_totais_por_id_sus(municipio_id_sus=municipio_id_sus)
