from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
import jose
import fastapi
import pytest

UNAUTHORIZED_RESPONSE_STATUS_CODE = 401
UNAUTHORIZED_RESPONSE_HEADER = {"WWW-Authenticate": "Bearer"}


@pytest.mark.asyncio
async def test_get_current_user_success(
    secret_key,
    algorithm,
    token_payload,
    token,
    user_1_with_active_profile,
    user_1_profile_1,
):
    with patch.multiple(
        auth,
        get_user=DEFAULT,
        get_perfil=DEFAULT,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends:
        get_perfil_return = {**user_1_profile_1.__dict__, "perfil": [1]}
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        mocks_auth["get_user"].return_value = user_1_with_active_profile
        mocks_auth["get_perfil"].return_value = get_perfil_return
        result = await auth.get_current_user()
    assert result == get_perfil_return


@pytest.mark.asyncio
async def test_invalid_token_payload(
    secret_key,
    algorithm,
    token,
):
    with patch.multiple(
        auth,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        invalid_token_payload = {}
        mock_decode.return_value = invalid_token_payload
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == UNAUTHORIZED_RESPONSE_STATUS_CODE
    assert exec_info.value.headers == UNAUTHORIZED_RESPONSE_HEADER


@pytest.mark.asyncio
async def test_invalid_token(
    secret_key,
    algorithm,
    token,
):
    with patch.multiple(
        auth,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.side_effect = jose.JWTError("Invalid token")
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == UNAUTHORIZED_RESPONSE_STATUS_CODE
    assert exec_info.value.headers == UNAUTHORIZED_RESPONSE_HEADER


@pytest.mark.asyncio
async def test_expired_token(
    secret_key,
    algorithm,
    token,
):
    with patch.multiple(
        auth,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.side_effect = jose.ExpiredSignatureError("Expired token")
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == UNAUTHORIZED_RESPONSE_STATUS_CODE
    assert exec_info.value.headers == UNAUTHORIZED_RESPONSE_HEADER


@pytest.mark.asyncio
async def test_user_does_not_exist(
    secret_key,
    algorithm,
    token_payload,
    token,
):
    with patch.multiple(
        auth,
        get_user=DEFAULT,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        mocks_auth["get_user"].return_value = None
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == UNAUTHORIZED_RESPONSE_STATUS_CODE
    assert exec_info.value.headers == UNAUTHORIZED_RESPONSE_HEADER


@pytest.mark.asyncio
async def test_user_is_inactive(
    secret_key,
    algorithm,
    token_payload,
    token,
    user_1_with_inactive_profile,
):
    with patch.multiple(
        auth,
        get_user=DEFAULT,
        SECRET_KEY=DEFAULT,
        ALGORITHM=DEFAULT,
        autospec=True,
    ) as mocks_auth, patch.object(
        jose.jwt, "decode", autospec=True
    ) as mock_decode, patch.object(
        fastapi, "Depends", autospec=True
    ) as mock_depends, pytest.raises(
        fastapi.HTTPException
    ) as exec_info:
        mock_decode.return_value = token_payload
        mock_depends.return_value = token
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        mocks_auth["get_user"].return_value = user_1_with_inactive_profile
        await auth.get_current_user()
    assert exec_info.type is fastapi.HTTPException
    assert exec_info.value.status_code == UNAUTHORIZED_RESPONSE_STATUS_CODE
    assert exec_info.value.headers == UNAUTHORIZED_RESPONSE_HEADER
