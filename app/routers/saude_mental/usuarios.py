from fastapi import APIRouter
import pymysql, pandas as pd
from sqlalchemy import create_engine

from app.controllers.saude_mental.usuarios import (
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
    engine = create_engine('postgresql+psycopg2://api_user:api-2302-ImPuLsO@34.68.68.223:5432/api') 
    con = engine.connect()
    df = pd.read_sql("SELECT * FROM saude_mental.caps_usuarios_ativos_perfil WHERE unidade_geografica_id_sus = '261160'", con)
    return df
    # return obter_usuarios_perfil(municipio_id_sus=municipio_id_sus)


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
