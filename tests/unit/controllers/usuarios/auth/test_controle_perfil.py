from app.controllers.usuarios.auth import controle_perfil
import pytest


@pytest.fixture
def user_profiles_with_permission():
    return [1, 2]


@pytest.fixture
def user_profiles_without_permission():
    return [3, 4]


@pytest.fixture
def profile_with_permission():
    return 2


def test_profile_has_permission(user_profiles_with_permission, profile_with_permission):
    result = controle_perfil(
        perfil_usuario=user_profiles_with_permission, perfil_rota=profile_with_permission
    )
    assert result is True


def test_profile_has_no_permission(
    user_profiles_without_permission, profile_with_permission
):
    result = controle_perfil(
        perfil_usuario=user_profiles_without_permission,
        perfil_rota=profile_with_permission,
    )
    expected = {
        "mensagem": "Perfil de usuário com Privilégio insuficiente para essa rota"
    }
    assert result == expected


def test_user_profile_is_not_iterable(profile_with_permission):
    with pytest.raises(TypeError):
        controle_perfil(perfil_usuario=1, perfil_rota=profile_with_permission)
