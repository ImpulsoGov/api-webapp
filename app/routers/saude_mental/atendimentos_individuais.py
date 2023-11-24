from fastapi import APIRouter
from typing import Union
from app.controllers.saude_mental.atendimentos_individuais import (
    obter_atendimentos_individuais_por_caps_de_municipio,
    obter_perfil_atendimentos_individuais_por_cid,
    obter_perfil_atendimentos_individuais_por_genero_e_idade,
    obter_perfil_atendimentos_individuais_por_raca,
    obter_resumo_perfil_usuarios_caps_por_id_sus,
)

router = APIRouter()


@router.get("/saude-mental/atendimentosindividuais/porcaps")
async def obter_atendimentos_caps(
    municipio_id_sus: str,
    estabelecimento: Union[str, None] = None,
    periodo: Union[str, None] = None,
    estabelecimento_linha_idade: Union[str, None] = None,
    estabelecimento_linha_perfil: Union[str, None] = None
):
    return obter_atendimentos_individuais_por_caps_de_municipio(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodo=periodo,
        estabelecimento_linha_perfil=estabelecimento_linha_perfil,
        estabelecimento_linha_idade=estabelecimento_linha_idade
    )


@router.get("/saude-mental/atendimentosindividuais/caps/perfil/resumo")
async def obter_resumo_perfil_usuarios_caps(
    municipio_id_sus: str,
):
    return obter_resumo_perfil_usuarios_caps_por_id_sus(municipio_id_sus=municipio_id_sus)


@router.get("/saude-mental/atendimentosindividuais/cid")
async def obter_cid_atendimentos_individuais(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_atendimentos_individuais_por_cid(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/atendimentosindividuais/genero-e-idade")
async def obter_genero_e_idade_atendimentos_individuais(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_atendimentos_individuais_por_genero_e_idade(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )


@router.get("/saude-mental/atendimentosindividuais/raca")
async def obter_raca_atendimentos_individuais(
    municipio_id_sus: str, estabelecimento: str, periodos: str
):
    return obter_perfil_atendimentos_individuais_por_raca(
        municipio_id_sus=municipio_id_sus,
        estabelecimento=estabelecimento,
        periodos=periodos,
    )
