from app.models import db,usuarios,usuarios_ip
from .auth import controle_perfil
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

def cadastrar_em_lote(user,username,acesso):
    #nome,mail,senha,cpf,municipio,cargo,telefone,whatsapp,equipe,id_cod,id,username,acesso
    #controle de acesso
    controle = controle_perfil(username,acesso)
    if controle != True : return controle
    #cadastrar usuario impulso
    session = db.session
    def cadastro_impulso(nome,mail,senha,cpf):
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
            session.add(usuario)
            return {
                    "mensagem":"Usuário Impulso cadastrado com sucesso",
                    "error":None
                    }
        except Exception as error:
            session.rollback()
            #raise Exception({"mensagem":"Cadastro não efetuado"})
            return {
                "mensagem": error,
                "error": True
            }
    #cadastrar usuario IP
    def cadastro_ip(municipio,cargo,telefone,whatsapp,mail,equipe):
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
        except:
            return {"mensagem":"Inserção dos dados falhou","error":True}
        return {"mensagem":"dados cadastrados com sucesso","error":None}
    #liberar primeiro acesso
    def liberar_acesso(id_cod,id):
        #verificar se usuario nunca foi ativado
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        try:
            usuario_id= session.query(usuarios.Usuario).filter_by(**id_db).all()[0].perfil_ativo
            print(usuario_id)
            if usuario_id != None : return {"mensagem": "Usuário já realizou primeira ativação"}
        except Exception as error:
            print({"error" : [error]})
            return {"erros" : [error]}
        #ativar perfil
        try:
            session.query(usuarios.Usuario).filter_by(**id_db).update({"perfil_ativo" : True})
            return {"mensagem" : "Usuário ativado com sucesso","error":None}
        except Exception as error:
            print({"error" : [error]})
            return {"erros" : [error]}
    #primeira ativação de perfil
    def ativar_perfil(id_cod,id):
    #verificar se usuario nunca foi ativado
        id_db = {"mail":id} if id_cod == 1 else {"cpf":id}
        try:
            usuario_id= session.query(usuarios.Usuario).filter_by(**id_db).all()[0].perfil_ativo
            print(usuario_id)
            if usuario_id != None : return {"mensagem": "Usuário já realizou primeira ativação","error":True}
        except Exception as error:
            print({"error" : [error]})
            return {"erros" : [error]}
        #ativar perfil
        try:
            session.query(usuarios.Usuario).filter_by(**id_db).update({"perfil_ativo" : True})
            return {"mensagem" : "Usuário ativado com sucesso","error":None}
        except Exception as error:
            print({"error" : [error]})
            return {"erros" : [error]}

    cadastro_impulso(user.nome,user.mail,user.senha,user.cpf)

    cadastro_ip(user.municipio_uf,user.cargo,user.telefone,user.whatsapp,user.mail,user.equipe)

    liberar_acesso(1,user.mail)
