import pytest
from dataclasses import dataclass
from typing import Union
from datetime import datetime


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


@pytest.fixture
def user_1_with_active_profile():
    return User(perfil_ativo=True)


@pytest.fixture
def user_1_with_inactive_profile():
    return User(perfil_ativo=False)


@pytest.fixture
def user_1_with_pending_first_access():
    return User()


@pytest.fixture
def user_2_with_active_profile():
    return User(
        id="2",
        nome_usuario="Usuário Teste 2",
        hash_senha="",
        mail="teste2@email.com",
        cpf="11111111111",
        perfil_ativo=True,
    )


@pytest.fixture
def user_1_profile_1():
    return UserProfile(perfil=1)


@pytest.fixture
def user_1_profile_2():
    return UserProfile(perfil=2)


@pytest.fixture
def secret_key():
    return "mock_secret"


@pytest.fixture
def algorithm():
    return "HS256"


@pytest.fixture
def token_payload():
    return {"sub": "00000000000"}


@pytest.fixture
def token():
    return "mock_token"
