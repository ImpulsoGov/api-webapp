from unittest.mock import patch
from app.controllers.usuarios import auth
from datetime import timedelta
from jose import jwt
import pytest


@pytest.fixture
def token_expiration_delta():
    return timedelta(minutes=30)


def test_creates_token_with_argument_expires_delta(
    token_payload, token_expiration_delta, token
):
    with patch.object(jwt, "encode", autospec=True) as mock_encode:
        mock_encode.return_value = token
        result = auth.criar_token(
            data=token_payload, expires_delta=token_expiration_delta
        )
    assert result == token


def test_creates_token_without_argument_expires_delta(token_payload, token):
    with patch.object(jwt, "encode", autospec=True) as mock_encode:
        mock_encode.return_value = token
        result = auth.criar_token(data=token_payload)
    assert result == token
