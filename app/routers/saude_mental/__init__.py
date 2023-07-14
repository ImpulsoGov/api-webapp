from fastapi import APIRouter

from app.routers.saude_mental import (
    abandono,
    ambulatorio,
    atencao_hospitalar,
    atendimentos_individuais,
    consultorionarua,
    encaminhamentos,
    estabelecimentos_e_periodos,
    internacoes,
    matriciamentos,
    procedimentos,
    reducaodedanos,
    resumo,
    usuarios,
)

router = APIRouter()

router.include_router(encaminhamentos.router)
router.include_router(matriciamentos.router)
router.include_router(internacoes.router)
router.include_router(atendimentos_individuais.router)
router.include_router(consultorionarua.router)
router.include_router(reducaodedanos.router)
router.include_router(usuarios.router)
router.include_router(abandono.router)
router.include_router(procedimentos.router)
router.include_router(atencao_hospitalar.router)
router.include_router(ambulatorio.router)
router.include_router(resumo.router)
router.include_router(estabelecimentos_e_periodos.router)
