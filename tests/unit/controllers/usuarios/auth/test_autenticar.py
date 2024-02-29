from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
from datetime import datetime
from dataclasses import dataclass
from typing import Union
import pytest

# from app.models.usuarios.usuarios import Usuario
# TODO: adicionar tratamento de erro na função autenticar


@dataclass
class User:
    id: str = "1"
    nome_usuario: str = "Usuário Teste 1"
    hash_senha: str = "testhash"
    mail: str = "teste1@email.com"
    cpf: str = "00000000000"
    perfil_ativo: Union[bool, None] = None
    criacao_data: datetime = datetime.now()
    atualizacao_data: datetime = datetime.now()

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(key)


MOCK_USER_WITH_ACTIVE_PROFILE = User(perfil_ativo=True)
MOCK_USER_WITH_INACTIVE_PROFILE = User(perfil_ativo=False)
MOCK_USER_WITH_PENDING_FIRST_ACCESS = User()
RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER = 1
RETURN_VALUE_FOR_INCORRECT_PASSWORD = 2
RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS = 3


def test_user_is_active_and_password_is_correct():
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks:
        mocks["get_user"].return_value = MOCK_USER_WITH_ACTIVE_PROFILE
        mocks["verificar_senha"].return_value = True
        result = auth.autenticar(cpf=MOCK_USER_WITH_ACTIVE_PROFILE["cpf"], senha="123456")
    assert result == MOCK_USER_WITH_ACTIVE_PROFILE.cpf


def test_user_is_active_and_password_is_incorrect():
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks:
        mocks["get_user"].return_value = MOCK_USER_WITH_ACTIVE_PROFILE
        mocks["verificar_senha"].return_value = False
        result = auth.autenticar(cpf=MOCK_USER_WITH_ACTIVE_PROFILE.cpf, senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_PASSWORD


def test_user_is_inactive():
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = MOCK_USER_WITH_INACTIVE_PROFILE
        result = auth.autenticar(cpf=MOCK_USER_WITH_INACTIVE_PROFILE.cpf, senha="123456")
    assert result == RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS


def test_user_has_pending_first_access():
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = MOCK_USER_WITH_PENDING_FIRST_ACCESS
        result = auth.autenticar(
            cpf=MOCK_USER_WITH_PENDING_FIRST_ACCESS.cpf, senha="123456"
        )
    assert result == RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS


def test_user_does_not_exist():
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = None
        result = auth.autenticar(cpf="00000000000", senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER


def test_cpf_is_incorrect():
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = MOCK_USER_WITH_ACTIVE_PROFILE
        result = auth.autenticar(cpf="11111111111", senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER


def test_exception_is_raised():
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks, pytest.raises(TypeError):
        mocks["get_user"].return_value = MOCK_USER_WITH_ACTIVE_PROFILE
        mocks["verificar_senha"].side_effect = TypeError("Type error")
        auth.autenticar(cpf=MOCK_USER_WITH_ACTIVE_PROFILE.cpf, senha="123456")
