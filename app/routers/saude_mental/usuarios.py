from fastapi import APIRouter

from app.controllers.saude_mental.usuarios import (obter_usuarios_perfil,obter_usuarios_perfil_estabelecimento,obter_usuarios_novos,obter_usuarios_novos_resumo)

router = APIRouter()


@router.get("/saude-mental/usuarios/perfil")
async def obter_usuarios_perfil(
    municipio_id_sus: str,
):
    return obter_usuarios_perfil(
        municipio_id_sus=municipio_id_sus
    )

@router.get("/saude-mental/usuarios/perfilestabelecimento")
async def obter_usuarios_perfil_estabelecimento(
    municipio_id_sus: str,
):
    return obter_usuarios_perfil_estabelecimento(
        municipio_id_sus=municipio_id_sus
    )

@router.get("/saude-mental/usuarios/novos")
async def obter_usuarios_novos(
    municipio_id_sus: str,
):
    return obter_usuarios_novos(
        municipio_id_sus=municipio_id_sus
    )

@router.get("/saude-mental/usuarios/novosresumo")
async def obter_usuarios_novos_resumo(
    municipio_id_sus: str,
):
    return obter_usuarios_novos_resumo(
        municipio_id_sus=municipio_id_sus
    )
