from fastapi import APIRouter

from app.routers.impulso_previne_publico import (
    acoes_estrategicas,
    caracterizacao_municipal_resumo,
    capitacao_ponderada,
    indicadores_desempenho,
)

router = APIRouter()

router.include_router(acoes_estrategicas.router)
router.include_router(caracterizacao_municipal_resumo.router)
router.include_router(capitacao_ponderada.router)
router.include_router(indicadores_desempenho.router)