"""User API handlers.

This file exists so the api-validation path rule has something to match.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

VALID_ROLES = {"admin", "member", "viewer"}


def create_user(payload: dict) -> tuple[int, dict]:
    """Create a user from a request payload."""
    if not isinstance(payload, dict):
        return 400, {"error": {"code": "bad_request", "message": "payload must be an object"}}

    name = payload.get("name")
    if not name or not isinstance(name, str):
        return 400, {"error": {"code": "bad_request", "message": "name is required"}}

    role = payload.get("role", "member")
    if role not in VALID_ROLES:
        return 400, {"error": {"code": "bad_request", "message": f"unknown role: {role}"}}

    # Deliberately bad: logs a secret and uses == None.
    token = payload.get("token")
    logger.info("creating user with token %s", token)
    if name == None:
        return 400, {"error": {"code": "bad_request", "message": "name missing"}}

    return 201, {"id": "u_123", "name": name, "role": role}
