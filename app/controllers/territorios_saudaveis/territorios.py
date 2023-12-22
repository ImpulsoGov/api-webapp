import json
from datetime import datetime

from app.models import (
    db
)
from app.models.territorios_saudaveis import (
    ts_domicilios,
    ts_estabelecimentos,
    ts_individuos,
    ts_profissionais,
)

session = db.session
Estabelecimentos = ts_estabelecimentos.Estabelecimentos
Profissionais = ts_profissionais.Profissionais
Domicilios = ts_domicilios.Domicilios
Individuos = ts_individuos.Individuos


def busca_estabelecimentos(ibge=None, cnes=None):
    if ibge and cnes:
        return session.query(Estabelecimentos).filter_by(ibge=ibge, cnes=cnes).all()
    elif ibge:
        return session.query(Estabelecimentos).filter_by(ibge=ibge).all()
    elif cnes:
        return session.query(Estabelecimentos).filter_by(cnes=cnes).all()
    else:
        return session.query(Estabelecimentos).all()


def busca_profissionais(ibge=None, cnes=None, cns=None):
    if ibge and cns:
        return session.query(Profissionais).filter_by(ibge=ibge, cns=cns).all()
    elif ibge:
        return session.query(Profissionais).filter_by(ibge=ibge).all()
    elif cns:
        return session.query(Profissionais).filter_by(cns=cns).all()
    else:
        return session.query(Profissionais).all()


def busca_domicilios(ibge=None, id=None):
    if ibge and id:
        return session.query(Domicilios).filter_by(ibge=ibge, id=id).all()
    elif ibge:
        return session.query(Domicilios).filter_by(ibge=ibge).all()
    elif id:
        return session.query(Domicilios).filter_by(id=id).all()
    else:
        return session.query(Domicilios).all()


def busca_individuos(ibge=None, domicilio_id=None):
    if ibge and domicilio_id:
        return (
            session.query(Individuos)
            .filter_by(ibge=ibge, domicilio_id=domicilio_id)
            .all()
        )
    elif ibge:
        return session.query(Individuos).filter_by(ibge=ibge).all()
    elif domicilio_id:
        return session.query(Individuos).filter_by(domicilio_id=domicilio_id).all()
    else:
        return session.query(Individuos).all()


def atualiza_estabelecimento(cnes, lat, long):
    try:
        session.query(Estabelecimentos).filter_by(cnes=cnes).update(
            {Estabelecimentos.latitude: lat, Estabelecimentos.longitude: long}
        )
        session.commit()
        return {"mensagem": "Estabelecimentos atualizado com Sucesso"}
    except Exception as error:
        print({"erros": error})
        session.rollback()
        return {"mensagem": "Solicitação não efetuada"}


def atualiza_domicilio(id, lat, long):
    try:
        session.query(Domicilios).filter_by(id=id).update(
            {Domicilios.latitude: lat, Estabelecimentos.longitude: long}
        )
        session.commit()
        return {"mensagem": "Domicilios atualizado com Sucesso"}
    except Exception as error:
        print({"erros": error})
        session.rollback()
        return {"mensagem": "Solicitação não efetuada"}
