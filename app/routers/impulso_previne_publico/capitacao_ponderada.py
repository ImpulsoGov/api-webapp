from fastapi import APIRouter, Depends
from app.controllers.impulso_previne_publico.capitacao_ponderada import (
    capitacao_ponderada_cadastros_por_equipe,
    capitacao_ponderada_cadastros_status,
    capitacao_ponderada_validacao_por_producao,
    capitacao_ponderada_validacao_por_producao_por_aplicacao
)
from app.controllers.usuarios.auth import Usuario, get_current_user

router = APIRouter()

@router.get("/impulsoprevine/capitacao-ponderada/cadastros-equipe")
async def obter_cadastros_por_equipe(
    municipio_uf: str, 
    username: Usuario = Depends(get_current_user)
):
    return capitacao_ponderada_cadastros_por_equipe(
        municipio_uf=municipio_uf,
    )

@router.get("/impulsoprevine/capitacao-ponderada/cadastros-contagem")
async def obter_contagem_cadastros_por_status(
    municipio_uf: str,
    username: Usuario = Depends(get_current_user)
):
    return capitacao_ponderada_cadastros_status(
        municipio_uf=municipio_uf
    )

@router.get("/impulsoprevine/capitacao-ponderada/validacao-producao")
async def obter_validacao_por_producao(
    municipio_uf: str,
    username: Usuario = Depends(get_current_user)
):
    return capitacao_ponderada_validacao_por_producao(
        municipio_uf=municipio_uf,
    )

@router.get("/impulsoprevine/capitacao-ponderada/validacao-producao-aplicacao")
async def obter_validacao_por_producao_por_aplicacao(
    municipio_uf: str,
    username: Usuario = Depends(get_current_user)
):
    return capitacao_ponderada_validacao_por_producao_por_aplicacao(
        municipio_uf=municipio_uf
    )