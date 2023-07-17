import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


env_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
load_dotenv(dotenv_path=env_path)

credencial_ = {
    "PRODUCAO": {
        "USERNAME": os.getenv("USERNAME_PROD"),
        "PASSWORD": os.getenv("PASSWORD_PROD"),
        "HOSTNAME": os.getenv("HOSTNAME_PROD"),
        "PORT": os.getenv("PORT_PROD"),
        "DATABASE": os.getenv("DATABASE_PROD"),
    },
    "suporte": {
        "USERNAME": os.getenv("USERNAME_USUARIOS"),
        "PASSWORD": os.getenv("PASSWORD_USUARIOS"),
        "HOSTNAME": os.getenv("HOSTNAME_USUARIOS"),
        "PORT": os.getenv("PORT_USUARIOS"),
        "DATABASE": os.getenv("DATABASE_USUARIOS"),
    },
    "saude_mental": {
        "USERNAME": os.getenv("USERNAME_SM"),
        "PASSWORD": os.getenv("PASSWORD_SM"),
        "HOSTNAME": os.getenv("HOSTNAME_SM"),
        "PORT": os.getenv("PORT_SM"),
        "DATABASE": os.getenv("DATABASE_SM"),
    },
    "impulso_previne_publico": {
        "USERNAME": os.getenv("USERNAME_IP_PUB"),
        "PASSWORD": os.getenv("PASSWORD_IP_PUB"),
        "HOSTNAME": os.getenv("HOSTNAME_IP_PUB"),
        "PORT": os.getenv("PORT_IP_PUB"),
        "DATABASE": os.getenv("DATABASE_IP_PUB"),
    },
    "impulso_previne_nominal": {
        "USERNAME": os.getenv("USERNAME_IP_NOMINAL"),
        "PASSWORD": os.getenv("PASSWORD_IP_NOMINAL"),
        "HOSTNAME": os.getenv("HOSTNAME_IP_NOMINAL"),
        "PORT": os.getenv("PORT_IP_NOMINAL"),
        "DATABASE": os.getenv("DATABASE_IP_NOMINAL"),
    },
}

def conexao_banco(projeto):
    credencial = credencial_[projeto]
    engine = create_engine(
        "postgresql://{}:{}@{}:{}/{}?".format(
            credencial["USERNAME"].strip(),
            credencial["PASSWORD"].strip(),
            credencial["HOSTNAME"].strip(),
            credencial["PORT"].strip(),
            credencial["DATABASE"].strip(),
        ),
        connect_args={
            "options": "-c statement_timeout=100000000",
        },
        echo=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    return Base
