from app.models import db,caracterizacao_municipal_resumo
session = db.session
CaracterizacaoMunicipal = caracterizacao_municipal_resumo.CaracterizacaoMunicipal

def consultar_caracterizacaoMunicipal( municipio_uf=None):
    try: 
        return session.query(CaracterizacaoMunicipal).filter_by(municipio_uf=municipio_uf).with_entities(
            CaracterizacaoMunicipal.periodo_codigo,
            CaracterizacaoMunicipal.municipio_id_sus,
            CaracterizacaoMunicipal.municipio_nome,
            CaracterizacaoMunicipal.municipio_uf,
            CaracterizacaoMunicipal.municipio_tipologia,
            CaracterizacaoMunicipal.municipio_populacao_2020,
            CaracterizacaoMunicipal.equipe_total,
            CaracterizacaoMunicipal.cadastro_parametro,
            CaracterizacaoMunicipal.cadastros_equipes_validas,
            CaracterizacaoMunicipal.cadastros_equipes_validas_com_ponderacao,
        ).all()   
    except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error