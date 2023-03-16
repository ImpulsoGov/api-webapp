from app.models import DB_PRODUCAO  
from app.models.hipertensos import Hipertensos

session = DB_PRODUCAO.session

def hipertensos_equipe(municipio_uf,equipe):
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(equipe_ine_cadastro=equipe,municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def hipertensos_coordenacao(municipio_uf):
    try:
        return DB_PRODUCAO.session.query(Hipertensos).filter_by(municipio_uf=municipio_uf).all()
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


