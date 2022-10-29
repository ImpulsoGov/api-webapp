from app.models import DB_ANALITICO,busca_ativa
session = DB_ANALITICO.session
Gestantes = busca_ativa.Gestantes

def consulta_gestantes_equipe(municipio_uf,equipe):
    try:
        #query = session.query(Gestantes).filter_by(municipio_uf=municipio_uf)
        #query = session.query(Gestantes)
        #res = query.all()
        res_tupla = session.execute("SELECT municipio_id_sus, municipio_uf, estabelecimento_cnes, estabelecimento_nome, equipe_ine, equipe_nome, acs_nome, acs_data_ultima_visita, gestante_documento_cpf, gestante_documento_cns, gestante_nome, gestante_data_de_nascimento, gestante_telefone, gestante_endereco, gestante_dum, gestante_idade_gestacional_atual, gestante_idade_gestacional_primeiro_atendimento, gestante_dpp, gestante_consulta_prenatal_data_limite, gestante_dpp_dias_para, gestante_consulta_prenatal_total, gestante_consulta_prenatal_ultima_data, gestante_consulta_prenatal_ultima_dias_desde, atendimento_odontologico_realizado, exame_hiv_realizado, exame_sifilis_realizado, exame_sifilis_hiv_realizado, possui_registro_aborto, possui_registro_parto, criacao_data, atualizacao_data FROM busca_ativa.painel_enfermeiras_lista_nominal_gestantes where municipio_uf='"+municipio_uf+"'"+" and equipe_ine ='"+equipe+"';").fetchall()
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
