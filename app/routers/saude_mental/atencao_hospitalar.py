from fastapi import APIRouter

from app.controllers.saude_mental.atencao_hospitalar import (
    obter_acolhimento_noturno,
    obter_internacoes_resumo_admissoes,
    # obter_internacoes_resumo_admissoes_12m,
    obter_internacoes_resumo_altas,
    # obter_internacoes_resumo_altas_12m
)

router = APIRouter()


@router.get("/saude-mental/atencao_hospitalar/noturno")
async def obter_dados_acolhimento_noturno(
    municipio_id_sus: str,
):
    return obter_acolhimento_noturno(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/atencao_hospitalar/admissoes")
async def obter_internacoes_resumo_admissoes(
    municipio_id_sus: str,
):
    return obter_internacoes_resumo_admissoes(
        municipio_id_sus=municipio_id_sus
    )


# @router.get("/saude-mental/atencao_hospitalar/admissoes12m")
# async def obter_dados_internacoes_resumo_admissoes_12m(
#     municipio_id_sus: str,
# ):
#     return obter_internacoes_resumo_admissoes_12m(
#         municipio_id_sus=municipio_id_sus
#     )

@router.get("/saude-mental/atencao_hospitalar/altas")
async def obter_dados_internacoes_resumo_altas(
    municipio_id_sus: str,
):
    return obter_internacoes_resumo_altas(
        municipio_id_sus=municipio_id_sus
    )

# @router.get("/saude-mental/atencao_hospitalar/altas12m")
# async def obter_dados_internacoes_resumo_altas_12m(
#     municipio_id_sus: str,
# ):
#     return obter_internacoes_resumo_altas_12m(
#         municipio_id_sus=municipio_id_sus
#     )
