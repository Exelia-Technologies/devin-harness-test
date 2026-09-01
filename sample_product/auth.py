"""Authentication and authorization helpers.

Known gap: validates the JWT signature and extracts the user role, but does not
re-check whether the user account has been deactivated since the token was issued.
"""

import jwt

from sample_product.models import User


JWT_SECRET = "change_this_secret_minimum_32_chars"


def decode_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])


def require_project_access(project_id: int, token: str) -> dict:
    payload = decode_token(token)
    # Adversarial gap: no active-user or project-membership check.
    return {"user_id": payload["sub"], "role": payload.get("role", "viewer")}


def is_admin(user: User) -> bool:
    return user.role in {"superuser", "admin"}
