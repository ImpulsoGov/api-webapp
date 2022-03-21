from models import db,indicadores
session = db.session
Indicadores = indicadores.Indicadores

def consulta_indicadores(id_sus,municipio_nome,estado_sigla,estado_nome,indicadores_nome,indicadores_parametros_id):
    if estado_sigla != None and municipio_nome != None:
        query = session.query(Indicadores).filter_by(municipio_nome_normalizado=municipio_nome,estado_sigla=estado_sigla.upper())
        res = query.all()
        return res
    else:
        if estado_sigla != None and municipio_nome == None:
            query = session.query(Indicadores).filter_by(estado_sigla=estado_sigla.upper())
            res = query.all()
            return res
        if estado_sigla == None and municipio_nome != None:
            query = session.query(Indicadores).filter_by(municipio_nome_normalizado=municipio_nome)
            res = query.all()
            return res

    if  indicadores_parametros_id != None :
        query = session.query(Indicadores).filter_by(indicadores_parametros_id=indicadores_parametros_id)
        res = query.all()
        return res

    if  indicadores_nome != None :
        query = session.query(Indicadores).filter_by(indicadores_parametros_nome_normalizado=indicadores_nome)
        res = query.all()
        return res

    if  estado_nome != None :
        query = session.query(Indicadores).filter_by(estado_nome_normalizado=estado_nome)
        res = query.all()
        return res

    if  id_sus != None :
        query = session.query(Indicadores).filter_by(municipio_id_sus=id_sus)
        res = query.all()
        return res
