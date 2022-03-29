from fastapi import APIRouter, Depends
from typing import Optional
from controllers import municipios,auth
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class Municipios(BaseModel):
    id : int
    estado_sigla : str
    estado_nome : str
    estado_nome_normalizado : str
    estado_id_ibge : str
    municipio_eh_capital : bool
    municipio_id_sus : str
    municipio_id_ibge : str
    municipio_nome : str
    municipio_nome_normalizado : str
    slug : str
    ddd  : int
    municipio_comarca_id_judiciario : str
    macrorregiao_nome : str
    macrorregiao_id_ibge : str
    mesorregiao_id_ibge : str
    mesorregiao_nome : str
    microrregiao_id_ibge : str
    microrregiao_nome  : str
    regiao_saude_id : str
    regiao_saude_nome  : str
    regiao_imediata_id_ibge : str
    regiao_imediata_nome  : str
    regiao_intermediaria_id_ibge : str
    regiao_intermediaria_nome : str

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

@router.get("/suporte/municipios/", response_model=Municipios)
async def consulta_municipio(id_sus: Optional[str] = None, municipio_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None, current_user: User =Depends(auth.get_current_user) ):
    res = municipios.consulta_municipio(id_sus,municipio_nome,estado_sigla,estado_nome)
    return res[0]

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

@router.post("/suporte/usuarios/token", response_model=Token )
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return auth.login(form_data)

    
