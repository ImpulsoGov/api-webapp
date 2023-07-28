from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.impulso_previne_publico.capitacao_ponderada import (
    capitacao_ponderada_cadastros_por_equipe,
    capitacao_ponderada_cadastros_status,
    capitacao_ponderada_validacao_por_producao,
    capitacao_ponderada_validacao_por_producao_por_aplicacao
)

router = APIRouter()

@router.get("/impulsoprevine/capitacao-ponderada/cadastros-equipe")
async def obter_cadastros_por_equipe(
    municipio_uf: str, 
    
):
    return capitacao_ponderada_cadastros_por_equipe(
        municipio_uf=municipio_uf,
    )

@router.get("/impulsoprevine/capitacao-ponderada/cadastros-contagem")
async def obter_contagem_cadastros_por_status(
    municipio_uf: str,
):
    return capitacao_ponderada_cadastros_status(
        municipio_uf=municipio_uf
    )

@router.get("/impulsoprevine/capitacao-ponderada/validacao-producao")
async def obter_validacao_por_producao(
    municipio_uf: str,
):
    return capitacao_ponderada_validacao_por_producao(
        municipio_uf=municipio_uf,
    )

@router.get("/impulsoprevine/capitacao-ponderada/validacao-producao-aplicacao")
async def obter_validacao_por_producao_por_aplicacao(
    municipio_uf: str,
):
    return capitacao_ponderada_validacao_por_producao_por_aplicacao(
        municipio_uf=municipio_uf
    )