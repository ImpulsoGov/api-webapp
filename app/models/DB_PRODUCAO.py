import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
load_dotenv(dotenv_path=env_path)
credencial = {
    "USERNAME": os.getenv("USERNAME_PRODUCAO_APLICACOES"),
    "PASSWORD": os.getenv("PASSWORD_PRODUCAO_APLICACOES"),
    "HOSTNAME": os.getenv("HOSTNAME_PRODUCAO_APLICACOES"),
    "PORT": os.getenv("PORT_PRODUCAO_APLICACOES"),
    "DATABASE": os.getenv("DATABASE_PRODUCAO_APLICACOES"),
}
engine = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["USERNAME"],
        credencial["PASSWORD"],
        credencial["HOSTNAME"],
        int(credencial["PORT"]),
        credencial["DATABASE"],
    ),
    connect_args={
        "options": "-c statement_timeout=100000000",
    },
    echo=True,
)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
