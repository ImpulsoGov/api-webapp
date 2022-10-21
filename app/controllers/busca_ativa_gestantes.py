from app.models import DB_ANALITICO,busca_ativa
session = DB_ANALITICO.session
Gestantes = busca_ativa.Gestantes

def consulta_gestantes():
    query = session.query(Gestantes)
    res = query.all()
    return res
