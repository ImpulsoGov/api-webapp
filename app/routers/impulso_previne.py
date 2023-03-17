from fastapi.security import OAuth2PasswordRequestForm
from app.controllers import indicadores,forum_ip,auth,busca_ativa_gestantes,busca_ativa_diabeticos,busca_ativa_hipertensos,TrilhaCapacitacao
from fastapi import APIRouter, Depends,Form
from typing import Optional, List
from pydantic import BaseModel
from app.controllers.auth import get_current_user,Usuario
router = APIRouter()

class Indicador(BaseModel):
    id : int
    estado_sigla : str
    estado_nome : str
    estado_nome_normalizado : str
    municipio_id_sus : str
    municipio_nome : str
    municipio_nome_normalizado : str
    indicadores_parametros_id : int
    indicadores_parametros_nome : str
    indicadores_parametros_nome_normalizado : str
    indicadores_parametros_ordem : int
    indicadores_parametros_meta : float
    indicadores_parametros_peso : float
    indicadores_resultados_porcentagem : float
    diff_numerador_para_meta : int

    class Config:
        orm_mode = True

@router.get("/impulsoprevine/indicadores/resumo", response_model=List[Indicador])
async def consulta_indicadores(indicadores_parametros_id: Optional[str] = None, indicadores_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None, id_sus: Optional[str] = None, municipio_nome: Optional[str] = None):
    res = indicadores.consulta_indicadores(id_sus,municipio_nome,estado_sigla,estado_nome,indicadores_nome,indicadores_parametros_id)
    return res

class Mensagem(BaseModel):
    erros : Optional[List] = None
    mensagem : Optional[str] = None

    class Config:
        orm_mode = True

@router.post("/impulsoprevine/forum/criar-topico", response_model=Mensagem)
async def criar_topico(titulo: str, texto: str,username: Usuario = Depends(get_current_user)):
    res = forum_ip.criar_topico(titulo,texto)
    return res

@router.post("/impulsoprevine/forum/responder-topico", response_model=Mensagem)
async def responder_topico(resposta: str, topico_id: str, usuario: str,username: Usuario = Depends(get_current_user)):
    res = forum_ip.resposta_topico(resposta,topico_id,usuario)
    return res

class Topico(BaseModel):
    erros : Optional[List] = None
    topicos : Optional[List] = None

    class Config:
        orm_mode = True

@router.get("/impulsoprevine/forum/", response_model=Topico)
async def buscar_topicos(respostas: Optional[int] = None, topico_id: Optional[str] = None, username: Usuario = Depends(get_current_user)):
    return forum_ip.buscar_topico(topico_id,respostas)

@router.post("/impulsoprevine/forum/excluir-topico", response_model=Mensagem)
async def excluir_topicos(topico_id: Optional[str] = None, username: Usuario = Depends(get_current_user)):
    return forum_ip.excluir_topico(topico_id)

@router.get("/impulsoprevine/busca-ativa/gestantes")
async def gestantes_equipe(municipio_uf,equipe,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_gestantes.consulta_gestantes_equipe(municipio_uf,equipe)
    return res

@router.get("/impulsoprevine/busca-ativa/gestantes-coordenacao")
async def gestantes_municipio(municipio_uf,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_gestantes.consulta_gestantes_coordenacao(municipio_uf)
    return res

@router.get("/impulsoprevine/busca-ativa/gestantes-cadastros-duplicados-por-equipe")
async def gestantes_cadastros_equipe(municipio_uf,equipe,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_gestantes.cadastros_duplicados_gestantes_por_equipe(municipio_uf,equipe)
    return res

@router.get("/impulsoprevine/busca-ativa/gestantes-cadastros-duplicados-por-municipio")
async def gestantes_cadastros_municipio(municipio_uf,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_gestantes.cadastros_duplicados_gestantes_por_municipio(municipio_uf)
    return res

@router.get("/impulsoprevine/busca-ativa/diabeticos-por-equipe")
async def diabeticos_equipe(municipio_uf,equipe,username: Usuario = Depends(get_current_user)):
    return busca_ativa_diabeticos.diabeticos_equipe(municipio_uf,equipe)

@router.get("/impulsoprevine/busca-ativa/diabeticos-por-municipio")
async def diabeticos_municipio(municipio_uf,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_diabeticos.diabeticos_coordenacao(municipio_uf)
    return res

@router.get("/impulsoprevine/busca-ativa/hipertensos-por-equipe")
async def hipertensos_equipe(municipio_uf,equipe,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_hipertensos.hipertensos_equipe(municipio_uf,equipe)
    return res

@router.get("/impulsoprevine/busca-ativa/hipertensos-por-municipio")
async def hipertensos_municipio(municipio_uf,username: Usuario = Depends(get_current_user)):
    res = busca_ativa_hipertensos.hipertensos_coordenacao(municipio_uf)
    return res


@router.post("/impulsoprevine/capacitacao/conclusao-conteudo")
async def conclusao(usuario_id: str = Form(...), codigo_conteudo: str = Form(...),conclusao: bool = Form(...),username: Usuario = Depends(auth.get_current_user)):
    res = TrilhaCapacitacao.conclusao_conteudo(usuario_id,codigo_conteudo,conclusao)
    return res

@router.post("/impulsoprevine/capacitacao/avaliacao-conteudo")
async def avaliacao(usuario_id: str = Form(...), codigo_conteudo: str = Form(...),avaliacao: int = Form(...),username: Usuario = Depends(auth.get_current_user)):
    res = TrilhaCapacitacao.avaliacao_conteudo(usuario_id,codigo_conteudo,avaliacao)
    return res

@router.post("/impulsoprevine/capacitacao/consulta-avaliacao-conclusao")
async def consulta_avaliacao_conclusao_conteudo(
    usuario_id: str = Form(...),
    codigo_conteudo: str = Form(...),
    username: Usuario = Depends(auth.get_current_user)
    ):
    res = TrilhaCapacitacao.consulta_avaliacao_conclusao(usuario_id,codigo_conteudo)
    return res

@router.post("/impulsoprevine/capacitacao/consulta-avaliacao-conclusao-por-usuario")
async def consulta_avaliacao_conclusao_conteudo(
    usuario_id: str = Form(...),
    username: Usuario = Depends(auth.get_current_user)
    ):
    res = TrilhaCapacitacao.consulta_avaliacao_conclusao_por_usuario(usuario_id)
    return res
