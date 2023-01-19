from app.models import db,usuarios,usuarios_ip,perfil_acesso,perfil_usuario
from .auth import controle_perfil
from passlib.context import CryptContext
from datetime import datetime
import uuid
from validate_docbr import CPF
cpf_verificador = CPF()
import re
from email_validator import validate_email, EmailNotValidError
session = db.session


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

def obter_id(email):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=email)
        res = query.all()
        return res[0].id if len(res)!=0 else {"mensagem":"E-mail não cadastrado"}
    except:
        return {"mensagem":"Error"}

def validador_de_cpf(cpf):
    return cpf_verificador.validate(cpf)

def consulta_cpf(cpf):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(cpf=cpf)
        res = query.all()
        if len(res)==0 or res == None:return True
    except:
        return {"mensagem":"CPF já cadastrado"}

def consulta_id_usuario(id):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(id=id)
        res = query.all()
        return True if len(res)==0 else {"mensagem":"E-mail já cadastrado"}
    except ValueError as e:
        return {"mensagem":e}

def verifica_mail(email):
    try:
      valid = validate_email(email)
      return True
    except EmailNotValidError as e:
      return {"mensagem":str(e)}

def cadastrar_usuario(nome,mail,senha,cpf):
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

def cadastrar_usuario_ip(municipio,cargo,telefone,whatsapp,mail,equipe):
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wp = True if whatsapp == '1' else False
    try:
        id_usuario = obter_id(mail)
        print(id_usuario)
        #validar municipio
        #validar cargo
        #formato telefone
    except :
        return {"mensagem":"Validação dos dados enviados não efetuada"}
    
    usuario_dados = usuarios_ip.UsuarioIP(
        id = str(uuid.uuid4()),
        municipio=municipio,
        cargo=cargo,
        telefone=telefone,
        whatsapp=wp,
        id_usuario=id_usuario,
        equipe=equipe,
        criacao_data=criacao_data,
        atualizacao_data=atualizacao_data
        )
    session = db.session
    session.add(usuario_dados)
    session.commit()
    return {"mensagem":"dados cadastrados com sucesso, apos a liberação do seu perfil de acesso você recebera no e-mail cadastro mensagem com o link para ativação do seu cadastro"}

#cadastrar usuario impulso
def cadastro_impulso(nome,mail,senha,cpf):
    try:
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
        if not cpf_verificador.validate(cpf): return {"mensagem":"CPF Invalido","error":True}
        if not validar_senha(senha)[1] : return validar_senha(senha)[0] 
        if verifica_mail(mail) != True: return verifica_mail(mail)
        if consulta_mail(mail) != True : return consulta_mail(mail)
        print(consulta_cpf(cpf) != True)
        print(consulta_cpf(cpf))
        if consulta_cpf(cpf) != True : return {"mensagem":"CPF invalido","error": True}

    except Exception as error:
        session.rollback()
        return {
            "mensagem": error,
            "error": True
        }
    try:
        session.add(usuario)
        return {
                "mensagem":"Usuário Impulso cadastrado com sucesso",
                "error":None
                }
    except Exception as error:
        session.rollback()
        return {
            "mensagem": error,
            "error": True
        }
#cadastrar usuario IP
def cadastro_ip(municipio,cargo,telefone,whatsapp,mail,equipe):
    try:
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        wp = True if whatsapp == '1' else False
        id_usuario = obter_id(mail)
        #validar municipio
        #validar cargo
        #formato telefone
    except :
        session.rollback()
        return {"mensagem":"Validação dos dados enviados não efetuada","error":True}
    try:
        usuario_dados = usuarios_ip.UsuarioIP(
            id = str(uuid.uuid4()),
            municipio=municipio,
            cargo=cargo,
            telefone=telefone,
            whatsapp=wp,
            id_usuario=id_usuario,
            equipe=equipe,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data
            )
        session.add(usuario_dados)
        return {"mensagem":"dados cadastrados com sucesso","error":None}

    except:
        session.rollback()
        return {"mensagem":"Inserção dos dados falhou","error":True}
#liberar primeiro acesso
def liberar_acesso(id_cod,id):
    #libera primeiro perfil apos cadastro
    #informar perfil liberado
    try:
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        res= session.query(usuarios.Usuario).filter_by(**id_db).all()
    except Exception as error:
        print({"error" : error})
        return error
    if res[0].perfil_ativo != None : return {"mensagem" : "Usuário já passou pela primeira liberação de perfil"}
    usuario_id= session.query(usuarios.Usuario).filter_by(**id_db).all()[0].id
    perfil_id= session.query(perfil_acesso.Perfil_lista).filter_by(perfil=6).all()[0].id #perfil 6 - IP
    novo_perfil = perfil_usuario.Perfil(
        id = str(uuid.uuid4()),
        usuario_id=usuario_id,
        perfil_id=perfil_id,
        criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        atualizacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    try:
        session.add(novo_perfil)
        return {"error": None }
    except Exception as error:
        print({"erros" : error})
        return error

#primeira ativação de perfil
def ativar_perfil(id_cod,id):
    #verificar se usuario nunca foi ativado
    id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
    try:
        usuario_id= session.query(usuarios.Usuario).filter_by(**id_db).all()[0].perfil_ativo
        print(usuario_id)
        if usuario_id != None : return {"mensagem": "Usuário já realizou primeira ativação","error":True}
    except Exception as error:
        session.rollback()
        return {"erros" : [error]}
    #ativar perfil
    try:
        session.query(usuarios.Usuario).filter_by(**id_db).update({"perfil_ativo" : True})
        session.commit()
        return {"mensagem" : "Usuário ativado com sucesso","error":None}
    except Exception as error:
        session.rollback()
        print({"error" : [error]})
        return {"erros" : [error]}

def cadastrar_em_lote(nome,mail,senha,cpf,municipio_uf,cargo,telefone,whatsapp,equipe,username,acesso):
    #controle de acesso
    controle = controle_perfil(username,acesso)
    if controle != True : return controle
    cad_impulso = cadastro_impulso(nome,mail,senha,cpf)
    etapas = []
    if (cad_impulso['error'] == None): 
        cad_ip = cadastro_ip(municipio_uf,cargo,telefone,whatsapp,mail,equipe)
        etapas.append("Cadastro Impulso realizado com sucesso")
    else:
        return cad_impulso

    if (cad_ip['error'] == None): 
        etapas.append("Cadastro IP realizado com sucesso")
        lib_acess = liberar_acesso(1,mail)
    else:
        return cad_ip

    if (lib_acess['error'] == None): 
        etapas.append("Liberação de acesso realizada com sucesso")
        ativar_user = ativar_perfil(1,mail)
    else:
        return lib_acess

    if (ativar_user['error'] == None): 
        etapas.append("Ativação de perfil realizada com sucesso")
        etapas.append("Usuario cadastrado com sucesso")
        if len(etapas) == 5 : 
            session.commit()
            print("commit realizado com sucesso")
        return etapas
    else:
        return ativar_user