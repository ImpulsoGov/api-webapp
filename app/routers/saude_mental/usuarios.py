from fastapi import APIRouter
import pymysql, pandas as pd
from sqlalchemy import create_engine

from app.controllers.saude_mental.usuarios import (
    obter_usuarios_novos,
    obter_usuarios_novos_resumo,
    obter_usuarios_perfil,
    obter_usuarios_perfil_estabelecimento,
    obter_usuarios_perfil_condicao,
    obter_usuarios_perfil_idade_raca,
    obter_perfil_usuarios_ativos_por_condicao,
)
from app.models.db import session

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
    return obter_usuarios_perfil_estabelecimento(
        municipio_id_sus=municipio_id_sus
    )


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
    municipio_id_sus: str,
    linha_perfil: str,
    linha_idade: str,
):
    return obter_perfil_usuarios_ativos_por_condicao(
        municipio_id_sus,
        linha_perfil,
        linha_idade,
    )
