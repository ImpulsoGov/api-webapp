from fastapi import APIRouter
from typing import Optional
from controllers import municipios
router = APIRouter()

@router.get("/suporte/municipios/")
async def consulta(id_sus: Optional[str] = None, nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None ):
    res = municipios.consulta_municipio(id_sus,nome,estado_sigla,estado_nome)
    return res

