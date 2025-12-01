from datetime import datetime, timedelta, timezone
from app.auth_service.core.settings import settings
import jwt

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
TOKEN_TTL = settings.token_ttl

def create_access_token(self, data) -> str:
    """Create an access token from user data."""
    try:
        payload = data.model_dump()
    except Exception:
        try:
            payload = data.dict()
        except Exception:
            payload = dict(data)

    payload.pop("password", None)
    payload["exp"] = (
        datetime.now(timezone.utc) + timedelta(minutes=TOKEN_TTL)
    )

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token