"""Tests for the user API handlers."""

from src.api.users import create_user


def test_creates_user_with_default_role():
    status, body = create_user({"name": "Ada"})
    assert status == 201
    assert body["name"] == "Ada"
    assert body["role"] == "member"


def test_rejects_missing_name():
    status, body = create_user({})
    assert status == 400
    assert body["error"]["code"] == "bad_request"


def test_rejects_unknown_role():
    status, body = create_user({"name": "Ada", "role": "superuser"})
    assert status == 400
    assert body["error"]["code"] == "bad_request"
