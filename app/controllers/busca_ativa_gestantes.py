from app.models import DB_PRODUCAO  
from app.models.busca_ativa_aps import GestantesCoordenacao
from app.models.busca_ativa_equipe import Gestantes

session = DB_PRODUCAO.session

def consulta_gestantes_equipe(municipio_uf,equipe):
    try:
        #query = session.query(Gestantes).filter_by(municipio_uf=municipio_uf,equipe_ine=equipe)
        #query = session.query(Gestantes)
        #res = query.all()
        #for item in res[0:3]:
            #for key in item.__dict__:
                #if type(item.__dict__[key]) == bool: item.__dict__[key]=int(item.__dict__[key])
        res_tupla = session.execute("SELECT * FROM impulso_previne_dados_nominais.painel_enfermeiras_lista_nominal_gestantes where municipio_uf='"+municipio_uf+"'"+" and equipe_ine ='"+equipe+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error


def consulta_gestantes_coordenacao(municipio_uf):
    try:
        #query = session.query(GestantesCoordenacao).filter_by(municipio_uf=municipio_uf)
        #query = session.query(GestantesCoordenacao)
        #res = query.all()
        
        #for item in res[0:3]:
            #for key in item.__dict__:
                #if type(item.__dict__[key]) == bool: item.__dict__[key]=int(item.__dict__[key])
        res_tupla = session.execute("SELECT * FROM impulso_previne_dados_nominais.painel_coordenadores_lista_nominal_gestantes where municipio_uf='"+municipio_uf+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def cadastros_duplicados_gestantes_por_equipe(municipio_uf,equipe):
    try:
        res_tupla = session.execute("SELECT * FROM impulso_previne_dados_nominais.painel_cadastros_gestantes_duplicadas where municipio_uf='"+municipio_uf+"'"+" and equipe_ine ='"+equipe+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

def cadastros_duplicados_gestantes_por_municipio(municipio_uf):
    try:
        res_tupla = session.execute("SELECT * FROM impulso_previne_dados_nominais.painel_cadastros_gestantes_duplicadas where municipio_uf='"+municipio_uf+"';").fetchall()
        res = []
        for item in res_tupla:
            res.append(dict(item))
        for item in res:
            for key, value in item.items(): 
                if type(value) == bool: item[key]=int(value)
        return res
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error

