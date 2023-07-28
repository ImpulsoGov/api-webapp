from typing import List, Optional

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.controllers.impulso_previne_publico import (
    indicadores,
    indicadores_desempenho_score_equipes_validas,
    indicadores_municipios_equipes_homologadas,
)

router = APIRouter()


class Indicador(BaseModel):
    id: int
    estado_sigla: str
    estado_nome: str
    estado_nome_normalizado: str
    municipio_id_sus: str
    municipio_nome: str
    municipio_nome_normalizado: str
    indicadores_parametros_id: int
    indicadores_parametros_nome: str
    indicadores_parametros_nome_normalizado: str
    indicadores_parametros_ordem: int
    indicadores_parametros_meta: float
    indicadores_parametros_peso: float
    indicadores_resultados_porcentagem: float
    diff_numerador_para_meta: int

    class Config:
        orm_mode = True

@router.get("/impulsoprevine/indicadores/resumo", response_model=List[Indicador])
async def consulta_indicadores(
    indicadores_parametros_id: Optional[str] = None,
    indicadores_nome: Optional[str] = None,
    estado_sigla: Optional[str] = None,
    estado_nome: Optional[str] = None,
    id_sus: Optional[str] = None,
    municipio_nome: Optional[str] = None,
):
    res = indicadores.consulta_indicadores(
        id_sus,
        municipio_nome,
        estado_sigla,
        estado_nome,
        indicadores_nome,
        indicadores_parametros_id,
    )
    return res


@router.get("/impulsoprevine/indicadores/municipios_equipes_homologadas")
async def consultar_indicadores_equipes_homologadas_municipios(municipio_uf: str):
    res = indicadores_municipios_equipes_homologadas.consultar_indicadores_municipios_equipes_homologadas(
        municipio_uf
    )
    return res


@router.get("/impulsoprevine/indicadores/desempenho_score_equipes_validas")
async def consultar_indicadores_desempenho(municipio_uf: str):
    res = indicadores_desempenho_score_equipes_validas.consultar_indicadores_desempenho(
        municipio_uf
    )
    return res