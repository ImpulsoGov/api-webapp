from fastapi import APIRouter, Depends,Form
from typing import Optional,List
from app.controllers import municipios,auth,cadastro_usuarios,recuperação_senha,gerenciamento_usuarios, chave_temp_data_studio
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from app.models.usuarios import Usuario
from fastapi import BackgroundTasks
router = APIRouter()

class Municipio(BaseModel):
    id : int
    estado_sigla : str
    estado_nome : str
    estado_nome_normalizado : str
    estado_id_ibge : str
    municipio_eh_capital : bool
    municipio_id_sus : str
    municipio_id_ibge : str
    municipio_nome : str
    municipio_nome_normalizado : str
    slug : str
    ddd  : int
    municipio_comarca_id_judiciario : str
    macrorregiao_nome : str
    macrorregiao_id_ibge : str
    mesorregiao_id_ibge : str
    mesorregiao_nome : str
    microrregiao_id_ibge : str
    microrregiao_nome  : str
    regiao_saude_id : str
    regiao_saude_nome  : str
    regiao_imediata_id_ibge : str
    regiao_imediata_nome  : str
    regiao_intermediaria_id_ibge : str
    regiao_intermediaria_nome : str

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

@router.get("/suporte/municipios/", response_model=List[Municipio])
async def consulta_municipio(id_sus: Optional[str] = None, municipio_nome: Optional[str] = None , estado_sigla: Optional[str] = None, estado_nome: Optional[str] = None):
    res = municipios.consulta_municipio(id_sus,municipio_nome,estado_sigla,estado_nome)
    return res

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

@router.post("/suporte/usuarios/token", response_model=Token )
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.login(form_data)

class Mensagem(BaseModel):
    erros : Optional[List] = None
    mensagem : Optional[str] = None

    class Config:
        orm_mode = True

@router.post("/suporte/usuarios/cadastro")
async def cadastro(
    nome: str = Form(...),
    mail: str = Form(...),
    senha: str = Form(...),
    cpf: str = Form(...)
    ):
    return cadastro_usuarios.cadastrar_usuario(nome,mail,senha,cpf)

@router.post("/suporte/usuarios/cadastro-ip")
async def cadastroip(
    municipio: str = Form(...),
    cargo: str = Form(...),
    telefone: str = Form(...),
    whatsapp: str = Form(...),
    mail: str = Form(...),
    equipe: str = Form(...),
    ):
    return cadastro_usuarios.cadastrar_usuario_ip(municipio,cargo,telefone,whatsapp,mail,equipe)

@router.post("/suporte/usuarios/cadastro-lote")
async def cadastro_lotes(
    nome: str = Form(...),
    mail: str = Form(...),
    senha: str = Form(...),
    cpf: str = Form(...),
    municipio_uf: str = Form(...),
    cargo: str = Form(...),
    telefone: str = Form(...),
    whatsapp: str = Form(...),
    equipe: str = Form(...),
    username: Usuario = Depends(auth.get_current_user)
    ):
    return cadastro_usuarios.cadastrar_em_lote(nome,mail,senha,cpf,municipio_uf,cargo,telefone,whatsapp,equipe,username["perfil"],2)


@router.post("/suporte/usuarios/solicitar-recuperacao", response_model=Mensagem)
async def solicita_recuperacao(mail: str):
    return recuperação_senha.solicita_recuperacao(mail)

@router.post("/suporte/usuarios/alterar-senha", response_model=Mensagem)
async def alterar_senha(mail: str = Form(...),codigo: str = Form(...),senha: str = Form(...)):
    return recuperação_senha.recuperar(mail,codigo,senha)

class Usuarios_lista(BaseModel):
    usuarios : Optional[List] = None
    erros : Optional[List] = None


