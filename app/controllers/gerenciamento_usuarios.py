from app.models import db,usuarios,perfil_acesso,perfil_usuario,ativar_usuario,usuarios_ip,recuperacao_senha
from app.controllers import recuperação_senha,auth,cadastro_usuarios
from datetime import datetime
import random,math
import uuid
session = db.session
Usuarios = usuarios.Usuario
UsuariosIP = usuarios_ip.UsuarioIP
Perfil = perfil_usuario.Perfil
Perfil_lista = perfil_acesso.Perfil_lista 
Ativar = ativar_usuario.Ativar
enviar_mail = recuperação_senha.enviar_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time

from dotenv import load_dotenv

env_path = os.path.dirname(os.path.realpath(__file__))+'/.env'
load_dotenv(dotenv_path=env_path)


def lista_usuarios_sem_liberacao(username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #Retorna todos os usuarios sem perfil
    try:
        res = db.session.query(Usuarios).with_entities(
                    Usuarios.mail,
                    Usuarios.cpf,
                    Usuarios.id,
        ).filter_by(perfil_ativo=None).all()
        return {"usuarios" : res}
    except:
        return None

def lista_usuarios(username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return {"erros" : [controle]}
    #Retorna lista com todos os usuarios ativos e respectivo perfil dados:(Nome,e-mail, perfil)
    try:
        res = db.session.query(
            Perfil
        ).join(Perfil_lista
        ).join(Usuarios
        ).with_entities(
            Usuarios.mail,
            Usuarios.cpf,
            Usuarios.nome_usuario,
            Perfil_lista.perfil
        ).filter_by(perfil_ativo=True
        ).all()
        return {"usuarios" : res}
    except Exception as error:
        print({"error" : error})
        return error

def cargo_nome(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #Informa dados cadastrais a partir do e-mail ou cpf do usuario
    #id_cod 1 para e-mail e 2 para cpf
    id_cod_ref = [1,2]
    if id_cod not in id_cod_ref : return {"erros" : ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail":id} if int(id_cod) == 1 else {"cpf":id}
    try:
        nome_usuario = db.session.query(Usuarios).with_entities(
                    Usuarios.nome_usuario,
                    Usuarios.id,
        ).filter_by(**id_db).all()
        cargo_usuario = db.session.query(UsuariosIP).with_entities(
                    UsuariosIP.cargo,
                    UsuariosIP.municipio,
                    UsuariosIP.equipe
        ).filter_by(id_usuario=nome_usuario[0].id).all()
        print(cargo_usuario)
        return {
                "cadastro" : [
                    {
                        "nome":nome_usuario[0].nome_usuario,
                        "id":nome_usuario[0].id,
                        "cargo":cargo_usuario[0].cargo,
                        "municipio":cargo_usuario[0].municipio,
                        "equipe":cargo_usuario[0].equipe
                    }
                ]}
    except Exception as error:
        print({"erros" : [error]})
        return error

def dados_usuarios(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #Informa dados cadastrais a partir do e-mail ou cpf do usuario
    #id_cod 1 para e-mail e 2 para cpf
    id_cod_ref = [1,2]
    if id_cod not in id_cod_ref : return {"erros" : ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail":id} if int(id_cod) == 1 else {"cpf":id}
    try:
        res = db.session.query(Usuarios).with_entities(
                    Usuarios.mail,
                    Usuarios.cpf,
                    Usuarios.id,
                    Usuarios.nome_usuario,
                    Usuarios.perfil_ativo,
                    Usuarios.criacao_data,
                    Usuarios.atualizacao_data,
        ).filter_by(**id_db).all()
        return {"cadastro" : res}
    except Exception as error:
        print({"erros" : [error]})
        return error

def add_perfil(id_cod,id,perfil,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #consultar perfis que o usuario já tem
    id_cod_ref = [1,2]
    if id_cod not in id_cod_ref : return {"erros" : ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
    try:
        res = db.session.query(
            Perfil
        ).join(Perfil_lista
        ).join(Usuarios
        ).with_entities(
            Usuarios.id,
            Usuarios.mail,
            Usuarios.cpf,
            Usuarios.nome_usuario,
            Perfil_lista.perfil
        ).filter_by(**id_db
        ).all()
        if len(res)==0 :return {"mensagem" : "Dados invalidos"}
    except Exception as error:
        print({"error" : error})
        return error
    #verficar se o usuario já possui o perfil a ser adicionado 
    for resultado in res:
        if resultado["perfil"] == perfil: return {"mensagem":"Usuário já possui perfil informado"}
    try:
        query = db.session.query(Perfil_lista).filter_by(perfil=perfil).all()
        query_perfil_id = query[0].id
    except Exception as error:
        print({"error" : error})
        return error

    #registra perfil a ser adicionado
    novo_perfil = Perfil(
        id = str(uuid.uuid4()),
        usuario_id=res[0].id,
        perfil_id=query_perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    try:
        session.add(novo_perfil)
        session.commit()
        return {"mensagem":"Perfil cadastrado com sucesso"}
    except:
        session.rollback()
        return {"mensagem":"Adição de perfil não efetuada"}

def get_perfil_usuarios(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #consultar perfis que o usuario já tem
    id_cod_ref = [1,2]
    if id_cod not in id_cod_ref : return {"erros" : ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
    try:
        res = db.session.query(
            Perfil
        ).join(Perfil_lista
        ).join(Usuarios
        ).with_entities(
            Usuarios.mail,
            Usuarios.nome_usuario,
            Perfil_lista.perfil,
            Perfil_lista.descricao
        ).filter_by(**id_db
        ).all()
        if len(res)==0 :return {"mensagem" : "Sem perfil de acesso atribuido"}
        return res
    except Exception as error:
        print({"error" : error})
        return error

def remove_perfil(id_cod,id,perfil,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #recebe e-mail ou cpf e perfil a ser removido
    #consultar perfis que o usuario já tem
    id_cod_ref = [1,2]
    if id_cod not in id_cod_ref : return {"erros" : ["id_cod invalido, insira 1 para e-mail e 2 para CPF"]}
    id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
    try:
        res = db.session.query(
            Perfil
        ).join(Perfil_lista
        ).join(Usuarios
        ).with_entities(
            Usuarios.id,
            Usuarios.mail,
            Usuarios.cpf,
            Usuarios.nome_usuario,
            Perfil_lista.perfil
        ).filter_by(**id_db
        ).all()
    except Exception as error:
        print({"error" : error})
        return error
    #verficar se o usuario já possui o perfil a ser excluido
    match = 0
    for resultado in res: 
        if str(resultado["perfil"]) == str(perfil): match += 1
    if match==0 : return {"mensagem":"Usuario não possui perfil informado"}
    perfil_usuario_id= str(res[0]["id"])
    perfil_id = session.query(Perfil_lista).filter_by(perfil=perfil).all()[0].id
    #verifca quantidade de perfis que o usuário possui
    if len(res)==1 : return {"mensagem" : "Usuário possui somente 1 perfil de acesso, para cancelar o acesso desse usuário utilize o recurso /suporte/ger_usuarios/desativa-usuario. Para trocar o perfil, adicione o perfil novo para então realizar a exclusão do perfil antigo."}
    #apagar perfil
    session.query(Perfil).filter_by(usuario_id=perfil_usuario_id,perfil_id=perfil_id).delete()
    session.commit()
    return {"mensagem" : "Perfil excluido com sucesso"}

def desativar_usuario(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #recebe e-mail ou cpf do usuario a ser desativado
    #verifica status do usuario
    try:
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        res= db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros" : [error]})
        return {"erros" : [error]}
    if res[0].perfil_ativo == None : return {"mensagem" : "Usuário não ativo, verifique o recurso de liberação de primeiro acesso"}
    if res[0].perfil_ativo == False : return {"mensagem" : "Usuário não ativo"}
    if res[0].perfil_ativo == True : 
        try:
            id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
            session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo" : False})
            session.commit()
            return {"mensagem" : "Usuário desativado com sucesso"}
        except Exception as error:
            print({"erros" : [error]})
            return {"erros" : [error]}

def reativar_usuario(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #recebe e-mail ou cpf do usuario a ser re-ativado
    try:
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        res= db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros" : [error]})
        return {"erros" : [error]}
    if res[0].perfil_ativo == None : return {"mensagem" : "Usuário não ativo, verifique o recurso de liberação de primeiro acesso"}
    if res[0].perfil_ativo == True : return {"mensagem" : "Usuário ativo"}
    if res[0].perfil_ativo == False : 
        try:
            id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
            session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo" : True})
            session.commit()
            return {"mensagem" : "Usuário ativado com sucesso"}
        except Exception as error:
            print({"erros" : [error]})
            return {"erros" : [error]}

def primeiro_acesso(id_cod,id,perfil,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #libera primeiro perfil apos cadastro, envia e-mail com codigo de ativação
    #informar perfil liberado
    try:
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        res= db.session.query(Usuarios).filter_by(**id_db).all()
    except Exception as error:
        print({"erros" : error})
        return error
    if res[0].perfil_ativo != None : return {"mensagem" : "Usuário já passou pela primeira liberação de perfil"}
    usuario_id= db.session.query(Usuarios).filter_by(**id_db).all()[0].id
    perfil_id= db.session.query(Perfil_lista).filter_by(perfil=perfil).all()[0].id
    novo_perfil = Perfil(
        id = str(uuid.uuid4()),
        usuario_id=usuario_id,
        perfil_id=perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    session.add(novo_perfil)
    #gerar e gravar codigo de ativacao
    try:
        codigo = str(uuid.uuid4())
        codigo_ativ_usuario = Ativar(codigo_ativacao=codigo,usuario_id=usuario_id)
        session.add(codigo_ativ_usuario)
        session.commit()
    except Exception as error:
        print({"erros" : [error]})
        return error
    #enviar e-mail com codigo de ativação
    mail= db.session.query(Usuarios).filter_by(**id_db).all()[0].mail
    url = '/ger_usuarios/ativacao-primeiro-acesso'
    mensagem = 'Codigo de ativação (campo : "codigo") '+codigo+' envie o codigo no endpoint '+url+' junto com e-mail ou CPF cadastrado (campo : "id")'
    #enviar_mail(mail,mensagem)
    return {"mensagem" : "Usuário recebeu perfil base informado com sucesso, para adicionar outros perfis utilize o recurso /ger_usuarios/add-perfil. O usuário ira receber e-mail com codigo de ativação, o usuário somente estará ativo após validação do codigo "}

def primeira_ativacao(id_cod,id,codigo,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #Recebe codigo de ativação,  ativa usuario
    #validar codigo
    try:
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        usuario_id= db.session.query(Usuarios).filter_by(**id_db).all()[0].id
        res= db.session.query(Ativar).filter_by(codigo_ativacao=codigo,usuario_id=usuario_id).all()
        if str(res[0].codigo_ativacao) != codigo or len(res)==0: return {"mensagem": "Codigo Invalido"}
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}
    #ativar perfil
    try:
        session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo" : True})
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}
    #apagar codigo de ativação
    session.query(Ativar).filter_by(usuario_id=usuario_id).delete()
    session.commit()
    return {"mensagem" : "Usuário ativado com sucesso"}

def primeira_ativacao_em_lote(id_cod,id,username,acesso):
    #controle de acesso
    controle = auth.controle_perfil(username,acesso)
    if controle != True : return controle
    #verificar se usuario nunca foi ativado
    id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
    try:
        usuario_id= db.session.query(Usuarios).filter_by(**id_db).all()[0].perfil_ativo
        print(usuario_id)
        if usuario_id != None : return {"mensagem": "Usuário já realizou primeira ativação"}
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}
    #ativar perfil
    try:
        session.query(Usuarios).filter_by(**id_db).update({"perfil_ativo" : True})
        session.commit()
        return {"mensagem" : "Usuário ativado com sucesso"}
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}

def verificar_mail(mail):
    try:
        res = db.session.query(Usuarios).filter_by(mail=mail).all()
        if len(res)<1 : return {"mensagem": "E-mail não cadastrado"}
        mail_db = res[0].mail
        if mail_db == None or mail != mail_db : return {"mensagem": "E-mail não cadastrado"}
        return True
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}

def consulta_primeiro_acesso(mail):
    try:
        res = db.session.query(Usuarios).filter_by(mail=mail).all()
        if len(res)<1 : return {
            "mensagem": "E-mail não cadastrado",
            "success" : False
            }
        mail_db = res[0].mail
        if mail_db == None or mail != mail_db : return {
            "mensagem": "E-mail não cadastrado",
            "success" : False
            }
        if res[0].hash_senha != None and res[0].perfil_ativo != None : return {
            "mensagem": "Usuário já realizou primeiro acesso",
            "success" : False
            }
        criar_codigo_recuperacao(mail)
        codigo = criar_codigo_recuperacao(mail)
        assunto = 'Código Criação de senha - Plataforma Impulso Previne'
        mensagem = 'Seu código de criação de senha é ' + str(codigo)
        enviar_mail(mail,assunto,mensagem)

        return {"success" : True}
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}

def criar_codigo_recuperacao(mail): 
    res = db.session.query(recuperacao_senha.Recuperar).filter_by(mail=mail).all()
    def gravar_codigo():
            codigo_recuperacao = math.floor(random.random() * 1000000)
            novo_codigo = recuperacao_senha.Recuperar(
                mail = mail,
                codigo_recuperacao = codigo_recuperacao,
                criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
            try:
                session.add(novo_codigo)
                session.commit()
                return codigo_recuperacao
            except Exception as error:
                print({"erros" : error})
                return error
    if len(res)>0 :
        time_diff = datetime.now() - res[0].criacao_data
        if time_diff.total_seconds() < 15*60 : 
            return res[0].codigo_recuperacao
        else:
            apagar_codigo_recuperacao(mail)
            codigo = gravar_codigo()
            return codigo  
    else:
        return gravar_codigo()

def apagar_codigo_recuperacao(mail):
    try:
        session.query(recuperacao_senha.Recuperar).filter(recuperacao_senha.Recuperar.mail == mail).delete()
        session.commit()
    except Exception as error:
        print({"erros" : error})

def apagar_codigo_recuperacao_tempo(mail):
    time.sleep(15*60)
    apagar_codigo_recuperacao(mail)

def enviar_mail(destinatario,assunto,texto):
    #enviar e-mail
    
    # Configuração
    host = 'smtp.gmail.com'
    port = 587
    user = os.getenv("MAIL")
    password = os.getenv("PASSWORD")

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = texto
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = destinatario
    email_msg['Subject'] = assunto
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()

def solicitar_nova_senha(mail):
    mail_check = verificar_mail(mail)
    if mail_check == True:
        codigo = criar_codigo_recuperacao(mail)
        assunto = 'Código de Recuperação - Plataforma Impulso Previne'
        mensagem = 'Seu código de recuperação de senha é ' + str(codigo)
        enviar_mail(mail,assunto,mensagem)
        return {"msg": "solicitação realizada com sucesso", "success": True}
    else:
        return {"msg": mail_check, "success": False}

def validar_codigo(codigo,mail):
    try:
        res = db.session.query(recuperacao_senha.Recuperar).filter_by(mail=mail).all()
        if len(res)<1 : return {"mensagem": "E-mail não cadastrado"}
        mail_db = res[0].mail
        codigo_db = str(res[0].codigo_recuperacao)
        if mail_db == None or mail != mail_db : return {"mensagem": "E-mail não cadastrado"}
        if codigo_db == None or codigo != codigo_db : return {"mensagem": "Codigo invalido"}
        return True
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}

def alterar_senha(mail,codigo,senha):
    try:
        codigo_valido = validar_codigo(codigo,mail)
        if codigo_valido != True: return codigo_valido
        validacao_senha = cadastro_usuarios.validar_senha(senha)
        if validacao_senha[1] != True : return validacao_senha[0]
        hash = auth.senha_hash(senha)
        session.query(Usuarios).filter(Usuarios.mail == mail).update({"hash_senha" : hash})
        session.commit()
        apagar_codigo_recuperacao(mail)
        return {"msg": "alteração realizada com sucesso", "success": True}
    except Exception as error:
        print({"error" : [error]})
        return {"erros" : [error]}
