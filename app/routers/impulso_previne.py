from fastapi import APIRouter
from typing import Optional, List
from controllers import indicadores
from pydantic import BaseModel
router = APIRouter()

class Indicador(BaseModel):
    id : int
    estado_sigla : str
    estado_nome : str
    estado_nome_normalizado : str
    municipio_id_sus : str
    municipio_nome : str
    municipio_nome_normalizado : str
    indicadores_parametros_id : int
    indicadores_parametros_nome : str
    indicadores_parametros_nome_normalizado : str
    indicadores_parametros_ordem : int
    indicadores_parametros_meta : float
    indicadores_parametros_peso : float
    indicadores_resultados_porcentagem : float
    diff_numerador_para_meta : int

    class Config:
        orm_mode = True


@router.get("/impulsoprevine/indicadores/", response_model=List[Indicador])
async def consulta_indicadores(indicadores_parametros_id: Optional[str] = None, indicadores_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None, id_sus: Optional[str] = None, municipio_nome: Optional[str] = None):
    res = indicadores.consulta_indicadores(id_sus,municipio_nome,estado_sigla,estado_nome,indicadores_nome,indicadores_parametros_id)
    return res