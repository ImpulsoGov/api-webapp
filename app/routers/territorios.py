from fastapi import APIRouter, Depends,Form
from typing import Optional,List
from app.controllers import territorios
from fastapi.security import OAuth2PasswordRequestForm
import pandas as pd

router = APIRouter()

@router.get("/territorios/estabelecimentos")
async def busca_estabelecimento(cnes: Optional[str] = None):
    res = territorios.busca_estabelecimento(cnes)
    return res

@router.put("/territorios/estabelecimentos/{cnes}")
async def atualiza_estabelecimento(cnes, lat, long):
    res = territorios.atualiza_estabelecimento(cnes, lat, long)
    return res

@router.get("/territorios/profissionais")
async def busca_profissionais(cns: Optional[str] = None):
    res = territorios.busca_profissionais(cns)
    return res

@router.get("/territorios/domicilios")
async def busca_domicilios(id: Optional[str] = None):
    res = territorios.busca_domicilios(id)
    return res

@router.get("/territorios/individuos")
async def busca_individuos(domicilio_id: Optional[str] = None):
    res = territorios.busca_individuos(domicilio_id)
    return res

@router.put("/territorios/domicilios/{id}")
async def atualiza_domicilio(id, lat, long):
    res = territorios.atualiza_domicilio(id, lat, long)
    return res