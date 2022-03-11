from models import db,teste_orm
session = db.session
User = teste_orm.User

def consulta(nome,sobrenome):
    query = session.query(User).filter_by(nome=nome,sobrenome=sobrenome)
    res = query.all()
    return res[0]