from unittest.mock import patch
from datetime import datetime
from app.controllers.usuarios import auth
from app.models import db

# TODO: padronizar uso do patch
# TODO: usar função util que encadeia métodos
# TODO: adicionar validação de existência do retorno do banco com respostas descritivas

MOCK_USER_1 = {
    "id": "1",
    "nome_usuario": "Usuário Teste 1",
    "hash_senha": "",
    "mail": "teste1@email.com",
    "cpf": "00000000000",
    "perfil_ativo": True,
    "criacao_data": datetime.now(),
    "atualizacao_data": datetime.now(),
}
MOCK_USER_2 = {
    "id": "2",
    "nome_usuario": "Usuário Teste 2",
    "hash_senha": "",
    "mail": "teste2@email.com",
    "cpf": "11111111111",
    "perfil_ativo": True,
    "criacao_data": datetime.now(),
    "atualizacao_data": datetime.now(),
}


def test_get_user_db_returns_list_of_users():
    with patch.object(auth, "db") as mock_db:
        config = {
            "session.query.return_value.filter_by.return_value.all.return_value": (
                [MOCK_USER_1, MOCK_USER_2]
            )
        }
        mock_db.configure_mock(**config)
        result = auth.get_user(cpf="00000000000")
    assert result == MOCK_USER_1


def test_get_user_db_raises_exception():
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            "query.return_value.filter_by.return_value.all.side_effect": (
                Exception("Error")
            )
        }
        mock_session.configure_mock(**config)
        result = auth.get_user(cpf="00000000000")
    assert result is None


def test_get_user_db_returns_empty_list():
    with patch("app.controllers.usuarios.auth.db") as mock_db:
        config = {
            "session.query.return_value.filter_by.return_value.all.return_value": []
        }
        mock_db.configure_mock(**config)
        result = auth.get_user(cpf="00000000000")
    assert result is None
