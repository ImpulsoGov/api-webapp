from models import db,usuarios
from passlib.context import CryptContext
from datetime import datetime
import uuid
def cadastrar(nome,mail,senha,cpf):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    criacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    atualizacao_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuario = usuarios.Usuario(
        id = str(uuid.uuid4()),
        nome_usuario=nome,
        mail=mail,
        hash_senha=pwd_context.hash(senha),
        perfil=None,
        cpf=cpf,
        criacao_data=criacao_data,
        atualizacao_data=atualizacao_data
        )
    session = db.session
    session.add(usuario)
    session.commit()
    return {"mensagem":"usuario cadastrado com sucesso"}
