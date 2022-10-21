import os
from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
from app.models import db,chave_data_studio

# openssl rand -base64 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def gen_chave_temp(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.__dict__.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    try:
        store_chave_temp(encoded_jwt)
    except Exception as error:
        print(error)
        return {
                "access_token":"",
                "mensagem":"chave não armazenada"
               }
    return {"access_token":encoded_jwt}

def store_chave_temp(chave: str):
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    chave_db = chave_data_studio.ChaveDS(
        chave=chave,
        criacao_data=criacao_data,
    )    
    try:
        session = db.session
        db.session.add(chave_db)
        session.commit()
        return {"mensagem":"Chave emitida e registrada com sucesso"}
    except Exception as error:
        print(error)
        session.rollback()
        return {"mensagem":"Registro não efetuado"}

def val_chave_temp(chave: str):
    try:
        expire = jwt.decode(chave, SECRET_KEY, algorithms=[ALGORITHM]).get("exp")
    except Exception as error:
        return {"access_token":False,"mensagem": str(error)}
    try:
        res = db.session.query(chave_data_studio.ChaveDS).filter_by(chave=chave).all()
        if len(res)== 0 : return {"access_token":False,"mensagem": "Chave Invalida"}
        return {"access_token":True,"mensagem": "Chave Valida"}
    except Exception as error:
        db.session.rollback()
        print(error)
        return {"mensagem": "Validação não efetuada"}
    
