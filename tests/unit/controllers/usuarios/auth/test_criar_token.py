from unittest.mock import patch, DEFAULT
from app.controllers.usuarios import auth
from datetime import timedelta
from jose import jwt

TOKEN_EXPIRATION_DELTA = timedelta(hours=1)
TOKEN_DATA = {"sub": "00000000000"}
MOCK_SECRET_KEY = "mock_secret"
MOCK_ALGORITHM = "HS256"
MOCK_JWT_ENCODE = "mock_token"


def test_creates_token_with_argument_expires_delta():
    with patch.multiple(
        auth, SECRET_KEY=DEFAULT, ALGORITHM=DEFAULT, autospec=True
    ) as mocks_auth, patch.object(jwt, "encode", autospec=True) as mock_encode:
        mocks_auth["SECRET_KEY"].return_value = MOCK_SECRET_KEY
        mocks_auth["ALGORITHM"].return_value = MOCK_ALGORITHM
        mock_encode.return_value = MOCK_JWT_ENCODE
        result = auth.criar_token(data=TOKEN_DATA, expires_delta=TOKEN_EXPIRATION_DELTA)
    assert result == MOCK_JWT_ENCODE


def test_creates_token_without_argument_expires_delta():
    with patch.multiple(
        auth, SECRET_KEY=DEFAULT, ALGORITHM=DEFAULT, autospec=True
    ) as mocks_auth, patch.object(jwt, "encode", autospec=True) as mock_encode:
        mocks_auth["SECRET_KEY"].return_value = MOCK_SECRET_KEY
        mocks_auth["ALGORITHM"].return_value = MOCK_ALGORITHM
        mock_encode.return_value = MOCK_JWT_ENCODE
        result = auth.criar_token(data=TOKEN_DATA)
    assert result == MOCK_JWT_ENCODE
