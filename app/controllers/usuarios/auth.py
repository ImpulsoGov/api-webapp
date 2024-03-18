import os
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from requests import session

from app.models import db
from app.models.usuarios import perfil_acesso, perfil_usuario, usuarios
import re

Usuarios = usuarios.Usuario
Perfil = perfil_usuario.Perfil
Perfil_lista = perfil_acesso.Perfil_lista

env_path = os.path.dirname(os.path.realpath(os.path.dirname(__file__))) + "/.env"
load_dotenv(dotenv_path=env_path)
# openssl rand -base64 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Usuario(BaseModel):
    id: str
    mail: str
    perfil: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verificar_senha(senha, hash_senha):
    return pwd_context.verify(senha, hash_senha)


def senha_hash(senha):
    print("------------- : senha+hash")
    print(senha)
    print(pwd_context.hash(senha))
    return pwd_context.hash(senha)


def get_user(cpf: str):
    print(cpf)
    try:
        res = (
            db.session.query(usuarios.Usuario)
            .filter_by(cpf=re.sub(r"\D", "", cpf))
            .all()
        )
        return res[0]
    except Exception as error:
        print({"error": error})
        return None


def get_perfil(cpf: str):
    try:
        res = (
            db.session.query(Perfil)
            .join(Perfil_lista)
            .join(Usuarios)
            .with_entities(
                Usuarios.id,
                Usuarios.mail,
                Usuarios.cpf,
                Usuarios.perfil_ativo,
                Usuarios.nome_usuario,
                Perfil_lista.perfil,
            )
            .filter_by(cpf=cpf)
            .all()
        )
        perfil = []
        for item in res:
            perfil.append(item["perfil"])
        user = {
            "id": res[0].id,
            "mail": res[0].mail,
            "cpf": res[0].cpf,
            "perfil_ativo": res[0].perfil_ativo,
            "nome_usuario": res[0].nome_usuario,
            "perfil": perfil,
        }
        return user
    except Exception as error:
        print({"erros": [error]})
        return {"erros": [error]}


def autenticar(cpf: str, senha: str):
    usuario = get_user(re.sub(r"\D", "", cpf))
    print(cpf, usuario)
    if usuario == None or usuario.cpf != re.sub(r"\D", "", cpf):
        return 1
    if usuario.perfil_ativo == False or usuario.perfil_ativo == None:
        return 3
    if not verificar_senha(senha, usuario.hash_senha):
        return 2
    return usuario.cpf


def criar_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credencial Invalida",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(cpf=token_data.username)
    if user is None:
        raise credentials_exception
    if user.perfil_ativo == False:
        user_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário Inativo",
            headers={"WWW-Authenticate": "Bearer"},
        )
        return user_exception
    return get_perfil(user.cpf)


def controle_perfil(perfil_usuario, perfil_rota):
    return (
        True
        if perfil_rota in perfil_usuario
        else {
            "mensagem": "Perfil de usuário com Privilégio insuficiente para essa rota"
        }
    )


def login(form_data: OAuth2PasswordRequestForm = Depends()):
    cpf = autenticar(form_data.username, form_data.password)
    print("-----------------cpf")
    print(cpf, form_data.username)
    if cpf != re.sub(r"\D", "", form_data.username):
        if cpf == 1:
            erro = "CPF Incorreto"
        elif cpf == 2:
            erro = "Senha Inválida"
        elif cpf == 3:
            erro = "Usuário Inativo"
        print("-----------------erro")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=erro,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = criar_token(data={"sub": cpf}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
