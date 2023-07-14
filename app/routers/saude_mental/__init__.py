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

router_saude_mental = APIRouter()

router_saude_mental.include_router(encaminhamentos.router)
router_saude_mental.include_router(matriciamentos.router)
router_saude_mental.include_router(internacoes.router)
router_saude_mental.include_router(atendimentos_individuais.router)
router_saude_mental.include_router(consultorionarua.router)
router_saude_mental.include_router(reducaodedanos.router)
router_saude_mental.include_router(usuarios.router)
router_saude_mental.include_router(abandono.router)
router_saude_mental.include_router(procedimentos.router)
router_saude_mental.include_router(atencao_hospitalar.router)
router_saude_mental.include_router(ambulatorio.router)
router_saude_mental.include_router(resumo.router)
router_saude_mental.include_router(estabelecimentos_e_periodos.router)
