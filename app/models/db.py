from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

env_path = os.path.dirname(os.path.realpath(__file__))+'/.env'
load_dotenv(dotenv_path=env_path)
try:
   credencial_ = {
      "local":[
         {
            "USERNAME":os.getenv("USERNAME_LOCAL"),
            "PASSWORD":os.getenv("PASSWORD_LOCAL"),
            "HOSTNAME":os.getenv("HOSTNAME_LOCAL"),
            "PORT":os.getenv("PORT_LOCAL"),
            "DATABASE":os.getenv("DATABASE_LOCAL")
         }
      ],
      "homologacao":[
         {
         "USERNAME":os.environ("USERNAME_PROD"),
         "PASSWORD":os.environ("PASSWORD_PROD"),
         "HOSTNAME":os.environ("HOSTNAME_PROD"),
         "PORT":os.environ("PORT_PROD"),
         "DATABASE":os.environ("DATABASE_PROD")
      }],
      "prod":[
         {
         "USERNAME":os.environ("USERNAME_PROD"),
         "PASSWORD":os.environ("PASSWORD_PROD"),
         "HOSTNAME":os.environ("HOSTNAME_PROD"),
         "PORT":os.environ("PORT_PROD"),
         "DATABASE":os.environ("DATABASE_PROD")
      }
   ]
   }

   credencial = credencial_["homologacao"][0] if os.environ("HEROKU") == "TRUE" else credencial_["prod"][0]

except:
   credencial_ = {
      "local":[
         {
            "USERNAME":os.getenv("USERNAME_LOCAL"),
            "PASSWORD":os.getenv("PASSWORD_LOCAL"),
            "HOSTNAME":os.getenv("HOSTNAME_LOCAL"),
            "PORT":os.getenv("PORT_LOCAL"),
            "DATABASE":os.getenv("DATABASE_LOCAL")
         }
      ],
      "homologacao":[
         {
         "USERNAME":os.getenv("USERNAME_HOMOLOGACAO"),
         "PASSWORD":os.getenv("PASSWORD_HOMOLOGACAO"),
         "HOSTNAME":os.getenv("HOSTNAME_HOMOLOGACAO"),
         "PORT":os.getenv("PORT_HOMOLOGACAO"),
         "DATABASE":os.getenv("DATABASE_HOMOLOGACAO")
      }],
      "prod":[
         {
         "USERNAME":os.getenv("USERNAME_PROD"),
         "PASSWORD":os.getenv("PASSWORD_PROD"),
         "HOSTNAME":os.getenv("HOSTNAME_PROD"),
         "PORT":os.getenv("PORT_PROD"),
         "DATABASE":os.getenv("DATABASE_PROD")
      }
   ]
   }
   credencial = credencial_["prod"][0]

engine = create_engine(
   'postgresql://{}:{}@{}:{}/{}?'.format(credencial['USERNAME'],
                     credencial['PASSWORD'],
                     credencial['HOSTNAME'],
                     int(credencial['PORT']),
                     credencial['DATABASE']), connect_args={"options": "-c statement_timeout=100000000",
                                                            },
    echo=True
        
)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()