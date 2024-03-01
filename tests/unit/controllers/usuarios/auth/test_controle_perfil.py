from app.controllers.usuarios.auth import controle_perfil
import pytest

USER_PROFILES_WITH_PERMISSION = [1, 2]
USER_PROFILES_WITHOUT_PERMISSION = [3, 4]
PROFILE_WITH_PERMISSION = 2


def test_profile_has_permission():
    result = controle_perfil(
        perfil_usuario=USER_PROFILES_WITH_PERMISSION, perfil_rota=PROFILE_WITH_PERMISSION
    )
    assert result is True


def test_profile_has_no_permission():
    result = controle_perfil(
        perfil_usuario=USER_PROFILES_WITHOUT_PERMISSION,
        perfil_rota=PROFILE_WITH_PERMISSION,
    )
    expected = {
        "mensagem": "Perfil de usuário com Privilégio insuficiente para essa rota"
    }
    assert result == expected


def test_user_profile_is_not_iterable():
    with pytest.raises(TypeError):
        controle_perfil(perfil_usuario=1, perfil_rota=PROFILE_WITH_PERMISSION)
