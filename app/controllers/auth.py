from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from models import db,usuarios
import os
from dotenv import load_dotenv

env_path = os.path.dirname(os.path.realpath(__file__))+'/.env'
load_dotenv(dotenv_path=env_path)

# openssl rand -base64 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

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
    return pwd_context.hash(senha)

def get_user(mail: str):
    try:
        query = db.session.query(usuarios.Usuario).filter_by(mail=mail)
        res = query.all()
        return res[0]
    except:
        return None

def autenticar(mail: str, senha: str):
    usuario = get_user(mail)
    if usuario==None or usuario.mail != mail:return 1
    if not verificar_senha(senha, usuario.hash_senha):return 2
    return usuario.mail

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
    user = get_user(mail=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def login(form_data: OAuth2PasswordRequestForm = Depends()):
    mail = autenticar(form_data.username, form_data.password)
    if mail != form_data.username:
        erro = "E-mail Incorreto" if mail == 1 else "Senha Invalida"
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= erro,
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = criar_token(
        data={"sub": mail}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


