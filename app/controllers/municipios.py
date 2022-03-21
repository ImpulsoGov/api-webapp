from models import db,municipios
session = db.session
Municipios = municipios.Municipios

def consulta_municipio(id_sus,nome,estado_sigla,estado_nome):
    if estado_sigla != None or nome != None:
        if estado_sigla != None and nome != None:
            slug = estado_sigla+'-'+nome
            query = session.query(Municipios).filter_by(slug=slug)
            res = query.all()
            return res
        else:
            if estado_sigla != None and nome == None:
                query = session.query(Municipios).with_entities(
                    Municipios.id,
                    Municipios.estado_sigla,
                    Municipios.estado_nome,
                    Municipios.estado_id_ibge,
                    Municipios.municipio_eh_capital,
                    Municipios.municipio_id_sus,
                    Municipios.municipio_id_ibge,
                    Municipios.municipio_nome,
                    Municipios.municipio_nome_normalizado
                ).filter_by(estado_sigla=estado_sigla.upper())
                res = query.all()
                return res
            if estado_sigla == None and nome != None:
                query = session.query(Municipios).filter_by(municipio_nome_normalizado=nome)
                res = query.all()
                return res
    if id_sus != None:
        query = session.query(Municipios).filter_by(municipio_id_sus=id_sus)
        res = query.all()
        return res
    if estado_nome != None:
        query = session.query(Municipios).with_entities(
                    Municipios.id,
                    Municipios.estado_sigla,
                    Municipios.estado_nome,
                    Municipios.estado_id_ibge,
                    Municipios.municipio_eh_capital,
                    Municipios.municipio_id_sus,
                    Municipios.municipio_id_ibge,
                    Municipios.municipio_nome,
                    Municipios.municipio_nome_normalizado
        ).filter_by(estado_nome_normalizado=estado_nome)
        res = query.all()
        return res
