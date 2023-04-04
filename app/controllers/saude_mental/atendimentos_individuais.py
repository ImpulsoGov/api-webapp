from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.atendimentos_individuais import (
    AtendimentosIndividuaisPorCaps,
    PerfilUsuariosAtendimentosIndividuaisCaps,
    ResumoPerfilUsuariosAtendimentosIndividuaisCaps,
)

session = db.session


def obter_atendimentos_individuais_por_caps_de_municipio(municipio_id_sus: str):
    atendimentos_individuais_caps = (
        session.query(AtendimentosIndividuaisPorCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(atendimentos_individuais_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de atendimentos individuais CAPS "
            "do município não encontrados",
        )

    return atendimentos_individuais_caps


def obter_perfil_usuarios_caps_por_id_sus(municipio_id_sus: str):
    perfil_usuarios_caps = (
        session.query(PerfilUsuariosAtendimentosIndividuaisCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(perfil_usuarios_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Dados de perfil de usuários CAPS "
            "do município não encontrados",
        )

    return perfil_usuarios_caps


def obter_resumo_perfil_usuarios_caps_por_id_sus(municipio_id_sus: str):
    resumo_perfil_usuarios_caps = (
        session.query(ResumoPerfilUsuariosAtendimentosIndividuaisCaps)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(resumo_perfil_usuarios_caps) == 0:
        raise HTTPException(
            status_code=404,
            detail="Resumo do perfil de usuários CAPS "
            "do município não encontrado",
        )

    return resumo_perfil_usuarios_caps
