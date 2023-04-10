from fastapi import HTTPException

from app.models import db
from app.models.saude_mental.atencao_hospitalar import (
    AcolhimentoNoturno,
    # InternacoesResumoAdmissoes,
    # InternacoesResumoAdmissoes12m,
    # InternacoesResumoAltas,
    # InternacoesResumoAltas12m
)

session = db.session


def obter_acolhimento_noturno(
    municipio_id_sus: str,
):
    acolhimento_noturno = (
        session.query(AcolhimentoNoturno)
        .filter_by(unidade_geografica_id_sus=municipio_id_sus)
        .all()
    )

    if len(acolhimento_noturno) == 0:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dados não encontrados",
            ),
        )

    return acolhimento_noturno

# def obter_internacoes_resumo_admissoes(
#     municipio_id_sus: str,
# ):
#     internacoes_resumo_admissoes = (
#         session.query(InternacoesResumoAdmissoes)
#         .filter_by(unidade_geografica_id_sus=municipio_id_sus)
#         .all()
#     )

#     if len(internacoes_resumo_admissoes) == 0:
#         raise HTTPException(
#             status_code=404,
#             detail=(
#                 "Dados não encontrados",
#             ),
#         )

#     return internacoes_resumo_admissoes

# def obter_internacoes_resumo_admissoes_12m(
#     municipio_id_sus: str,
# ):
#     internacoes_resumo_admissoes_12m = (
#         session.query(InternacoesResumoAdmissoes12m)
#         .filter_by(unidade_geografica_id_sus=municipio_id_sus)
#         .all()
#     )

#     if len(internacoes_resumo_admissoes_12m) == 0:
#         raise HTTPException(
#             status_code=404,
#             detail=(
#                 "Dados não encontrados",
#             ),
#         )

#     return internacoes_resumo_admissoes_12m

# def obter_internacoes_resumo_altas(
#     municipio_id_sus: str,
# ):
#     internacoes_resumo_altas = (
#         session.query(InternacoesResumoAltas)
#         .filter_by(unidade_geografica_id_sus=municipio_id_sus)
#         .all()
#     )

#     if len(internacoes_resumo_altas) == 0:
#         raise HTTPException(
#             status_code=404,
#             detail=(
#                 "Dados não encontrados",
#             ),
#         )

#     return internacoes_resumo_altas

# def obter_internacoes_resumo_altas_12m(
#     municipio_id_sus: str,
# ):
#     internacoes_resumo_altas_12m = (
#         session.query(InternacoesResumoAltas12m)
#         .filter_by(unidade_geografica_id_sus=municipio_id_sus)
#         .all()
#     )

#     if len(internacoes_resumo_altas_12m) == 0:
#         raise HTTPException(
#             status_code=404,
#             detail=(
#                 "Dados não encontrados",
#             ),
#         )

#     return internacoes_resumo_altas_12m
