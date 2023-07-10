import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env_path = os.path.dirname(os.path.realpath(__file__)) + "/.env"
load_dotenv(dotenv_path=env_path)
credencial_ = {
    "HOMOLOGACAO": {
        "USERNAME": os.getenv("USERNAME_HOMOLOGACAO"),
        "PASSWORD": os.getenv("PASSWORD_HOMOLOGACAO"),
        "HOSTNAME": os.getenv("HOSTNAME_HOMOLOGACAO"),
        "PORT": os.getenv("PORT_HOMOLOGACAO"),
        "DATABASE": os.getenv("DATABASE_HOMOLOGACAO"),
    },
    "PRODUCAO": {
        "USERNAME": os.getenv("USERNAME_PROD"),
        "PASSWORD": os.getenv("PASSWORD_PROD"),
        "HOSTNAME": os.getenv("HOSTNAME_PROD"),
        "PORT": os.getenv("PORT_PROD"),
        "DATABASE": os.getenv("DATABASE_PROD"),
    },
}
credencial = credencial_[os.getenv("AMBIENTE").strip()]
engine = create_engine(
    "postgresql://{}:{}@{}:{}/{}?".format(
        credencial["USERNAME"].strip(),
        credencial["PASSWORD"].strip(),
        credencial["HOSTNAME"].strip(),
        int(credencial["PORT"].strip()),
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
