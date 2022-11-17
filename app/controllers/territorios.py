from app.models import ts_estabelecimentos,db
from datetime import datetime
import json
session = db.session
Estabelecimentos = ts_estabelecimentos.Estabelecimentos

def busca_estabelecimento(cnes = None):
    if cnes:
        return session.query(Estabelecimentos).filter_by(cnes=cnes).all()
    else: 
        return session.query(Estabelecimentos).all()

def atualiza_estabelecimento(cnes, lat, long):
    try:
        session.query(Estabelecimentos).filter_by(cnes = cnes).update({Estabelecimentos.latitude: lat, Estabelecimentos.longitude: long})
        session.commit()
        return {"mensagem" : "Estabelecimentos atualizado com Sucesso"}
    except Exception as error:
        print({"erros" : error})
        session.rollback()
        return {"mensagem":"Solicitação não efetuada"}

