from app.models import db,usuarios
from passlib.context import CryptContext
from datetime import datetime
import uuid
from validate_docbr import CPF
cpf_verificador = CPF()
import re
from email_validator import validate_email, EmailNotValidError

def validar_senha(senha):
    restricoes =[]
    if len(senha)<9: restricoes.append({"mensagem1":"Senha deve conter ao menos 8 caracteres"})
    if len(re.findall('[a-z]', senha))==0: restricoes.append({"mensagem2":"Senha deve conter letras minusculas"})
    if len(re.findall('[A-Z]', senha))==0: restricoes.append({"mensagem3":"Senha deve conter letras maiusculas"})
    if len(re.findall('[0-9]', senha))==0: restricoes.append({"mensagem4":"Senha deve conter numeros"})
    if len(re.findall('\W', senha))==0: restricoes.append({"mensagem4":"Senha deve conter caracteres especiais"})
    if len(re.findall('\s', senha))!=0: restricoes.append({"mensagem4":"Senha não deve conter espaços e quebras"})
    validacao=True if len(restricoes)==0 else False
    return restricoes,validacao

def consulta_mail(email):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=email)
        res = query.all()
        return True if len(res)==0 else {"mensagem":"E-mail já cadastrado"}
    except:
        return {"mensagem":"E-mail já cadastrado"}

def consulta_cpf(cpf):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(cpf=cpf)
        res = query.all()
        if len(res)==0 or res == None:return True
    except:
        return {"mensagem":"CPF já cadastrado"}


def verifica_mail(email):
    try:
      valid = validate_email(email)
      return True
    except EmailNotValidError as e:
      return {"mensagem":str(e)}

def cadastrar(nome,mail,senha,cpf):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuario = usuarios.Usuario(
        id = str(uuid.uuid4()),
        nome_usuario=nome,
        mail=mail,
        hash_senha=pwd_context.hash(senha),
        cpf=cpf,
        criacao_data=criacao_data,
        atualizacao_data=atualizacao_data
        )
    if not cpf_verificador.validate(cpf): return {"mensagem":"CPF Invalido"}
    if not validar_senha(senha)[1] : return validar_senha(senha)[0] 
    if verifica_mail(mail) != True: return verifica_mail(mail)
    if consulta_mail(mail) != True : return consulta_mail(mail)
    if consulta_cpf(cpf) != True : return consulta_cpf(cpf)
    
    try:
        session = db.session
        db.session.add(usuario)
        session.commit()
        return {"mensagem":"Usuario cadastrado com sucesso, apos a liberação do seu perfil de acesso você recebera no e-mail cadastro mensagem com o link para ativação do seu cadastro"}
    except:
        session.rollback()
        return {"mensagem":"Cadastro não efetuado"}