import uuid
from datetime import datetime
from sqlalchemy import func
from fastapi import HTTPException

from passlib.context import CryptContext
from validate_docbr import CPF

from app.models import db, municipios
from app.models.usuarios import (
    usuarios,
    perfil_acesso,
    perfil_usuario,
    usuarios_ip,
    usuarios_sm,
)
from app.utils.exceptions import ValidationError

from .auth import controle_perfil

cpf_verificador = CPF()
import re

from email_validator import EmailNotValidError, validate_email

session = db.session


def validar_senha(senha):
    restricoes = []
    if len(senha) < 8:
        restricoes.append({"mensagem1": "Senha deve conter ao menos 8 caracteres"})
    if len(re.findall("[a-z]", senha)) == 0:
        restricoes.append({"mensagem2": "Senha deve conter letras minusculas"})
    if len(re.findall("[A-Z]", senha)) == 0:
        restricoes.append({"mensagem3": "Senha deve conter letras maiusculas"})
    if len(re.findall("[0-9]", senha)) == 0:
        restricoes.append({"mensagem4": "Senha deve conter numeros"})
    if len(re.findall("\W", senha)) == 0:
        restricoes.append({"mensagem4": "Senha deve conter caracteres especiais"})
    if len(re.findall("\s", senha)) != 0:
        restricoes.append({"mensagem4": "Senha não deve conter espaços e quebras"})
    validacao = True if len(restricoes) == 0 else False
    return restricoes, validacao


def consulta_mail(email):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=email)
        res = query.all()
        return (
            True if len(res) == 0 else {"mensagem": "E-mail já cadastrado", "error": True}
        )
    except:
        return {"mensagem": "E-mail já cadastrado", "error": True}


def obter_id(email):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=email)
        res = query.all()
        return res[0].id if len(res) != 0 else {"mensagem": "E-mail não cadastrado"}
    except:
        return {"mensagem": "Error"}


def validador_de_cpf(cpf):
    return cpf_verificador.validate(cpf)


def consulta_cpf(cpf):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(cpf=cpf)
        res = query.all()
        if len(res) == 0 or res == None:
            return True
    except:
        return {"mensagem": "CPF já cadastrado"}


def consulta_id_usuario(id):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(id=id)
        res = query.all()
        return True if len(res) == 0 else {"mensagem": "E-mail já cadastrado"}
    except ValueError as e:
        return {"mensagem": e}


def verifica_mail(email):
    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError as e:
        return {"mensagem": str(e)}


def validar_municipio_id_ibge(municipio_id_ibge):
    try:
        query = db.session.query(municipios.Municipios).filter_by(
            municipio_id_sus=municipio_id_ibge
        )
        res = query.all()
        return (
            True
            if len(res) != 0
            else {"mensagem": "Id IBGE do município inválido", "error": True}
        )
    except:
        return {"mensagem": "Internal server error", "error": True}


def validar_se_municipio_corresponde_ao_id_sus(nome_uf: str, id_sus: str):
    municipio = (
        db.session.query(municipios.Municipios)
        .filter(
            func.concat(
                municipios.Municipios.municipio_nome,
                " - ",
                municipios.Municipios.estado_sigla,
            ).__eq__(nome_uf)
        )
        .first()
    )

    if municipio is None:
        raise ValidationError(f"Município {nome_uf} não existe na base de dados")

    if municipio.municipio_id_sus != id_sus:
        raise ValidationError(
            f"Município {nome_uf} e ID SUS {id_sus} não são correspondentes"
        )


def validar_cargo(cargo):
    try:
        query = db.session.query(cargos.Cargo).filter_by(id=cargo)
        res = query.first()

        return (
            {"id": res.id, "error": False}
            if res != None
            else {"mensagem": "Cargo inválido", "error": True}
        )
    except:
        return {"mensagem": "Internal server error", "error": True}


