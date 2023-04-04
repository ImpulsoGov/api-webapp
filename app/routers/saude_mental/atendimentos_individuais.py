from fastapi import APIRouter

from app.controllers.saude_mental.atendimentos_individuais import (
    obter_atendimentos_individuais_por_caps_de_municipio,
    obter_perfil_usuarios_caps_por_id_sus,
    obter_resumo_perfil_usuarios_caps_por_id_sus,
)

router = APIRouter()


@router.get("/saude-mental/atendimentosindividuais/porcaps")
async def obter_atendimentos_caps(
    municipio_id_sus: str,
):
    return obter_atendimentos_individuais_por_caps_de_municipio(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/atendimentosindividuais/caps/perfil")
async def obter_perfil_usuarios_caps(
    municipio_id_sus: str,
):
    return obter_perfil_usuarios_caps_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )


@router.get("/saude-mental/atendimentosindividuais/caps/perfil/resumo")
async def obter_resumo_perfil_usuarios_caps(
    municipio_id_sus: str,
):
    return obter_resumo_perfil_usuarios_caps_por_id_sus(
        municipio_id_sus=municipio_id_sus
    )
