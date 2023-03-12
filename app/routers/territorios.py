from typing import List, Optional

import pandas as pd
from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from app.controllers import territorios

router = APIRouter()

@router.get("/territorios/estabelecimentos")
async def busca_estabelecimentos(ibge: Optional[str] = None, cnes: Optional[str] = None):
    res = territorios.busca_estabelecimentos(ibge, cnes)
    return res

@router.put("/territorios/estabelecimentos/{cnes}")
async def atualiza_estabelecimento(cnes, lat, long):
    res = territorios.atualiza_estabelecimento(cnes, lat, long)
    return res

@router.get("/territorios/profissionais")
async def busca_profissionais(ibge: Optional[str] = None, cnes: Optional[str] = None, cns: Optional[str] = None):
    res = territorios.busca_profissionais(ibge, cns)
    return res

@router.get("/territorios/domicilios")
async def busca_domicilios(ibge: Optional[str] = None, id: Optional[str] = None):
    res = territorios.busca_domicilios(ibge, id)
    return res

@router.get("/territorios/individuos")
async def busca_individuos(ibge: Optional[str] = None, domicilio_id: Optional[str] = None):
    res = territorios.busca_individuos(ibge, domicilio_id)
    return res

@router.put("/territorios/domicilios/{id}")
async def atualiza_domicilio(id, lat, long):
    res = territorios.atualiza_domicilio(id, lat, long)
    return res