def validar_telefone(telefone):
    try:
        telefone_regex = "^\d{10,11}$"
        res = re.search(telefone_regex, telefone)

        return (
            True
            if res != None
            else {"mensagem": "Formato de telefone inválido", "error": True}
        )
    except:
        raise {"mensagem": "Internal server error", "error": True}


def cadastrar_usuario(nome, mail, senha, cpf):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuario = usuarios.Usuario(
        id=str(uuid.uuid4()),
        nome_usuario=nome,
        mail=mail,
        hash_senha=pwd_context.hash(senha),
        cpf=cpf,
        criacao_data=criacao_data,
        atualizacao_data=atualizacao_data,
    )
    if not cpf_verificador.validate(cpf):
        return {"mensagem": "CPF Invalido"}
    if not validar_senha(senha)[1]:
        return validar_senha(senha)[0]
    if verifica_mail(mail) != True:
        return verifica_mail(mail)
    if consulta_mail(mail) != True:
        return consulta_mail(mail)
    if consulta_cpf(cpf) != True:
        return consulta_cpf(cpf)

    try:
        session = db.session
        db.session.add(usuario)
        session.commit()
        return {
            "mensagem": "Usuario cadastrado com sucesso, apos a liberação do seu perfil de acesso você recebera no e-mail cadastro mensagem com o link para ativação do seu cadastro"
        }
    except:
        session.rollback()
        return {"mensagem": "Cadastro não efetuado"}


def cadastrar_usuario_ip(municipio, cargo, telefone, whatsapp, mail, equipe):
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wp = True if whatsapp == "1" else False
    try:
        id_usuario = obter_id(mail)
        # validar municipio
        # validar cargo
        # formato telefone
    except:
        return {"mensagem": "Validação dos dados enviados não efetuada"}

    usuario_dados = usuarios_ip.UsuarioIP(
        id=str(uuid.uuid4()),
        municipio=municipio,
        cargo=cargo,
        telefone=telefone,
        whatsapp=wp,
        id_usuario=id_usuario,
        equipe=equipe,
        criacao_data=criacao_data,
        atualizacao_data=atualizacao_data,
    )
    session = db.session
    session.add(usuario_dados)
    session.commit()
    return {
        "mensagem": "dados cadastrados com sucesso, apos a liberação do seu perfil de acesso você recebera no e-mail cadastro mensagem com o link para ativação do seu cadastro"
    }


# cadastrar usuario impulso
def cadastro_impulso(nome, mail, senha, cpf):
    try:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usuario = usuarios.Usuario(
            id=str(uuid.uuid4()),
            nome_usuario=nome,
            mail=mail,
            hash_senha=pwd_context.hash(senha),
            cpf=cpf,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
        )
        if not cpf_verificador.validate(cpf):
            return {"mensagem": "CPF Invalido", "error": True}
        if not validar_senha(senha)[1]:
            return validar_senha(senha)[0]
        if verifica_mail(mail) != True:
            return verifica_mail(mail)
        if consulta_mail(mail) != True:
            return consulta_mail(mail)
        if consulta_cpf(cpf) != True:
            return {"mensagem": "CPF invalido", "error": True}

    except Exception as error:
        session.rollback()
        return {"mensagem": error, "error": True}
    try:
        session.add(usuario)
        return {"mensagem": "Usuário Impulso cadastrado com sucesso", "error": None}
    except Exception as error:
        session.rollback()
        return {"mensagem": error, "error": True}


def cadastro_impulso_sem_ativacao(nome, mail, cpf):
    try:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usuario = usuarios.Usuario(
            id=str(uuid.uuid4()),
            nome_usuario=nome,
            mail=mail,
            cpf=cpf,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
        )
        if not cpf_verificador.validate(cpf):
            return {"mensagem": "CPF Invalido", "error": True}
        if verifica_mail(mail) != True:
            return verifica_mail(mail)
        if consulta_mail(mail) != True:
            return consulta_mail(mail)
        if consulta_cpf(cpf) != True:
            return {"mensagem": "CPF invalido", "error": True}

    except Exception as error:
        session.rollback()
        return {"mensagem": error, "error": True}
    try:
        session.add(usuario)
        return {"mensagem": "Usuário Impulso cadastrado com sucesso", "error": None}
    except Exception as error:
        session.rollback()
        return {"mensagem": error, "error": True}


