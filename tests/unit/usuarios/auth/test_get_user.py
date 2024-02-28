from unittest.mock import patch
from datetime import datetime
from app.controllers.usuarios.auth import get_user

MOCK_USER = {
    "id": "1",
    "nome_usuario": "Usuário Teste",
    "hash_senha": "",
    "mail": "teste@email.com",
    "cpf": "00000000000",
    "perfil_ativo": True,
    "criacao_data": datetime.now(),
    "atualizacao_data": datetime.now(),
}


# ref: https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls
def test_get_user_success():
    with patch("app.controllers.usuarios.auth.db") as mock_db:
        config = {
            "session.query.return_value.filter_by.return_value.all.return_value": (
                [MOCK_USER]
            )
        }
        mock_db.configure_mock(**config)
        result = get_user(cpf="00000000000")
    assert result == MOCK_USER


def test_get_user_db_raises_exception():
    with patch("app.controllers.usuarios.auth.db") as mock_db:
        config = {
            "session.query.return_value.filter_by.return_value.all.side_effect": (
                Exception("Error")
            )
        }
        mock_db.configure_mock(**config)
        result = get_user(cpf="00000000000")
    assert result is None


def test_get_user_db_returns_empty_list():
    with patch("app.controllers.usuarios.auth.db") as mock_db:
        config = {
            "session.query.return_value.filter_by.return_value.all.return_value": []
        }
        mock_db.configure_mock(**config)
        result = get_user(cpf="00000000000")
    assert result is None
