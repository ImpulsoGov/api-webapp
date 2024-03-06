from unittest.mock import patch
from app.controllers.usuarios import auth
from datetime import timedelta, datetime
from jose import jwt
import pytest


@pytest.fixture
def base_date():
    return datetime(year=2021, month=1, day=1, hour=1, minute=1, second=1)


def test_creates_token_with_value_passed_to_expires_delta(
    token_payload, token, base_date
):
    with patch.object(jwt, "encode", autospec=True) as mock_encode, patch(
        "app.controllers.usuarios.auth.datetime"
    ) as mock_datetime:
        token_expiration_delta = timedelta(minutes=30)
        token_with_expiration_time = f"{token}.{base_date + token_expiration_delta}"
        mock_datetime.utcnow.return_value = base_date
        mock_encode.return_value = token_with_expiration_time
        result = auth.criar_token(
            data=token_payload, expires_delta=token_expiration_delta
        )
    assert result == token_with_expiration_time


def test_creates_token_with_expires_delta_default_value(token_payload, token, base_date):
    with patch.object(jwt, "encode", autospec=True) as mock_encode, patch(
        "app.controllers.usuarios.auth.datetime"
    ) as mock_datetime:
        token_with_expiration_time = f"{token}.{base_date + timedelta(minutes=15)}"
        mock_datetime.utcnow.return_value = base_date
        mock_encode.return_value = token_with_expiration_time
        result = auth.criar_token(data=token_payload)
    assert result == token_with_expiration_time
