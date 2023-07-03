from fastapi import APIRouter

from app.controllers.saude_mental.usuarios import (
    obter_estabelecimentos_por_id_sus,
    obter_perfil_usuarios_ativos_por_cid,
    obter_perfil_usuarios_ativos_por_condicao,
    obter_perfil_usuarios_ativos_por_genero_e_idade,
    obter_perfil_usuarios_ativos_por_raca,
    obter_perfil_usuarios_novos_por_condicao,
    obter_perfil_usuarios_novos_por_genero_e_idade,
    obter_perfil_usuarios_novos_por_raca,
    obter_periodos_por_id_sus,
    obter_usuarios_novos,
    obter_usuarios_novos_resumo,
    obter_usuarios_perfil,
    obter_usuarios_perfil_estabelecimento,
)

router = APIRouter()


@router.get("/saude-mental/usuarios/perfil")
async def obter_perfil_usuarios(
    municipio_id_sus: str,
):
    return obter_usuarios_perfil(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/perfilestabelecimento")
async def obter_perfil_usuarios_estabelecimento(
    municipio_id_sus: str,
):
    return obter_usuarios_perfil_estabelecimento(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/novos")
async def obter_novos_usuarios(
    municipio_id_sus: str,
):
    return obter_usuarios_novos(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/novosresumo")
async def obter_novos_usuarios_resumo(
    municipio_id_sus: str,
):
    return obter_usuarios_novos_resumo(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/usuarios/perfil/condicao")
async def obter_condicao_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_condicao(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/genero-e-idade")
async def obter_genero_e_idade_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_genero_e_idade(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/raca")
async def obter_raca_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_raca(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/cid")
async def obter_cid_usuarios_ativos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_ativos_por_cid(
        municipio_id_sus,
        estabelecimento,
        periodo,
    )


@router.get("/saude-mental/usuarios/perfil/estabelecimentos")
async def obter_estabelecimentos(municipio_id_sus: str):
    return obter_estabelecimentos_por_id_sus(
        municipio_id_sus,
    )


@router.get("/saude-mental/usuarios/perfil/periodos")
async def obter_periodos(municipio_id_sus: str):
    return obter_periodos_por_id_sus(
        municipio_id_sus,
    )


@router.get("/saude-mental/usuarios/novos/condicao")
async def obter_condicao_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_novos_por_condicao(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodo=periodo,
    )


@router.get("/saude-mental/usuarios/novos/genero-e-idade")
async def obter_genero_e_idade_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_novos_por_genero_e_idade(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodo=periodo,
    )


@router.get("/saude-mental/usuarios/novos/raca")
async def obter_raca_usuarios_novos(
    municipio_id_sus: str, estabelecimento: str, periodo: str
):
    return obter_perfil_usuarios_novos_por_raca(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodo=periodo,
    )