@router.get("/suporte/ger_usuarios/lista-usuarios-sem-liberacao", response_model=Usuarios_lista)
async def lista_usuarios_sem_liberacao(username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.lista_usuarios_sem_liberacao(username["perfil"],2)
    return res

@router.get("/suporte/ger_usuarios/lista-usuarios", response_model=Usuarios_lista)
async def lista_usuarios(username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.lista_usuarios(username["perfil"],2)
    return res

class Cadastro(BaseModel):
    erros : Optional[List] = None
    cadastro : Optional[List] = None

@router.get("/suporte/ger_usuarios/cadastro", response_model=Cadastro)
async def dados_cadastro(id: str, id_cod: int,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.dados_usuarios(id_cod,id,username["perfil"],2)
    return res

@router.get("/suporte/ger_usuarios/cargo-nome")
async def nome_cargo(id: str, id_cod: int,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.cargo_nome(id_cod,id,username["perfil"],6)
    return res

@router.post("/suporte/ger_usuarios/add-perfil", response_model=Mensagem)
async def adicionar_perfil(perfil: int, id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.add_perfil(id_cod,id_usuario,perfil,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/remove-perfil", response_model=Mensagem)
async def remover_perfil(perfil: int, id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.remove_perfil(id_cod,id_usuario,perfil,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/desativa-usuario", response_model=Mensagem)
async def desativar_usuario(id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.desativar_usuario(id_cod,id_usuario,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/reativa-usuario", response_model=Mensagem)
async def reativar_usuario(id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.reativar_usuario(id_cod,id_usuario,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/perfil-primeiro-acesso", response_model=Mensagem)
async def liberar_primeiro_acesso(perfil: int, id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.primeiro_acesso(id_cod,id_usuario,perfil,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/ativacao-primeiro-acesso", response_model=Mensagem)
async def ativacao_inicial_usuario(codigo: str, id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.primeira_ativacao(id_cod,id_usuario,codigo,username["perfil"],2)
    return res

@router.post("/suporte/ger_usuarios/ativacao-primeiro-acesso-em-lote", response_model=Mensagem)
async def ativacao_inicial_usuario_em_lote(id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.primeira_ativacao_em_lote(id_cod,id_usuario,username["perfil"],2)
    return res

@router.get("/suporte/ger_usuarios/obter-perfil")
async def ativacao_inicial_usuario_em_lote(id_cod: int,id_usuario: str,username: Usuario = Depends(auth.get_current_user)):
    res = gerenciamento_usuarios.get_perfil_usuarios(id_cod,id_usuario,username["perfil"],2)
    return res


class ChaveDS(BaseModel):
    access_token: str
    mensagem : Optional[str] = None
    class Config:
        orm_mode = True

class ValChaveDS(BaseModel):
    access_token: Optional[bool] 
    mensagem : Optional[str] = None
    class Config:
        orm_mode = True

@router.post("/suporte/ds/genchavetemp" , response_model=ChaveDS)
async def gen_chave(form_data: OAuth2PasswordRequestForm = Depends()):
    return chave_temp_data_studio.gen_chave_temp(form_data)

@router.post("/suporte/ds/valchavetemp" , response_model=ValChaveDS)
async def gen_chave(chave: str,form_data: OAuth2PasswordRequestForm = Depends() ):
    return chave_temp_data_studio.val_chave_temp(chave)

@router.get("/suporte/validar-cpf")
async def gen_chave(cpf: str):
    return cadastro_usuarios.validador_de_cpf(cpf)

@router.get("/suporte/validate-token",)
async def validate_token(username: Usuario = Depends(auth.get_current_user)):
    return True

@router.post("/suporte/ger_usuarios/solicitar-nova-senha")
async def solicitar_nova_senha(background_tasks: BackgroundTasks,mail: str = Form(...)):
    background_tasks.add_task(gerenciamento_usuarios.apagar_codigo_recuperacao_tempo,mail)
    return gerenciamento_usuarios.solicitar_nova_senha(mail)

@router.post("/suporte/ger_usuarios/alterar-senha")
async def solicitar_nova_senha(mail: str,codigo: str,nova_senha: str):
    return gerenciamento_usuarios.alterar_senha(mail,codigo,nova_senha)
