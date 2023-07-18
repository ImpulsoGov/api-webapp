from typing import List, Optional

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.controllers.impulso_previne_nominal import (
    TrilhaCapacitacao,
    busca_ativa_diabeticos,
    busca_ativa_gestantes,
    busca_ativa_hipertensos,
    forum_ip,
)
from app.controllers.usuarios.auth import Usuario, get_current_user

router = APIRouter()

class Mensagem(BaseModel):
    erros: Optional[List] = None
    mensagem: Optional[str] = None

    class Config:
        orm_mode = True


@router.post("/impulsoprevine/forum/criar-topico", response_model=Mensagem)
async def criar_topico(
    titulo: str, texto: str, username: Usuario = Depends(get_current_user)
):
    res = forum_ip.criar_topico(titulo, texto)
    return res


@router.post("/impulsoprevine/forum/responder-topico", response_model=Mensagem)
async def responder_topico(
    resposta: str,
    topico_id: str,
    usuario: str,
    username: Usuario = Depends(get_current_user),
):
    res = forum_ip.resposta_topico(resposta, topico_id, usuario)
    return res


class Topico(BaseModel):
    erros: Optional[List] = None
    topicos: Optional[List] = None

    class Config:
        orm_mode = True


@router.get("/impulsoprevine/forum/", response_model=Topico)
async def buscar_topicos(
    respostas: Optional[int] = None,
    topico_id: Optional[str] = None,
    username: Usuario = Depends(get_current_user),
):
    return forum_ip.buscar_topico(topico_id, respostas)


@router.post("/impulsoprevine/forum/excluir-topico", response_model=Mensagem)
async def excluir_topicos(
    topico_id: Optional[str] = None, username: Usuario = Depends(get_current_user)
):
    return forum_ip.excluir_topico(topico_id)


@router.get("/impulsoprevine/busca-ativa/gestantes")
async def gestantes_equipe(
    municipio_uf, equipe, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_gestantes.consulta_gestantes_equipe(municipio_uf, equipe)
    return res


@router.get("/impulsoprevine/busca-ativa/gestantes-coordenacao")
async def gestantes_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_gestantes.consulta_gestantes_coordenacao(municipio_uf)
    return res


@router.get("/impulsoprevine/busca-ativa/gestantes-cadastros-duplicados-por-equipe")
async def gestantes_cadastros_equipe(
    municipio_uf, equipe, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_gestantes.cadastros_duplicados_gestantes_por_equipe(
        municipio_uf, equipe
    )
    return res


@router.get("/impulsoprevine/busca-ativa/gestantes-cadastros-duplicados-por-municipio")
async def gestantes_cadastros_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_gestantes.cadastros_duplicados_gestantes_por_municipio(municipio_uf)
    return res


@router.get("/impulsoprevine/busca-ativa/diabeticos-por-equipe")
async def diabeticos_equipe(
    municipio_uf, equipe, username: Usuario = Depends(get_current_user)
):
    return busca_ativa_diabeticos.diabeticos_equipe(municipio_uf, equipe)


@router.get("/impulsoprevine/busca-ativa/diabeticos-por-municipio")
async def diabeticos_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_diabeticos.diabetes_aps(municipio_uf)
    return res


@router.get("/impulsoprevine/busca-ativa/diabeticos-graficos")
async def diabeticos_graficos_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_diabeticos.diabeticos_graficos(municipio_uf)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensos-por-equipe")
async def hipertensos_equipe(
    municipio_uf, faixa_etaria, equipe, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensos_equipe(municipio_uf, equipe, faixa_etaria)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensos-por-municipio")
async def hipertensos_municipio(
    municipio_uf, faixa_etaria, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensos_coordenacao(municipio_uf, faixa_etaria)
    return res


@router.get("/impulsoprevine/busca-ativa/score-cards-hipertensos-por-municipio")
async def hipertensos_municipio(
    municipio_id_sus, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensao_score_cards_aps(municipio_id_sus)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensao-por-municipio")
async def hipertensao_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensao_aps(municipio_uf)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensao-por-equipe")
async def hipertensao_equipe(
    municipio_uf, equipe, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensao_equipe(municipio_uf, equipe)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensao-grafico")
async def hipertensao_grafico_aps(
    municipio_id_sus, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensao_grafico(municipio_id_sus)
    return res


@router.get("/impulsoprevine/busca-ativa/hipertensos-graficos")
async def hipertensos_graficos_municipio(
    municipio_uf, username: Usuario = Depends(get_current_user)
):
    res = busca_ativa_hipertensos.hipertensos_graficos(municipio_uf)
    return res


@router.post("/impulsoprevine/capacitacao/conclusao-conteudo")
async def conclusao(
    usuario_id: str = Form(...),
    codigo_conteudo: str = Form(...),
    conclusao: bool = Form(...),
    username: Usuario = Depends(get_current_user),
):
    res = TrilhaCapacitacao.conclusao_conteudo(usuario_id, codigo_conteudo, conclusao)
    return res


@router.post("/impulsoprevine/capacitacao/avaliacao-conteudo")
async def avaliacao(
    usuario_id: str = Form(...),
    codigo_conteudo: str = Form(...),
    avaliacao: int = Form(...),
    username: Usuario = Depends(get_current_user),
):
    res = TrilhaCapacitacao.avaliacao_conteudo(usuario_id, codigo_conteudo, avaliacao)
    return res


@router.post("/impulsoprevine/capacitacao/consulta-avaliacao-conclusao")
async def consulta_avaliacao_conclusao_conteudo(
    usuario_id: str = Form(...),
    codigo_conteudo: str = Form(...),
    username: Usuario = Depends(get_current_user),
):
    res = TrilhaCapacitacao.consulta_avaliacao_conclusao(usuario_id, codigo_conteudo)
    return res


@router.post("/impulsoprevine/capacitacao/consulta-avaliacao-conclusao-por-usuario")
async def consulta_avaliacao_conclusao_conteudo(
    usuario_id: str = Form(...), username: Usuario = Depends(get_current_user)
):
    res = TrilhaCapacitacao.consulta_avaliacao_conclusao_por_usuario(usuario_id)
    return res

@router.get("/impulsoprevine/capacitacao/acesso-trilhas")
async def acesso_trilha(usuario_id: str,username: Usuario = Depends(get_current_user)):
    return TrilhaCapacitacao.trilha_acesso(usuario_id)

@router.get("/impulsoprevine/capacitacao/acesso-modulos-trilha")
async def acesso_modulos(usuario_id: str,trilha_id : str, username: Usuario = Depends(get_current_user)):
    return TrilhaCapacitacao.trilha_modulos_acesso(usuario_id,trilha_id)

@router.post("/impulsoprevine/capacitacao/liberar-acesso-modulo-trilha")
async def liberar_acesso_modulo_trilha(
    usuario_id: str = Form(...),
    trilha_id: str = Form(...),
    modulo : int = Form(...),
    username: Usuario = Depends(get_current_user)
):
    return TrilhaCapacitacao.trilha_modulos_acesso_add(usuario_id,trilha_id,modulo)