from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
import jose
import fastapi
import pytest

RESPONSE_HEADER = {"WWW-Authenticate": "Bearer"}


@pytest.mark.asyncio
async def test_get_current_user_success(
    token_payload,
    token,
    user_1_with_active_profile,
    user_1_profile_1,
):
    with patch.multiple(
        auth,
        get_user=DEFAULT,
        get_perfil=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends:
        get_perfil_return = {**user_1_profile_1.__dict__, "perfil": [1]}
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_auth["get_user"].return_value = user_1_with_active_profile
        mocks_auth["get_perfil"].return_value = get_perfil_return
        result = await auth.get_current_user()
    assert result == get_perfil_return


@pytest.mark.asyncio
async def test_invalid_token_payload(
    token,
):
    with patch.object(jose.jwt, "decode", autospec=True) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(fastapi.HTTPException) as exec_info:
        invalid_token_payload = {}
        mock_decode.return_value = invalid_token_payload
        mock_depends.return_value = token
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Credencial Invalida"


@pytest.mark.asyncio
async def test_invalid_token(
    token,
):
    with patch.object(jose.jwt, "decode", autospec=True) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(fastapi.HTTPException) as exec_info:
        mock_decode.side_effect = jose.JWTError("Invalid token")
        mock_depends.return_value = token
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Credencial Invalida"


@pytest.mark.asyncio
async def test_expired_token(
    token,
):
    with patch.object(jose.jwt, "decode", autospec=True) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(fastapi.HTTPException) as exec_info:
        mock_decode.side_effect = jose.ExpiredSignatureError("Expired token")
        mock_depends.return_value = token
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Credencial Invalida"


@pytest.mark.asyncio
async def test_user_does_not_exist(
    token_payload,
    token,
):
    with patch.object(
        auth,
        "get_user",
        autospec=True,
    ) as mocks_get_user, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_get_user.return_value = None
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Credencial Invalida"


@pytest.mark.asyncio
async def test_user_is_inactive(
    token_payload,
    token,
    user_1_with_inactive_profile,
):
    with patch.object(
        auth,
        "get_user",
        autospec=True,
    ) as mocks_get_user, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_get_user.return_value = user_1_with_inactive_profile
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == fastapi.status.HTTP_401_UNAUTHORIZED
    assert exec_info.value.headers == RESPONSE_HEADER
    assert exec_info.value.detail == "Usuário Inativo"
