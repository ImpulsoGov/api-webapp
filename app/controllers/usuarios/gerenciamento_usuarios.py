from app.controllers.usuarios import recuperação_senha, auth, cadastro_usuarios
from datetime import datetime
from sqlalchemy import func, exc
import random, math, uuid
from fastapi import HTTPException
from email_validator import validate_email, EmailNotValidError
from validate_docbr import CPF
import re
import uuid
from datetime import datetime
from typing import List, NoReturn, Union

from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import exc, func
from validate_docbr import CPF

from app.controllers.usuarios import auth, cadastro_usuarios, recuperação_senha
from app.controllers.usuarios.validacao_permissao import (
    PermissionError,
    validar_permissao,
)
from app.models import db
from app.models.usuarios import (
    ativar_usuario,
    perfil_acesso,
    perfil_usuario,
    recuperacao_senha,
    usuarios,
    usuarios_ip,
    usuarios_sm,
)
from twilio.rest import Client

session = db.session
Usuarios = usuarios.Usuario
UsuariosIP = usuarios_ip.UsuarioIP
Perfil = perfil_usuario.Perfil
Perfil_lista = perfil_acesso.Perfil_lista
Ativar = ativar_usuario.Ativar
enviar_mail = recuperação_senha.enviar_mail
UsuarioSM = usuarios_sm.UsuarioSM
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

env_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
load_dotenv(dotenv_path=env_path)

PERFIL_PERMITIDO_PARA_GERIR_USUARIOS = 2


class UsuarioIPAtualizado(BaseModel):
    id: str
    nome_usuario: str
    cpf: str
    mail: str
    municipio: str
    equipe: str
    cargo: str
    telefone: str
    municipio_id_sus: str
    perfil_ativo: Union[bool, None]


def lista_usuarios_sem_liberacao(username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # Retorna todos os usuarios sem perfil
    try:
        res = (
            db.session.query(Usuarios)
            .with_entities(
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.id,
            )
            .filter_by(perfil_ativo=None)
            .all()
        )
        return {"usuarios": res}
    except:
        return None


def lista_usuarios(username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return {"erros": [controle]}
    # Retorna lista com todos os usuarios ativos e respectivo perfil dados:(Nome,e-mail, perfil)
    try:
        res = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .with_entities(
                Usuarios.mail, Usuarios.cpf, Usuarios.nome_usuario, Perfil_lista.perfil
            )
            .filter_by(perfil_ativo=True)
            .all()
        )
        return {"usuarios": res}
    except Exception as error:
        print({"error": error})
        return error


def cargo_nome(id_cod, id):
    # Informa dados cadastrais a partir do e-mail ou cpf do usuario
    # id_cod 1 para e-mail e 2 para cpf
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if int(id_cod) == 1 else {"cpf": id}
    try:
        perfil = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .filter_by(**id_db)
            .join(UsuariosIP)
            .with_entities(
                func.array_agg(func.distinct(Perfil_lista.perfil)).label("perfis"),
                Usuarios.nome_usuario.label("nome"),
                Usuarios.id,
                UsuariosIP.cargo,
                UsuariosIP.municipio,
                UsuariosIP.equipe,
                UsuariosIP.municipio_id_sus,
            )
            .group_by(
                Usuarios.nome_usuario,
                Usuarios.id,
                UsuariosIP.cargo,
                UsuariosIP.municipio,
                UsuariosIP.equipe,
                UsuariosIP.municipio_id_sus,
            )
            .all()
        )
        return {"cadastro": perfil}
    except Exception as error:
        print({"erros": [error]})
        return error


def obter_dados_usuarioSM(id_cod, id):
    # Informa dados cadastrais a partir do e-mail ou cpf do usuario
    # id_cod 1 para e-mail e 2 para cpf
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if int(id_cod) == 1 else {"cpf": id}
    try:
        perfil = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .filter_by(**id_db)
            .join(UsuarioSM)
            .with_entities(
                func.array_agg(func.distinct(Perfil_lista.perfil)).label("perfis"),
                Usuarios.nome_usuario.label("nome"),
                Usuarios.id,
                UsuarioSM.cargo_id,
                UsuarioSM.municipio_id_ibge,
                UsuarioSM.unidade_saude,
            )
            .group_by(
                Usuarios.nome_usuario,
                Usuarios.id,
                UsuarioSM.cargo_id,
                UsuarioSM.municipio_id_ibge,
                UsuarioSM.unidade_saude,
            )
            .all()
        )
        return {"cadastro": perfil}
    except Exception as error:
        print({"erros": [error]})
        return error


