from unittest.mock import patch
from app.controllers.usuarios.auth import get_perfil
from app.models import db
from dataclasses import dataclass


@dataclass
class UserProfile:
    perfil: int
    id: str = "1"
    mail: str = "teste1@email.com"
    cpf: str = "00000000000"
    perfil_ativo: bool = True
    nome_usuario: str = "Usuário Teste 1"

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(key)


MOCK_USER_1_PROFILE_1 = UserProfile(perfil=1)
MOCK_USER_1_PROFILE_2 = UserProfile(perfil=2)


def test_db_returns_list_of_user_profile():
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            "query.return_value.join.return_value.join.return_value.with_entities.return_value.filter_by.return_value.all.return_value": (
                [MOCK_USER_1_PROFILE_1, MOCK_USER_1_PROFILE_2]
            )
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
        expected = {
            **MOCK_USER_1_PROFILE_1.__dict__,
            "perfil": [MOCK_USER_1_PROFILE_1.perfil, MOCK_USER_1_PROFILE_2.perfil],
        }
    assert result == expected


def test_db_returns_empty_list():
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            "query.return_value.join.return_value.join.return_value.with_entities.return_value.filter_by.return_value.all.return_value": (
                []
            )
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
    assert "erros" in result.keys()


def test_db_raises_exception():
    with patch.object(db, "session", autospec=True) as mock_session:
        config = {
            "query.return_value.join.return_value.join.return_value.with_entities.return_value.filter_by.return_value.all.side_effect": (
                Exception("Error")
            )
        }
        mock_session.configure_mock(**config)
        result = get_perfil(cpf="00000000000")
    assert "erros" in result.keys()
