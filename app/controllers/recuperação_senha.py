from app.models import db,recuperacao_senha,usuarios
import uuid
Recuperar = recuperacao_senha.Recuperar
Usuario = usuarios.Usuario
from app.controllers.auth import senha_hash
from app.controllers.cadastro_usuarios import validar_senha
session = db.session
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

env_path = os.path.dirname(os.path.realpath(__file__))+'/.env'
load_dotenv(dotenv_path=env_path)

def consulta_mail(email):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=email)
        res = query.all()
        return False if len(res)==0 else True
    except Exception as error: 
        print(error)
        return {"mensagem":"Operação não efetuada"}

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

def solicita_recuperacao(usuario_mail):
    #if usuario_mail != username : return {"mensagem" : "Somente o proprio usuário tem privilegios para solicitar alteração de senha"}
    #gerar codigo de recuperação uuid
    codigo = str(uuid.uuid4())
    #inseir na tabela usuario_mail codigo de alteração/recuperação de senha
    req = Recuperar(mail=usuario_mail,codigo_recuperacao=codigo)
    try:
        consulta = consulta_mail(usuario_mail)
        if consulta == False : return {"mensagem":"E-mail não cadastrado"}
        if consulta == True: 
            session.add(req)
            session.commit()
            #enviar codigo via e-mail
            url = '/suporte/usuarios/alterar-senha'
            exemplo = ''
            mensagem = 'Codigo de recuperação (campo : "codigo") '+codigo+' envie o codigo no endpoint '+url+' junto com e-mail cadastrado (campo : "mail") e nova senha (campo : "senha")  no corpo (form-data) da requisição, exemplo da requisição no endereço '+exemplo
            enviar_mail(usuario_mail,mensagem)
            return {"mensagem":"Solicitação efetuada com sucesso,você ira receber no e-mail cadastrado o codigo de recuperação e endpoint de cadastrar nova senha"}
    except Exception as error:
        print({"error" : error})
        session.rollback()
        return {"mensagem":"Solicitação não efetuada"}

def recuperar(usuario_mail,codigo_recuperacao,nova_senha):
    #bater usuario-mail e codigo de recuperação informados com os que constam no banco de dados
    query = session.query(Recuperar).filter_by(mail=usuario_mail,codigo_recuperacao=codigo_recuperacao)
    res = query.all()
    #validar senha
    if validar_senha(nova_senha)[1] == False:
        return {"erros" : validar_senha(nova_senha)[0]}
    #inserir a hash da nova senha no banco
    elif len(res)>0:
        hash = senha_hash(nova_senha)
        session.query(Usuario).filter(Usuario.mail == usuario_mail).update({"hash_senha" : hash})
        #apagar codigo de recuperação do banco de dados
        session.query(Recuperar).filter(Recuperar.mail == usuario_mail).delete()
        session.commit()
        return {"mensagem" : "Senha atualizada com sucesso"}
    else:
        return {"mensagem" : "Usuario ou codigo de recuperação invalido"}