from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
from dataclasses import dataclass
import pytest
import fastapi

# TODO: retornar erro 400 quando usuário envia credenciais de login estiverem incorretas
RESPONSE_HEADER = {"WWW-Authenticate": "Bearer"}


@dataclass
class LoginCredentials:
    username: str = "12345678900"
    password: str = "123456"


@pytest.fixture
def login_credentials():
    return LoginCredentials()


def test_login_success(login_credentials, token):
    with patch.multiple(
        auth,
        autenticar=DEFAULT,
        criar_token=DEFAULT,
        autospec=True,
    ) as mocks_auth:
        mocks_auth["autenticar"].return_value = login_credentials.username
        mocks_auth["criar_token"].return_value = token
        result = auth.login(form_data=login_credentials)
    assert result == {"access_token": token, "token_type": "bearer"}


def test_incorrect_cpf(login_credentials):
    with patch.object(
        auth, "autenticar", autospec=True
    ) as mock_autenticar, pytest.raises(fastapi.HTTPException) as exec_info:
        incorrect_cpf_code = 1
        mock_autenticar.return_value = incorrect_cpf_code
        auth.login(form_data=login_credentials)
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "CPF Incorreto"


def test_incorrect_password(login_credentials):
    with patch.object(
        auth, "autenticar", autospec=True
    ) as mock_autenticar, pytest.raises(fastapi.HTTPException) as exec_info:
        incorrect_password_code = 2
        mock_autenticar.return_value = incorrect_password_code
        auth.login(form_data=login_credentials)
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Senha Inválida"


def test_user_is_inactive(login_credentials):
    with patch.object(
        auth, "autenticar", autospec=True
    ) as mock_autenticar, pytest.raises(fastapi.HTTPException) as exec_info:
        inactive_user_code = 3
        mock_autenticar.return_value = inactive_user_code
        auth.login(form_data=login_credentials)
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Usuário Inativo"