# cadastrar usuario IP
def cadastro_ip(municipio, cargo, telefone, whatsapp, mail, equipe, municipio_id_sus):
    validar_se_municipio_corresponde_ao_id_sus(nome_uf=municipio, id_sus=municipio_id_sus)
    try:
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        wp = True if whatsapp == "1" else False
        id_usuario = obter_id(mail)
        # validar cargo
        # formato telefone
    except:
        session.rollback()
        return {"mensagem": "Validação dos dados enviados não efetuada", "error": True}
    try:
        usuario_dados = usuarios_ip.UsuarioIP(
            id=str(uuid.uuid4()),
            municipio=municipio,
            cargo=cargo,
            telefone=telefone,
            whatsapp=wp,
            id_usuario=id_usuario,
            equipe=equipe,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
            municipio_id_sus=municipio_id_sus,
        )
        session.add(usuario_dados)
        return {"mensagem": "dados cadastrados com sucesso", "error": None}

    except:
        session.rollback()
        return {"mensagem": "Inserção dos dados falhou", "error": True}


# cadastrar usuario SM
def cadastro_sm(municipio_id_ibge, cargo, telefone, whatsapp, mail, unidade_saude):
    try:
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        wp = True if whatsapp == "1" else False
        id_usuario = obter_id(mail)
        # validar municipio
        validar_municipio = validar_municipio_id_ibge(municipio_id_ibge)
        if validar_municipio != True:
            return validar_municipio
        # validar cargo
        validacao_cargo = validar_cargo(cargo)
        if validacao_cargo["error"]:
            return validacao_cargo
        # formato telefone
        validacao_telefone = validar_telefone(telefone=telefone)
        if validacao_telefone != True:
            return validacao_telefone
    except:
        return {"mensagem": "Validação dos dados enviados não efetuada", "error": True}
    try:
        usuario_dados = usuarios_sm.UsuarioSM(
            id=str(uuid.uuid4()),
            municipio_id_ibge=municipio_id_ibge,
            cargo_id=cargo,
            telefone=telefone,
            whatsapp=wp,
            id_usuario=id_usuario,
            unidade_saude=unidade_saude,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
        )
        session.add(usuario_dados)
        return {"mensagem": "dados cadastrados com sucesso", "error": None}

    except:
        session.rollback()
        return {"mensagem": "Inserção dos dados falhou", "error": True}


