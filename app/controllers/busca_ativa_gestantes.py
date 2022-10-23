from app.models import DB_ANALITICO,busca_ativa
session = DB_ANALITICO.session
Gestantes = busca_ativa.Gestantes

def consulta_gestantes(municipio_uf):
    try:
        query = DB_ANALITICO.session.query(Gestantes).filter_by(municipio_uf=municipio_uf)
        res = query.all()
        return res
    except Exception as error:
        print({"erros" : [error]})
        return error
