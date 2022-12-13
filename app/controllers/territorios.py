from app.models import ts_estabelecimentos,db,ts_profissionais,ts_domicilios,ts_individuos
from datetime import datetime
import json
session = db.session
Estabelecimentos = ts_estabelecimentos.Estabelecimentos
Profissionais = ts_profissionais.Profissionais
Domicilios = ts_domicilios.Domicilios
Individuos = ts_individuos.Individuos

def busca_estabelecimento(cnes = None):
    if cnes:
        return session.query(Estabelecimentos).filter_by(cnes=cnes).all()
    else: 
        return session.query(Estabelecimentos).all()

def busca_profissionais(cns = None):
    if cns:
        return session.query(Profissionais).filter_by(cns=cns).all()
    else: 
        return session.query(Profissionais).all()

def busca_domicilios(id = None):
    if id:
        return session.query(Domicilios).filter_by(id=id).all()
    else: 
        return session.query(Domicilios).all()
        
def busca_individuos(domicilio_id = None):
    if domicilio_id:
        return session.query(Individuos).filter_by(domicilio_id=domicilio_id).all()
    else: 
        return session.query(Individuos).all()

def atualiza_estabelecimento(cnes, lat, long):
    try:
        session.query(Estabelecimentos).filter_by(cnes = cnes).update({Estabelecimentos.latitude: lat, Estabelecimentos.longitude: long})
        session.commit()
        return {"mensagem" : "Estabelecimentos atualizado com Sucesso"}
    except Exception as error:
        print({"erros" : error})
        session.rollback()
        return {"mensagem":"Solicitação não efetuada"}

def atualiza_domicilio(id, lat, long):
    try:
        session.query(Domicilios).filter_by(id = id).update({Domicilios.latitude: lat, Estabelecimentos.longitude: long})
        session.commit()
        return {"mensagem" : "Domicilios atualizado com Sucesso"}
    except Exception as error:
        print({"erros" : error})
        session.rollback()
        return {"mensagem":"Solicitação não efetuada"}
