from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
from datetime import timedelta
from jose import jwt
import pytest


@pytest.fixture
def token_expiration_delta():
    return timedelta(hours=1)


def test_creates_token_with_argument_expires_delta(
    secret_key, algorithm, token_payload, token_expiration_delta, token
):
    with patch.multiple(
        auth, SECRET_KEY=DEFAULT, ALGORITHM=DEFAULT, autospec=True
    ) as mocks_auth, patch.object(jwt, "encode", autospec=True) as mock_encode:
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        mock_encode.return_value = token
        result = auth.criar_token(
            data=token_payload, expires_delta=token_expiration_delta
        )
    assert result == token


def test_creates_token_without_argument_expires_delta(
    secret_key, algorithm, token_payload, token
):
    with patch.multiple(
        auth, SECRET_KEY=DEFAULT, ALGORITHM=DEFAULT, autospec=True
    ) as mocks_auth, patch.object(jwt, "encode", autospec=True) as mock_encode:
        mocks_auth["SECRET_KEY"].return_value = secret_key
        mocks_auth["ALGORITHM"].return_value = algorithm
        mock_encode.return_value = token
        result = auth.criar_token(data=token_payload)
    assert result == token
