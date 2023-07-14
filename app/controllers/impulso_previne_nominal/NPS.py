from datetime import datetime
from app.models import db
from app.models.impulso_previne_nominal import NPS
session = db.session
from fastapi import HTTPException,status

def consulta_avaliacao(usuario_id):
    res = session.query(NPS.NPS).filter_by(usuario_id=usuario_id).all()
    if len(res) == 0 : raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario não encontrado")
    return res

def consulta_avaliacao_apoio(usuario_id):
    res = session.query(NPS.NPS).filter_by(usuario_id=usuario_id).all()
    if len(res) > 0 : raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario já realizou avaliação")
    return res


def NPS_UMANE(usuario_id,avaliacao):
    consulta_avaliacao_apoio(usuario_id)
    if avaliacao <1 or avaliacao >5 : 
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Avaliação fora do intervalo de 1 a 5"
        )
    try:
        nps_avaliacao = NPS.NPS(
            usuario_id=usuario_id,
            avaliacao=avaliacao,
            criacao_data=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        session.add(nps_avaliacao)
        session.commit()
        return {"mensagem":"dados cadastrados com sucesso","error":None}
    except Exception as error:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Avaliação não registrada : "+ str(error)
        )
