import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

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



engine_1 = create_engine(
        "postgresql://postgres:UAnnT-80Gg-3m@34.68.133.244:5432/postgres?",
        connect_args={
            "options": "-c statement_timeout=100000000",
        },
        echo=True,
    )
Base_1 = declarative_base()
# import pdb; pdb.set_trace()
Base_1.metadata.drop_all(bind=engine_1)
Base_1.metadata.create_all(bind=engine_1)
Session = sessionmaker(twophase=True)
Session.configure(binds={Base_1: engine_1})

engine_2 = create_engine(
        "postgresql://api_user:EgQVEc-6201M@34.68.68.223:5432/api?",
        connect_args={
            "options": "-c statement_timeout=100000000",
        },
        echo=True,
    )
Base_2 = declarative_base()
Base_2.metadata.drop_all(bind=engine_2)

def conexao_banco(projeto):
    # credencial = credencial_[projeto]
    # engine = create_engine(
    #     "postgresql://{}:{}@{}:{}/{}?".format(
    #         credencial["USERNAME"].strip(),
    #         credencial["PASSWORD"].strip(),
    #         credencial["HOSTNAME"].strip(),
    #         credencial["PORT"].strip(),
    #         credencial["DATABASE"].strip(),
    #     ),
    #     connect_args={
    #         "options": "-c statement_timeout=100000000",
    #     },
    #     echo=True,
    # )

    # engine_1 = create_engine(
    #     "postgresql://postgres:UAnnT-80Gg-3m@34.68.133.244:5432/postgres?",
    #     connect_args={
    #         "options": "-c statement_timeout=100000000",
    #     },
    #     echo=True,
    # )
    # Base_1 = declarative_base()
    # Base_1.metadata.drop_all(bind=engine_1)

    # Session = sessionmaker(bind=engine)
    # Base = declarative_base()
    return Base_1
