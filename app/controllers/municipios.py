from models import db,municipios
session = db.session
Municipios = municipios.Municipios

def consulta_id(id):
    query = session.query(Municipios).filter_by(id_sus=id)
    res = query.all()
    return res

def consulta_slug(slug):
    query = session.query(Municipios).filter_by(slug=slug)
    res = query.all()
    return res