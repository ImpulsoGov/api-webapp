from fastapi import APIRouter
from typing import Optional
from controllers import indicadores
router = APIRouter()

@router.get("/impulsoprevine/indicadores/")
async def consulta(indicadores_parametros_id: Optional[str] = None, indicadores_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None, id_sus: Optional[str] = None, municipio_nome: Optional[str] = None):
    res = indicadores.consulta_indicadores(id_sus,municipio_nome,estado_sigla,estado_nome,indicadores_nome,indicadores_parametros_id)
    return res