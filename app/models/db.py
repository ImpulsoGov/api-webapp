import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
load_dotenv(dotenv_path=env_path)
credencial = {
    "PRODUCAO": {
        "USERNAME": os.getenv("USERNAME_PROD"),
        "PASSWORD": os.getenv("PASSWORD_PROD"),
        "HOSTNAME": os.getenv("HOSTNAME_PROD"),
        "PORT": os.getenv("PORT_PROD"),
        "DATABASE": os.getenv("DATABASE_PROD"),
    },
    "PRODUCAO_APLICACOES": {
        "USERNAME": os.getenv("USERNAME_PRODUCAO_APLICACOES"),
        "PASSWORD": os.getenv("PASSWORD_PRODUCAO_APLICACOES"),
        "HOSTNAME": os.getenv("HOSTNAME_PRODUCAO_APLICACOES"),
        "PORT": os.getenv("PORT_PRODUCAO_APLICACOES"),
        "DATABASE": os.getenv("DATABASE_PRODUCAO_APLICACOES"),
    },
    "usuarios": {
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


engine_usuarios = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["usuarios"]["USERNAME"].strip(),
        credencial["usuarios"]["PASSWORD"].strip(),
        credencial["usuarios"]["HOSTNAME"].strip(),
        int(credencial["usuarios"]["PORT"].strip()),
        credencial["usuarios"]["DATABASE"].strip(),
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)

engine_PRODUCAO = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["PRODUCAO"]["USERNAME"].strip(),
        credencial["PRODUCAO"]["PASSWORD"].strip(),
        credencial["PRODUCAO"]["HOSTNAME"].strip(),
        int(credencial["PRODUCAO"]["PORT"].strip()),
        credencial["PRODUCAO"]["DATABASE"].strip(),
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)
engine_PRODUCAO_APLICACOES = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["PRODUCAO_APLICACOES"]["USERNAME"].strip(),
        credencial["PRODUCAO_APLICACOES"]["PASSWORD"].strip(),
        credencial["PRODUCAO_APLICACOES"]["HOSTNAME"].strip(),
        int(credencial["PRODUCAO_APLICACOES"]["PORT"].strip()),
        credencial["PRODUCAO_APLICACOES"]["DATABASE"].strip(),
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)

engine_saude_mental = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["saude_mental"]["USERNAME"].strip(),
        credencial["saude_mental"]["PASSWORD"].strip(),
        credencial["saude_mental"]["HOSTNAME"].strip(),
        int(credencial["saude_mental"]["PORT"].strip()),
        credencial["saude_mental"]["DATABASE"].strip(),
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)

engine_impulso_previne_publico = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["impulso_previne_publico"]["USERNAME"].strip(),
        credencial["impulso_previne_publico"]["PASSWORD"].strip(),
        credencial["impulso_previne_publico"]["HOSTNAME"].strip(),
        int(credencial["impulso_previne_publico"]["PORT"].strip()),
        credencial["impulso_previne_publico"]["DATABASE"].strip(),
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)


### CRIA AS BASES DE CADA UM DOS MODELOS ###
Base_usuarios = declarative_base()
Base_usuarios.metadata.drop_all(bind=engine_usuarios)
Base_usuarios.metadata.create_all(bind=engine_usuarios)

Base_PRODUCAO = declarative_base()
Base_PRODUCAO.metadata.drop_all(bind=engine_PRODUCAO)
Base_PRODUCAO.metadata.create_all(bind=engine_PRODUCAO)

Base_PRODUCAO_APLICACOES = declarative_base()
Base_PRODUCAO_APLICACOES.metadata.drop_all(bind=engine_PRODUCAO_APLICACOES)
Base_PRODUCAO_APLICACOES.metadata.create_all(bind=engine_PRODUCAO_APLICACOES)

Base_saude_mental = declarative_base()
Base_saude_mental.metadata.drop_all(bind=engine_saude_mental)
Base_saude_mental.metadata.create_all(bind=engine_saude_mental)

Base_impulso_previne_publico = declarative_base()
Base_impulso_previne_publico.metadata.drop_all(bind=engine_impulso_previne_publico)
Base_impulso_previne_publico.metadata.create_all(bind=engine_impulso_previne_publico)

### CRIADOR DE SESSÃO ###
Session = sessionmaker(twophase=True)
Session.configure(
    binds={
        Base_usuarios: engine_usuarios,
        Base_PRODUCAO: engine_PRODUCAO,
        Base_PRODUCAO_APLICACOES: engine_PRODUCAO_APLICACOES,
        Base_saude_mental: engine_saude_mental,
        Base_impulso_previne_publico: engine_impulso_previne_publico,
    }
)
session = Session()