def dados_usuarios(id_cod, id, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # Informa dados cadastrais a partir do e-mail ou cpf do usuario
    # id_cod 1 para e-mail e 2 para cpf
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if int(id_cod) == 1 else {"cpf": id}
    try:
        res = (
            db.session.query(Usuarios)
            .with_entities(
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.id,
                Usuarios.nome_usuario,
                Usuarios.perfil_ativo,
                Usuarios.criacao_data,
                Usuarios.atualizacao_data,
            )
            .filter_by(**id_db)
            .all()
        )
        return {"cadastro": res}
    except Exception as error:
        print({"erros": [error]})
        return error


def add_perfil(id_cod, id, perfil, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # consultar perfis que o usuario já tem
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
    try:
        res = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .with_entities(
                Usuarios.id,
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.nome_usuario,
                Perfil_lista.perfil,
            )
            .filter_by(**id_db)
            .all()
        )
        if len(res) == 0:
            return {"mensagem": "Dados invalidos"}
    except Exception as error:
        print({"error": error})
        return error
    # verficar se o usuario já possui o perfil a ser adicionado
    for resultado in res:
        if resultado["perfil"] == perfil:
            return {"mensagem": "Usuário já possui perfil informado"}
    try:
        query = db.session.query(Perfil_lista).filter_by(perfil=perfil).all()
        query_perfil_id = query[0].id
    except Exception as error:
        print({"error": error})
        return error

    # registra perfil a ser adicionado
    novo_perfil = Perfil(
        id=str(uuid.uuid4()),
        usuario_id=res[0].id,
        perfil_id=query_perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    try:
        session.add(novo_perfil)
        session.commit()
        return {"mensagem": "Perfil cadastrado com sucesso"}
    except:
        session.rollback()
        return {"mensagem": "Adição de perfil não efetuada"}


def get_perfil_usuarios(id_cod, id, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # consultar perfis que o usuario já tem
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
    try:
        res = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .with_entities(
                Usuarios.mail,
                Usuarios.nome_usuario,
                Perfil_lista.perfil,
                Perfil_lista.descricao,
            )
            .filter_by(**id_db)
            .all()
        )
        if len(res) == 0:
            return {"mensagem": "Sem perfil de acesso atribuido"}
        return res
    except Exception as error:
        print({"error": error})
        return error


def remove_perfil(id_cod, id, perfil, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # recebe e-mail ou cpf e perfil a ser removido
    # consultar perfis que o usuario já tem
    id_cod_ref = [1, 2]
    if id_cod not in id_cod_ref:
        return {"erros": ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
    try:
        res = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .with_entities(
                Usuarios.id,
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.nome_usuario,
                Perfil_lista.perfil,
            )
            .filter_by(**id_db)
            .all()
        )
    except Exception as error:
        print({"error": error})
        return error
    # verficar se o usuario já possui o perfil a ser excluido
    match = 0
    for resultado in res:
        if str(resultado["perfil"]) == str(perfil):
            match += 1
    if match == 0:
        return {"mensagem": "Usuario não possui perfil informado"}
    perfil_usuario_id = str(res[0]["id"])
    perfil_id = session.query(Perfil_lista).filter_by(perfil=perfil).all()[0].id
    # verifca quantidade de perfis que o usuário possui
    if len(res) == 1:
        return {
            "mensagem": "Usuário possui somente 1 perfil de acesso, para cancelar o acesso desse usuário utilize o recurso /suporte/ger_usuarios/desativa-usuario. Para trocar o perfil, adicione o perfil novo para então realizar a exclusão do perfil antigo."
        }
    # apagar perfil
    session.query(Perfil).filter_by(
        usuario_id=perfil_usuario_id, perfil_id=perfil_id
    ).delete()
    session.commit()
    return {"mensagem": "Perfil excluido com sucesso"}


def desativar_usuario(id_cod, id, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # recebe e-mail ou cpf do usuario a ser desativado
    # verifica status do usuario
    try:
        id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
        res = db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros": [error]})
        return {"erros": [error]}
    if res[0].perfil_ativo == None:
        return {
            "mensagem": "Usuário não ativo, verifique o recurso de liberação de primeiro acesso"
        }
    if res[0].perfil_ativo == False:
        return {"mensagem": "Usuário não ativo"}
    if res[0].perfil_ativo == True:
        try:
            id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
            session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo": False})
            session.commit()
            return {"mensagem": "Usuário desativado com sucesso"}
        except Exception as error:
            print({"erros": [error]})
            return {"erros": [error]}


def reativar_usuario(id_cod, id, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # recebe e-mail ou cpf do usuario a ser re-ativado
    try:
        id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
        res = db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros": [error]})
        return {"erros": [error]}
    if res[0].perfil_ativo == None:
        return {
            "mensagem": "Usuário não ativo, verifique o recurso de liberação de primeiro acesso"
        }
    if res[0].perfil_ativo == True:
        return {"mensagem": "Usuário ativo"}
    if res[0].perfil_ativo == False:
        try:
            id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
            session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo": True})
            session.commit()
            return {"mensagem": "Usuário ativado com sucesso"}
        except Exception as error:
            print({"erros": [error]})
            return {"erros": [error]}


def primeiro_acesso(id_cod, id, perfil, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # libera primeiro perfil apos cadastro, envia e-mail com codigo de ativação
    # informar perfil liberado
    try:
        id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
        res = db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros": error})
        return error
    if res[0].perfil_ativo != None:
        return {"mensagem": "Usuário já passou pela primeira liberação de perfil"}
    usuario_id = db.session.query(Usuarios).filter_by(**id_db).all()[0].id
    perfil_id = db.session.query(Perfil_lista).filter_by(perfil=perfil).all()[0].id
    novo_perfil = Perfil(
        id=str(uuid.uuid4()),
        usuario_id=usuario_id,
        perfil_id=perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    session.add(novo_perfil)
    # gerar e gravar codigo de ativacao
    try:
        codigo = str(uuid.uuid4())
        codigo_ativ_usuario = Ativar(codigo_ativacao=codigo, usuario_id=usuario_id)
        session.add(codigo_ativ_usuario)
        session.commit()
    except Exception as error:
        print({"erros": [error]})
        return error
    # enviar e-mail com codigo de ativação
    mail = db.session.query(Usuarios).filter_by(**id_db).all()[0].mail
    url = "/ger_usuarios/ativacao-primeiro-acesso"
    mensagem = (
        'Codigo de ativação (campo : "codigo") '
        + codigo
        + " envie o codigo no endpoint "
        + url
        + ' junto com e-mail ou CPF cadastrado (campo : "id")'
    )
    # enviar_mail(mail,mensagem)
    return {
        "mensagem": "Usuário recebeu perfil base informado com sucesso, para adicionar outros perfis utilize o recurso /ger_usuarios/add-perfil. O usuário ira receber e-mail com codigo de ativação, o usuário somente estará ativo após validação do codigo "
    }


def primeira_ativacao(id_cod, id, codigo, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # Recebe codigo de ativação,  ativa usuario
    # validar codigo
    try:
        id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
        usuario_id = db.session.query(Usuarios).filter_by(**id_db).all()[0].id
        res = (
            db.session.query(Ativar)
            .filter_by(codigo_ativacao=codigo, usuario_id=usuario_id)
            .all()
        )
        if str(res[0].codigo_ativacao) != codigo or len(res) == 0:
            return {"mensagem": "Codigo Invalido"}
    except Exception as error:
        print({"error": [error]})
        return {"erros": [error]}
    # ativar perfil
    try:
        session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo": True})
    except Exception as error:
        print({"error": [error]})
        return {"erros": [error]}
    # apagar codigo de ativação
    session.query(Ativar).filter_by(usuario_id=usuario_id).delete()
    session.commit()
    return {"mensagem": "Usuário ativado com sucesso"}


def primeira_ativacao_em_lote(id_cod, id, username, acesso):
    # controle de acesso
    controle = auth.controle_perfil(username, acesso)
    if controle != True:
        return controle
    # verificar se usuario nunca foi ativado
    id_db = {"mail": id} if id_cod == 1 else {"cpf": id}
    try:
        usuario_id = db.session.query(Usuarios).filter_by(**id_db).all()[0].perfil_ativo
        print(usuario_id)
        if usuario_id != None:
            return {"mensagem": "Usuário já realizou primeira ativação"}
    except Exception as error:
        print({"error": [error]})
        return {"erros": [error]}
    # ativar perfil
    try:
        session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo": True})
        session.commit()
        return {"mensagem": "Usuário ativado com sucesso"}
    except Exception as error:
        print({"error": [error]})
        return {"erros": [error]}


def verificar_mail(mail):
    try:
        res = db.session.query(Usuarios).filter_by(mail=mail).all()
        if len(res) < 1:
            return {"mensagem": "E-mail não cadastrado"}
        mail_db = res[0].mail
        if mail_db == None or mail != mail_db:
            return {"mensagem": "E-mail não cadastrado"}
        return True
    except Exception as error:
        print({"error": [error]})
        return {"erros": [error]}


def verificar_cpf(cpf):
    try:
        res = db.session.query(Usuarios).filter_by(cpf=cpf).all()
        if len(res) < 1:
            return {
                "mensagem": "CPF digitado não cadastrado ou inválido.",
                "success": False,
            }
        cpf_db = res[0].cpf
        if cpf_db == None or cpf != cpf_db:
            return {
                "mensagem": "CPF digitado não cadastrado ou inválido.",
                "success": False,
            }
        telefone_usuario = (
            db.session.query(UsuariosIP)
            .filter_by(id_usuario=res[0].id)
            .all()[0]
            .telefone
        )

        return {"success": True, "telefone": telefone_usuario[7:11]}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def validar_cpf_primeiro_acesso(cpf):
    try:
        res = db.session.query(Usuarios).filter_by(cpf=cpf).all()
        if len(res) < 1:
            return {
                "mensagem": "CPF digitado não cadastrado ou inválido.",
                "success": False,
            }
        cpf_db = res[0].cpf
        if cpf_db == None or cpf != cpf_db:
            return {
                "mensagem": "CPF digitado não cadastrado ou inválido.",
                "success": False,
            }
        if res[0].hash_senha != None and res[0].perfil_ativo != None:
            return {
                "mensagem": "<div>Esse CPF já possui senha cadastrada. Volte e clique em Entrar. <br/>Precisa de ajuda nessa etapa? <a href='https://bit.ly/login-whatsapp-apoio' style='color: #FFF' target='_blank'>Clique aqui.</a></div>",
                "success": False,
            }
        usuario_ip = db.session.query(UsuariosIP).filter_by(id_usuario=res[0].id).all()
        if len(usuario_ip) < 1:
            return {
                "mensagem": "CPF digitado não cadastrado ou inválido.",
                "success": False,
            }

        telefone_usuario = usuario_ip[0].telefone
        return {"success": True, "telefone": telefone_usuario[7:11]}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def consulta_primeiro_acesso(cpf):
    try:
        res = db.session.query(Usuarios).filter_by(cpf=cpf).all()
        telefone_usuario = (
            db.session.query(UsuariosIP)
            .filter_by(id_usuario=res[0].id)
            .all()[0]
            .telefone
        )
        criar_codigo_recuperacao(res[0].mail)
        codigo = criar_codigo_recuperacao(res[0].mail)
        mensagem = (
            "ImpulsoPrevine: Esse é o seu código de verificação para criação de senha - "
            + str(codigo)
        )
        enviar_sms(telefone_usuario, mensagem)
        return {"success": True, "telefone": telefone_usuario[7:11]}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def criar_codigo_recuperacao(mail):
    res = db.session.query(recuperacao_senha.Recuperar).filter_by(mail=mail).all()
    cpf = db.session.query(Usuarios).filter_by(mail=mail).all()[0].cpf

    def gravar_codigo():
        codigo_recuperacao = math.floor(random.random() * 1000000)
        novo_codigo = recuperacao_senha.Recuperar(
            mail=mail,
            cpf=cpf,
            codigo_recuperacao=codigo_recuperacao,
            criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        try:
            session.add(novo_codigo)
            session.commit()
            return codigo_recuperacao
        except Exception as error:
            print({"erros": error})
            return error

    if len(res) > 0:
        time_diff = datetime.now() - res[0].criacao_data
        if time_diff.total_seconds() < 15 * 60:
            return res[0].codigo_recuperacao
        else:
            apagar_codigo_recuperacao(mail)
            codigo = gravar_codigo()
            return codigo
    else:
        return gravar_codigo()


def enviar_sms(telefone_usuario, mensagem):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensagem,
        from_=os.environ["TWILIO_TELEFONE_IMPULSO"],
        to="+55" + telefone_usuario,
    )
    # GRAVAR REGISTRO DA MENSAGEM ENVIADA
    return message.sid


def apagar_codigo_recuperacao(mail):
    try:
        session.query(recuperacao_senha.Recuperar).filter(
            recuperacao_senha.Recuperar.mail == mail
        ).delete()
        session.commit()
    except Exception as error:
        print({"erros": error})


def apagar_codigo_recuperacao_tempo(mail):
    time.sleep(2 * 60)
    apagar_codigo_recuperacao(mail)


def enviar_mail(destinatario, assunto, texto):
    # enviar e-mail

    # Configuração
    host = "smtp.gmail.com"
    port = 587
    user = os.getenv("MAIL")
    password = os.getenv("PASSWORD")

    # Criando objeto
    print("Criando objeto servidor...")
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print("Login...")
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = texto
    print("Criando mensagem...")
    email_msg = MIMEMultipart()
    email_msg["From"] = user
    email_msg["To"] = destinatario
    email_msg["Subject"] = assunto
    print("Adicionando texto...")
    email_msg.attach(MIMEText(message, "plain"))

    # Enviando mensagem
    print("Enviando mensagem...")
    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    print("Mensagem enviada!")
    server.quit()


def solicitar_nova_senha(cpf):
    try:
        res = db.session.query(Usuarios).filter_by(cpf=cpf).all()
        telefone_usuario = (
            db.session.query(UsuariosIP)
            .filter_by(id_usuario=res[0].id)
            .all()[0]
            .telefone
        )
        criar_codigo_recuperacao(res[0].mail)
        codigo = criar_codigo_recuperacao(res[0].mail)
        mensagem = (
            "ImpulsoPrevine: Esse é o seu código de verificação para criação de senha - "
            + str(codigo)
        )
        enviar_sms(telefone_usuario, mensagem)
        return {"success": True, "telefone": telefone_usuario[7:11]}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def validar_codigo(codigo, cpf):
    try:
        res = db.session.query(recuperacao_senha.Recuperar).filter_by(cpf=cpf).all()
        if len(res) < 1:
            return {"mensagem": "CPF não cadastrado", "success": False}
        cpf_db = res[0].cpf
        codigo_db = str(res[0].codigo_recuperacao)
        if cpf_db == None or cpf != cpf_db:
            return {"mensagem": "CPF não cadastrado", "success": False}
        if codigo_db == None or codigo != codigo_db:
            return {
                "mensagem": "Código digitado é inválido, tente novamente.",
                "success": False,
            }
        return {"success": True}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def alterar_senha(cpf, codigo, senha):
    try:
        codigo_valido = validar_codigo(codigo, cpf)
        if codigo_valido["success"] != True:
            return codigo_valido
        validacao_senha = cadastro_usuarios.validar_senha(senha)
        if validacao_senha[1] != True:
            return validacao_senha[0]
        hash = auth.senha_hash(senha)
        session.query(Usuarios).filter(Usuarios.cpf == cpf).update({"hash_senha": hash})
        session.commit()
        apagar_codigo_recuperacao(cpf)
        return {"msg": "alteração realizada com sucesso", "success": True}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def senha_primeiro_acesso(cpf, codigo, senha):
    try:
        alterarSenha = alterar_senha(cpf, codigo, senha)
        try:
            if alterarSenha["success"] != True:
                return alterarSenha
        except:
            return alterarSenha
        ativarPerfil = cadastro_usuarios.ativar_perfil(2, cpf)
        try:
            if ativarPerfil["error"] != None:
                return ativarPerfil
        except:
            return ativarPerfil
        return {"msg": "alteração realizada com sucesso", "success": True}
    except Exception as error:
        print({"error": [error]})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


def listar_usuarios_cadastrados_ip(perfis_usuario_autenticado: list):
    try:
        validar_permissao(
            perfis_usuario=perfis_usuario_autenticado,
            perfil_permitido=PERFIL_PERMITIDO_PARA_GERIR_USUARIOS,
        )

        usuarios_cadastrados = (
            session.query(Usuarios)
            .join(UsuariosIP)
            .join(Perfil)
            .join(Perfil_lista)
            .with_entities(
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.nome_usuario,
                Usuarios.perfil_ativo,
                UsuariosIP.id_usuario,
                UsuariosIP.municipio,
                UsuariosIP.cargo,
                UsuariosIP.telefone,
                UsuariosIP.equipe,
                UsuariosIP.municipio_id_sus,
                func.array_agg(func.distinct(Perfil_lista.descricao)).label(
                    "autorizacoes"
                ),
            )
            .filter(UsuariosIP.municipio.isnot(None))
            .group_by(
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.nome_usuario,
                Usuarios.perfil_ativo,
                UsuariosIP.id_usuario,
                UsuariosIP.municipio,
                UsuariosIP.cargo,
                UsuariosIP.telefone,
                UsuariosIP.equipe,
                UsuariosIP.municipio_id_sus,
            )
            .all()
        )

        return usuarios_cadastrados
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=(str(error)))
    except Exception as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def encontrar_usuario_por_id(id: str) -> Union[usuarios.Usuario, NoReturn]:
    usuario_encontrado = session.query(Usuarios).filter_by(id=id).first()

    if not usuario_encontrado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario_encontrado


def encontrar_usuario_ip_por_id(
    id: str,
) -> Union[usuarios_ip.UsuarioIP, NoReturn]:
    usuario_encontrado = session.query(UsuariosIP).filter_by(id_usuario=id).first()

    if not usuario_encontrado:
        raise HTTPException(
            status_code=404, detail="Usuário não encontrado na plataforma IP"
        )

    return usuario_encontrado


def validar_email(email: str) -> Union[None, NoReturn]:
    try:
        validate_email(email)

    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Formato de e-mail inválido")


def checar_se_novo_email_existe(email: str) -> Union[None, NoReturn]:
    usuario_encontrado = session.query(Usuarios).filter_by(mail=email).first()

    if usuario_encontrado and email != usuario_encontrado.mail:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")


def validar_cpf(cpf: str) -> Union[None, NoReturn]:
    cpf_esta_valido = CPF().validate(cpf)

    if not cpf_esta_valido:
        raise HTTPException(status_code=400, detail="CPF inválido")


def validar_telefone(telefone: str) -> Union[None, NoReturn]:
    telefone_regex = "^\d{10,11}$"
    resultado = re.search(telefone_regex, telefone)

    if resultado is None:
        raise HTTPException(status_code=400, detail="Formato de telefone inválido")


def atualizar_cadastro_geral(
    id: str, nome: str, cpf: str, mail: str, perfil_ativo: Union[bool, None] = None
) -> usuarios.Usuario:
    validar_email(email=mail)
    checar_se_novo_email_existe(email=mail)
    validar_cpf(cpf=cpf)

    usuario_encontrado = encontrar_usuario_por_id(id=id)

    usuario_encontrado.nome_usuario = nome
    usuario_encontrado.cpf = cpf
    usuario_encontrado.mail = mail
    usuario_encontrado.atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Só atualiza o campo perfil_ativo se o usuário já realizou primeiro acesso
    # (possui perfil_ativo diferente de None) e o perfil_ativo recebido para
    # atualizar é diferente de None
    if usuario_encontrado.perfil_ativo is not None and perfil_ativo is not None:
        usuario_encontrado.perfil_ativo = perfil_ativo

    return usuario_encontrado


def atualizar_cadastro_ip(
    id: str,
    municipio: str,
    equipe: str,
    cargo: str,
    telefone: str,
    municipio_id_sus: str,
) -> usuarios_ip.UsuarioIP:
    validar_telefone(telefone=telefone)

    usuario_encontrado = encontrar_usuario_ip_por_id(id=id)

    usuario_encontrado.municipio = municipio
    usuario_encontrado.municipio_id_sus = municipio_id_sus
    usuario_encontrado.equipe = equipe
    usuario_encontrado.cargo = cargo
    usuario_encontrado.telefone = telefone
    usuario_encontrado.atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return usuario_encontrado


def atualizar_cadastro_geral_e_ip(
    dados_usuario: UsuarioIPAtualizado, perfis_usuario_autenticado: list
):
    try:
        validar_permissao(
            perfis_usuario=perfis_usuario_autenticado,
            perfil_permitido=PERFIL_PERMITIDO_PARA_GERIR_USUARIOS,
        )

        usuario_atualizado = atualizar_cadastro_geral(
            id=dados_usuario["id"],
            nome=dados_usuario["nome_usuario"],
            cpf=dados_usuario["cpf"],
            mail=dados_usuario["mail"],
            perfil_ativo=dados_usuario["perfil_ativo"],
        )
        usuario_ip_atualizado = atualizar_cadastro_ip(
            id=dados_usuario["id"],
            municipio=dados_usuario["municipio"],
            equipe=dados_usuario["equipe"],
            cargo=dados_usuario["cargo"],
            telefone=dados_usuario["telefone"],
            municipio_id_sus=dados_usuario["municipio_id_sus"],
        )

        session.commit()

        return {
            "id_usuario": usuario_atualizado.id,
            "nome_usuario": usuario_atualizado.nome_usuario,
            "cpf": usuario_atualizado.cpf,
            "mail": usuario_atualizado.mail,
            "municipio": usuario_ip_atualizado.municipio,
            "equipe": usuario_ip_atualizado.equipe,
            "cargo": usuario_ip_atualizado.cargo,
            "telefone": usuario_ip_atualizado.telefone,
            "perfil_ativo": usuario_atualizado.perfil_ativo,
            "municipio_id_sus": usuario_ip_atualizado.municipio_id_sus,
            "whatsapp": usuario_ip_atualizado.whatsapp,
        }
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=(str(error)))
    except HTTPException as error:
        session.rollback()

        raise error
    except Exception as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def adicionar_novo_perfil_para_usuario(perfil_id: str, usuario_id: str):
    novo_perfil = Perfil(
        id=uuid.uuid4(),
        usuario_id=usuario_id,
        perfil_id=perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    session.add(novo_perfil)


def atualizar_perfis_usuario(
    usuario_id: str, perfis_ids: List[str], perfis_usuario_autenticado: list
):
    try:
        validar_permissao(
            perfis_usuario=perfis_usuario_autenticado,
            perfil_permitido=PERFIL_PERMITIDO_PARA_GERIR_USUARIOS,
        )

        perfis_cadastrados = (
            session.query(Perfil.perfil_id).filter_by(usuario_id=usuario_id).all()
        )

        perfis_ids_cadastrados = set(
            [str(perfil.perfil_id) for perfil in perfis_cadastrados]
        )

        perfis_ids_a_adicionar = set(perfis_ids).difference(perfis_ids_cadastrados)

        for perfil_id in perfis_ids_a_adicionar:
            adicionar_novo_perfil_para_usuario(
                perfil_id=perfil_id, usuario_id=usuario_id
            )

        perfis_ids_a_remover = set(perfis_ids_cadastrados).difference(perfis_ids)

        perfis_a_remover = (
            session.query(Perfil)
            .filter(Perfil.perfil_id.in_(list(perfis_ids_a_remover)))
            .filter(Perfil.usuario_id == usuario_id)
            .all()
        )

        for perfil in perfis_a_remover:
            session.delete(perfil)

        session.commit()

        return (
            session.query(Perfil_lista.id, Perfil_lista.descricao)
            .filter(Perfil_lista.id.in_(perfis_ids))
            .all()
        )
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=(str(error)))
    except Exception as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


def listar_perfis_de_acesso(perfis_usuario_autenticado: list):
    try:
        validar_permissao(
            perfis_usuario=perfis_usuario_autenticado,
            perfil_permitido=PERFIL_PERMITIDO_PARA_GERIR_USUARIOS,
        )

        perfis_de_acesso = session.query(Perfil_lista.id, Perfil_lista.descricao).all()

        return perfis_de_acesso
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=(str(error)))
    except Exception as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )


class CadastroUsuario(BaseModel):
    nome_usuario: str
    mail: str
    cpf: str


def criar_usuario_geral(dados_cadastro: CadastroUsuario):
    novo_usuario = Usuarios(
        id=uuid.uuid4(),
        nome_usuario=dados_cadastro["nome_usuario"],
        mail=dados_cadastro["mail"],
        cpf=dados_cadastro["cpf"],
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    return novo_usuario


class CadastroUsuarioIP(BaseModel):
    id_usuario: str
    municipio: str
    cargo: str
    telefone: str
    equipe: str
    whatsapp: bool
    municipio_id_sus: str


def criar_usuario_ip(dados_cadastro: CadastroUsuarioIP):
    novo_usuario_ip = UsuariosIP(
        id=uuid.uuid4(),
        id_usuario=dados_cadastro["id_usuario"],
        municipio=dados_cadastro["municipio"],
        municipio_id_sus=dados_cadastro["municipio_id_sus"],
        cargo=dados_cadastro["cargo"],
        telefone=dados_cadastro["telefone"],
        equipe=dados_cadastro["equipe"],
        whatsapp=dados_cadastro["whatsapp"],
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    return novo_usuario_ip


class DadosCadastro(BaseModel):
    nome_usuario: str
    mail: str
    cpf: str
    municipio: str
    cargo: str
    telefone: str
    equipe: str
    whatsapp: str
    municipio_id_sus: str


def cadastrar_usuario_geral_e_ip(
    dados_cadastro: DadosCadastro, perfis_usuario_autenticado: list
):
    try:
        validar_permissao(
            perfis_usuario=perfis_usuario_autenticado,
            perfil_permitido=PERFIL_PERMITIDO_PARA_GERIR_USUARIOS,
        )
        validar_email(dados_cadastro["mail"])
        validar_cpf(dados_cadastro["cpf"])
        validar_telefone(dados_cadastro["telefone"])

        novo_usuario = criar_usuario_geral(
            {
                "nome_usuario": dados_cadastro["nome_usuario"],
                "mail": dados_cadastro["mail"],
                "cpf": dados_cadastro["cpf"],
            }
        )

        novo_usuario_ip = criar_usuario_ip(
            {
                "id_usuario": novo_usuario.id,
                "municipio": dados_cadastro["municipio"],
                "municipio_id_sus": dados_cadastro["municipio_id_sus"],
                "cargo": dados_cadastro["cargo"],
                "telefone": dados_cadastro["telefone"],
                "equipe": dados_cadastro["equipe"],
                "whatsapp": True if dados_cadastro["whatsapp"] == "1" else False,
            }
        )

        session.add(novo_usuario)
        session.add(novo_usuario_ip)
        session.commit()

        return {
            "id_usuario": novo_usuario.id,
            "nome_usuario": novo_usuario.nome_usuario,
            "cpf": novo_usuario.cpf,
            "mail": novo_usuario.mail,
            "municipio": novo_usuario_ip.municipio,
            "municipio_id_sus": novo_usuario_ip.municipio_id_sus,
            "equipe": novo_usuario_ip.equipe,
            "cargo": novo_usuario_ip.cargo,
            "telefone": novo_usuario_ip.telefone,
            "whatsapp": novo_usuario_ip.whatsapp,
            "perfil_ativo": novo_usuario.perfil_ativo,
        }
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=(str(error)))
    except HTTPException as error:
        session.rollback()

        raise error
    except Exception as error:
        session.rollback()

        print({"error": str(error)})

        raise HTTPException(
            status_code=500,
            detail=("Internal Server Error"),
        )
