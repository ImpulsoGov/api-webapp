import re
import uuid
from datetime import datetime

from app.models import db
from app.models.impulso_previne_nominal import trilha_conteudo_avaliacao_conclusao, trilhas_acessos
from sqlalchemy import func
from fastapi import HTTPException, status

session = db.session


def consulta_avaliacao_conclusao(usuario_id, codigo_conteudo):
    try:
        query = db.session.query(
            trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo
        ).filter_by(usuario_id=usuario_id, codigo_conteudo=codigo_conteudo)
        res = query.all()
        return {"data": res, "error": None}
    except Exception as error:
        session.rollback()
        print(error)
        return {"mensagem": "Operação não efetuada", "error": error}


def consulta_avaliacao_conclusao_por_usuario(usuario_id):
    try:
        query = db.session.query(
            trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo
        ).filter_by(usuario_id=usuario_id)
        res = query.all()
        return {"data": res, "error": None}
    except Exception as error:
        session.rollback()
        print(error)
        return {"mensagem": "Operação não efetuada", "error": error}


def avaliacao_conteudo(usuario_id: str, codigo_conteudo: str, avaliacao: int):
    if len(re.findall("[A-Z][A-Z]-MOD[0-99]-C[0-99]", codigo_conteudo)) == 0:
        return {"msg": "Código de conteudo invalido", "error": True}
    res = consulta_avaliacao_conclusao(usuario_id, codigo_conteudo)
    if res["error"] != None:
        return {"msg": res["error"], "error": True}
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def avaliacao_check(avaliacao):
        if avaliacao in range(1,6) : return int(avaliacao)
        return False

    if avaliacao_check(avaliacao) == False:
        return {"error": "Avaliação invalida, informe um numero de 1 a 5"}
    if len(res["data"]) < 1:
        Avaliacao = trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo(
            id=str(uuid.uuid4()),
            usuario_id=usuario_id,
            codigo_conteudo=codigo_conteudo,
            avaliacao=avaliacao,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
        )

        try:
            session.add(Avaliacao)
            session.commit()
            return {"msg": "Avaliação cadastrada com sucesso", "error": None}
        except Exception as error:
            session.rollback()
            return {"error": error}
    if res["data"][0].__dict__["avaliacao"] == True:
        return {"msg": "Conteudo já avaliado", "concluido": True}
    if res["data"][0].__dict__["avaliacao"] == None:
        try:
            session.query(
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo
            ).filter(
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo.usuario_id
                == usuario_id,
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo.codigo_conteudo
                == codigo_conteudo,
            ).update(
                {"avaliacao": avaliacao}
            )
            session.commit()
            return {"msg": "Avaliação cadastrada com sucesso", "error": None}
        except Exception as error:
            session.rollback()
            return {"error": error}


def conclusao_conteudo(usuario_id: str, codigo_conteudo: str, concluido: bool):
    if len(re.findall("[A-Z][A-Z]-MOD[0-99]-C[0-99]", codigo_conteudo)) == 0:
        return {"msg": "Código de conteudo invalido", "error": True}
    res = consulta_avaliacao_conclusao(usuario_id, codigo_conteudo)
    if res["error"] != None:
        return {"msg": res["error"], "error": True}
    if len(res["data"]) < 1:
        criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Conclusao = trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo(
            id=str(uuid.uuid4()),
            usuario_id=usuario_id,
            codigo_conteudo=codigo_conteudo,
            concluido=concluido,
            criacao_data=criacao_data,
            atualizacao_data=atualizacao_data,
        )

        try:
            session.add(Conclusao)
            session.commit()
            return {"mensagem": "Conclusão de conteudo cadastrada com sucesso"}
        except Exception as error:
            session.rollback()
            return {"error": error}
    if res["data"][0].__dict__["concluido"] == True:
        return {"msg": "Conteudo já concluido", "concluido": True}
    if res["data"][0].__dict__["concluido"] == None:
        try:
            session.query(
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo
            ).filter(
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo.usuario_id
                == usuario_id,
                trilha_conteudo_avaliacao_conclusao.AvaliacaoConclusaoConteudo.codigo_conteudo
                == codigo_conteudo,
            ).update(
                {"concluido": concluido}
            )
            session.commit()
            return {
                "msg": "Conclusão de conteudo cadastrada com sucesso",
                "error": None,
            }
        except Exception as error:
            session.rollback()
            return {"error": error}

def trilha_acesso(usuario_id : str):
        try:
            res = session.query(trilhas_acessos.Trilhas_acesso).with_entities(
                trilhas_acessos.Trilhas_acesso.trilha_id
            ).filter_by(usuario_id=usuario_id).all()
            return res 
        except Exception as error:
            session.rollback()
            print({"erros" : [error]})
            return error

def trilha_modulos_acesso(usuario_id : str, trilha_id : str):
        try:
            res = session.query(trilhas_acessos.Trilhas_acesso).filter_by(
                usuario_id=usuario_id,trilha_id=trilha_id
            ).with_entities(
                trilhas_acessos.Trilhas_acesso.trilha_id,
                func.array_agg(trilhas_acessos.Trilhas_acesso.modulo).label("modulos"),
            ).group_by(
                trilhas_acessos.Trilhas_acesso.modulo,
                trilhas_acessos.Trilhas_acesso.trilha_id
            ).all()
            return res
        except Exception as error:
            session.rollback()
            print({"erros" : [error]})
            return error

def trilha_modulos_liberados(usuario_id : str, trilha_id : str, modulo : int):
        try:
            res = session.query(trilhas_acessos.Trilhas_acesso).filter_by(
                usuario_id=usuario_id,
                trilha_id=trilha_id,
                modulo = modulo
            ).with_entities(
                trilhas_acessos.Trilhas_acesso.trilha_id,
                func.array_agg(trilhas_acessos.Trilhas_acesso.modulo).label("modulos"),
            ).group_by(
                trilhas_acessos.Trilhas_acesso.modulo,
                trilhas_acessos.Trilhas_acesso.trilha_id
            ).all()
            return res
        except Exception as error:
            session.rollback()
            print({"erros" : [error]})
            return error


def trilha_modulos_acesso_add(usuario_id : str, trilha_id : str, modulo : int):
    modulo_existente = HTTPException(
        status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Modulo liberado anteriormente",
    )
    if len(trilha_modulos_liberados(usuario_id,trilha_id,modulo))!=0 : raise modulo_existente
    try:
        liberar_modulo = trilhas_acessos.Trilhas_acesso(
            id = str(uuid.uuid4()),
            usuario_id=usuario_id,
            trilha_id=trilha_id,
            modulo=modulo,
            criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        session.add(liberar_modulo)
        session.commit()
        return {"mensagem":"dados cadastrados com sucesso","error":None}

    except:
        session.rollback()
        return {"mensagem":"Inserção dos dados falhou","error":True}
