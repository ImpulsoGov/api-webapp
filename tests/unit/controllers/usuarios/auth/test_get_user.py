from unittest.mock import patch
from app.controllers.usuarios import auth
from app.models import db

# TODO: adicionar validação de existência do retorno do banco com respostas descritivas


def test_get_user_db_returns_list_of_users(
    user_1_with_active_profile, user_2_with_active_profile
):
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            "query.return_value.filter_by.return_value.all.return_value": (
                [user_1_with_active_profile, user_2_with_active_profile]
            )
        }
        mock_session.configure_mock(**config)
        result = auth.get_user(cpf=user_1_with_active_profile.cpf)
    assert result == user_1_with_active_profile


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
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {"query.return_value.filter_by.return_value.all.return_value": []}
        mock_session.configure_mock(**config)
        result = auth.get_user(cpf="00000000000")
    assert result is None
