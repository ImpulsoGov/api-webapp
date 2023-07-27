from fastapi import APIRouter,Depends
from app.controllers.impulso_previne_publico.caracterizacao_municipal_resumo import (
    caracterizacao_municipal_resumo
)
from app.controllers.usuarios.auth import Usuario, get_current_user

router = APIRouter()

@router.get("/impulsoprevine/caracterizacao_municipal/resumo")
async def obter_caracterizacao_municipal_resumo(
    municipio_uf: str,
    username: Usuario = Depends(get_current_user)
):
    return caracterizacao_municipal_resumo(
        municipio_uf=municipio_uf
    )