# liberar primeiro acesso
def liberar_acesso(id_cod, id, perfil):
    # libera primeiro perfil apos cadastro
    # informar perfil liberado
    try:
        id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
        res = session.query(usuarios.Usuario).filter_by(**id_db).all()
    except Exception as error:
        session.rollback()
        print({"error": error})
        return error
    try:
        if res[0].perfil_ativo != None:
            return {"mensagem": "Usuário já passou pela primeira liberação de perfil"}
        usuario_id = session.query(usuarios.Usuario).filter_by(**id_db).all()[0].id
        perfil_id = (
            session.query(perfil_acesso.Perfil_lista).filter_by(perfil=perfil).all()[0].id
        )  # perfil 6 - IP
        novo_perfil = perfil_usuario.Perfil(
            id=str(uuid.uuid4()),
            usuario_id=usuario_id,
            perfil_id=perfil_id,
            criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
    except Exception as error:
        print({"error": error})
        return error

    try:
        session.add(novo_perfil)
        return {"error": None}
    except Exception as error:
        print({"erros": error})
        return error


# primeira ativação de perfil
def ativar_perfil(id_cod, id):
    # verificar se usuario nunca foi ativado
    id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
    try:
        usuario_id = (
            session.query(usuarios.Usuario).filter_by(**id_db).all()[0].perfil_ativo
        )
        print(usuario_id)
        if usuario_id != None:
            return {"mensagem": "Usuário já realizou primeira ativação", "error": True}
    except Exception as error:
        session.rollback()
        return {"erros": [error]}
    # ativar perfil
    try:
        session.query(usuarios.Usuario).filter_by(**id_db).update(
            {
                "perfil_ativo": True,
                "atualizacao_data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        session.commit()
        return {"mensagem": "Usuário ativado com sucesso", "error": None}
    except Exception as error:
        session.rollback()
        print({"error": [error]})
        return {"erros": [error]}


def cadastrar_em_lote(
    nome,
    mail,
    senha,
    cpf,
    municipio_uf,
    cargo,
    telefone,
    whatsapp,
    equipe,
    username,
    acesso,
):
    # controle de acesso
    controle = controle_perfil(username, acesso)
    if controle != True:
        return controle
    cad_impulso = cadastro_impulso(nome, mail, senha, cpf)
    etapas = []
    if cad_impulso["error"] == None:
        cad_ip = cadastro_ip(municipio_uf, cargo, telefone, whatsapp, mail, equipe)
        etapas.append("Cadastro Impulso realizado com sucesso")
    else:
        return cad_impulso

    if cad_ip["error"] == None:
        etapas.append("Cadastro IP realizado com sucesso")
        lib_acess = liberar_acesso(1, mail)
    else:
        return cad_ip

    if lib_acess["error"] == None:
        etapas.append("Liberação de acesso realizada com sucesso")
        ativar_user = ativar_perfil(1, mail)
    else:
        return lib_acess

    if ativar_user["error"] == None:
        etapas.append("Ativação de perfil realizada com sucesso")
        etapas.append("Usuario cadastrado com sucesso")
        if len(etapas) == 5:
            session.commit()
            print("commit realizado com sucesso")
        return etapas
    else:
        return ativar_user


def cadastrar_em_lote_sem_ativacao(
    nome,
    mail,
    cpf,
    cargo,
    telefone,
    whatsapp,
    equipe,
    username,
    acesso,
    perfil,
    municipio_id_sus,
    projeto="IP",
    unidade_saude=None,
    municipio_uf=None,
):
    try:
        # controle de acesso
        controle = controle_perfil(username, acesso)
        if controle != True:
            return controle
        cad_impulso = cadastro_impulso_sem_ativacao(nome, mail, cpf)
        etapas = []
        cadastros_projetos = {"IP": cadastro_ip, "SM": cadastro_sm}
        proj_args = {
            "IP": {
                "municipio": municipio_uf,
                "cargo": cargo,
                "telefone": telefone,
                "whatsapp": whatsapp,
                "mail": mail,
                "equipe": equipe,
                "municipio_id_sus": municipio_id_sus,
            },
            "SM": {
                "municipio_id_ibge": municipio_id_sus,
                "cargo": cargo,
                "telefone": telefone,
                "whatsapp": whatsapp,
                "mail": mail,
                "unidade_saude": unidade_saude,
            },
        }
        if cad_impulso["error"] == None:
            cad_proj = cadastros_projetos[projeto](**(proj_args[projeto]))
            etapas.append("Cadastro Impulso realizado com sucesso")
        else:
            return cad_impulso

        if cad_proj["error"] == None:
            etapas.append("Cadastro IP realizado com sucesso")
            try:
                lib_acess = liberar_acesso(1, mail, perfil)
            except ValidationError as error:
                raise HTTPException(status_code=400, detail=str(error))
        else:
            return cad_proj
        if lib_acess["error"] == None:
            etapas.append("Liberação de perfil realizada com sucesso")
            if len(etapas) == 3:
                session.commit()
                print("commit realizado com sucesso")
                return etapas
        else:
            return lib_acess
    except ValidationError as error:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(error))
