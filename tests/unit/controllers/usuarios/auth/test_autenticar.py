from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
import pytest

# TODO: adicionar tratamento de erro na função autenticar

RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER = 1
RETURN_VALUE_FOR_INCORRECT_PASSWORD = 2
RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS = 3


def test_user_is_active_and_password_is_correct(user_1_with_active_profile):
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks:
        mocks["get_user"].return_value = user_1_with_active_profile
        mocks["verificar_senha"].return_value = True
        result = auth.autenticar(cpf=user_1_with_active_profile["cpf"], senha="123456")
    assert result == user_1_with_active_profile.cpf


def test_user_is_active_and_password_is_incorrect(user_1_with_active_profile):
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks:
        mocks["get_user"].return_value = user_1_with_active_profile
        mocks["verificar_senha"].return_value = False
        result = auth.autenticar(cpf=user_1_with_active_profile.cpf, senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_PASSWORD


def test_user_is_inactive(user_1_with_inactive_profile):
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = user_1_with_inactive_profile
        result = auth.autenticar(cpf=user_1_with_inactive_profile.cpf, senha="123456")
    assert result == RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS


def test_user_has_pending_first_access(user_1_with_pending_first_access):
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = user_1_with_pending_first_access
        result = auth.autenticar(cpf=user_1_with_pending_first_access.cpf, senha="123456")
    assert result == RETURN_VALUE_FOR_INACTIVE_PROFILE_OR_PENDING_FIRST_ACCESS


def test_user_does_not_exist():
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = None
        result = auth.autenticar(cpf="00000000000", senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER


def test_cpf_is_incorrect(user_1_with_active_profile):
    with patch.object(auth, "get_user", autospec=True) as mock_get_user:
        mock_get_user.return_value = user_1_with_active_profile
        result = auth.autenticar(cpf="11111111111", senha="123456")
    assert result == RETURN_VALUE_FOR_INCORRECT_CPF_OR_UNEXISTING_USER


def test_exception_is_raised(user_1_with_active_profile):
    with patch.multiple(
        auth, get_user=DEFAULT, verificar_senha=DEFAULT, autospec=True
    ) as mocks, pytest.raises(TypeError):
        mocks["get_user"].return_value = user_1_with_active_profile
        mocks["verificar_senha"].side_effect = TypeError("Type error")
        auth.autenticar(cpf=user_1_with_active_profile.cpf, senha="123456")
