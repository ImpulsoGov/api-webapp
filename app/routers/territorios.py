from fastapi import APIRouter, Depends,Form
from typing import Optional,List
from app.controllers import territorios
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from app.models.usuarios import Usuario
import pandas as pd

router = APIRouter()

fake_items_db = [{"id": 1, "item_name": "Foo", "classe": 0},
                {"id": 2, "item_name": "Bar", "classe": 0}, 
                {"id": 3, "item_name": "Baz", "classe": 0}]

@router.get("/territorios/teste")
async def read_item(skip: int = 0, limit: int = 10):
    itens = fake_items_db[skip : skip + limit]
    return itens

@router.get("/territorios/teste/{item_id}")
async def read_item(item_id: int, skip: int = 0, limit: int = 10):
    itens = fake_items_db[skip : skip + limit]
    id = item_id
    df = list(filter(lambda x: x['id'] == item_id, itens))
    return df

@router.get("/territorios/estabelecimentos")
async def busca_estabelecimento(cnes: Optional[str] = None):
    res = territorios.busca_estabelecimento(cnes)
    return res

@router.put("/territorios/estabelecimentos/{cnes}")
async def atualiza_estabelecimento(cnes, lat, long):
    res = territorios.atualiza_estabelecimento(cnes, lat, long)
    return res