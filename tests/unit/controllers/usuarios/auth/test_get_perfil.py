from unittest.mock import patch
from app.controllers.usuarios.auth import get_perfil
from app.models import db

# TODO: adicionar validação de existência do retorno do banco com respostas descritivas


def test_db_returns_list_of_user_profile(
    user_1_profile_1,
    user_1_profile_2,
):
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            (
                "query.return_value"
                ".join.return_value"
                ".join.return_value"
                ".with_entities.return_value"
                ".filter_by.return_value"
                ".all.return_value"
            ): ([user_1_profile_1, user_1_profile_2])
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
        expected = {
            **user_1_profile_1.__dict__,
            "perfil": [user_1_profile_1.perfil, user_1_profile_2.perfil],
        }
    assert result == expected


def test_db_returns_empty_list():
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            (
                "query.return_value"
                ".join.return_value"
                ".join.return_value"
                ".with_entities.return_value"
                ".filter_by.return_value"
                ".all.return_value"
            ): ([])
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
    assert isinstance(result, dict)
    assert "erros" in result.keys()


def test_db_raises_exception():
    with patch.object(db, "session", autospec=True) as mock_session:
        error = Exception("An error happened")
        config = {
            (
                "query.return_value"
                ".join.return_value"
                ".join.return_value"
                ".with_entities.return_value"
                ".filter_by.return_value"
                ".all.side_effect"
            ): (error)
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
    assert isinstance(result, dict)
    assert "erros" in result.keys()
    assert error in result["erros"]
