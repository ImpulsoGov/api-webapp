from fastapi import APIRouter,Request
from controllers import municipios
router = APIRouter()

@router.get("/suporte/municipios_id")
async def consulta(id_sus: str):
    res = municipios.consulta_id(id_sus)
    return res

@router.get("/suporte/municipios")
async def consulta(uf_municipio: str):
    res = municipios.consulta_slug(uf_municipio)
    return res