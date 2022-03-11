from fastapi import APIRouter
from controllers import t
router = APIRouter()

@router.get("/rota1/")
async def hello():
    return {"message":"Olha uma nova rota da API esta rodando :)"}

@router.get("/rota2/{item}")
async def hello(item):
    return {"message":item}
    
@router.get("/rota3/{nome}/{sobrenome}")
async def hello(nome,sobrenome):
    res = t.consulta(nome,sobrenome)
    return {"message":res}

