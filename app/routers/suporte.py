from fastapi import APIRouter, Depends,Form
from typing import Optional,List
from app.controllers import municipios,auth,cadastro_usuarios,recuperação_senha
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class Municipio(BaseModel):
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

@router.get("/suporte/municipios/", response_model=List[Municipio])
async def consulta_municipio(id_sus: Optional[str] = None, municipio_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None):
    res = municipios.consulta_municipio(id_sus,municipio_nome,estado_sigla,estado_nome)
    return res

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

@router.post("/suporte/usuarios/token", response_model=Token )
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.login(form_data)

class Mensagem(BaseModel):
    erros : Optional[List] = None
    mensagem : Optional[str] = None

@router.post("/suporte/usuarios/cadastro")
async def cadastro(
    nome: str = Form(...),
    mail: str = Form(...),
    senha: str = Form(...),
    cpf: str = Form(...)
    ):
    return cadastro_usuarios.cadastrar(nome,mail,senha,cpf)

@router.post("/suporte/usuarios/solicitar-recuperacao")
async def solicita_recuperacao(mail: str = Form(...)):
    return recuperação_senha.solicita_recuperacao(mail)

@router.post("/suporte/usuarios/alterar-senha", response_model=Mensagem)
async def solicita_recuperacao(mail: str = Form(...),codigo: str = Form(...),senha: str = Form(...)):
    return recuperação_senha.recuperar(mail,codigo,senha)