import json
from datetime import datetime

from app.models import db, forum_ip

session = db.session
Forum_ip = forum_ip.Forum_ip


def criar_topico(titulo, texto):
    try:
        topico = Forum_ip(
            titulo=titulo,
            texto=texto,
            data_criacao=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data_atualizacao=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        session.add(topico)
        session.commit()
        return {"mensagem": "Topico criado com sucesso"}
    except Exception as error:
        print({"error": error})
        session.rollback()
        return {"mensagem": "Solicitação não efetuada"}


def resposta_topico(resposta, topico_id, usuario):
    try:
        query = session.query(Forum_ip).filter_by(id=topico_id).all()
        if query == None:
            return {"mensagem": "Tópico ID não encontrado"}
        resposta_nova = {
            "texto": resposta,
            "usuario": usuario,
            "criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        if query[0].respostas == None:
            respostas = [resposta_nova]
        else:
            query[0].respostas.append(resposta_nova)
            respostas = query[0].respostas
        session.query(Forum_ip).filter_by(id=topico_id).update(
            {"respostas": respostas}
        )
        session.commit()
        return {"mensagem": "Resposta Registrada Com Sucesso"}
    except Exception as error:
        print({"error": error})
        session.rollback()
        return {"mensagem": "Solicitação não efetuada"}


def buscar_topico(topico_id=None, respostas=None):
    if topico_id == None and respostas == None:
        query = session.query(Forum_ip).all()
        return {"topicos": query}
    if topico_id != None and respostas == None:
        query = session.query(Forum_ip).filter_by(id=topico_id).all()
        return {"topicos": query}
    if topico_id != None and respostas != None:
        query = session.query(Forum_ip).filter_by(id=topico_id).all()
        return {"topicos": query[0].respostas[0:respostas]}


def excluir_topico(topico_id):
    try:
        session.query(Forum_ip).filter_by(id=topico_id).delete()
        return {"mensagem": "Tópico excluido com Sucesso"}
    except Exception as error:
        print({"erros": error})
        session.rollback()
        return {"mensagem": "Solicitação não efetuada"}
