from datetime import datetime, timedelta, timezone
import jwt
from django.conf import settings


def generate_access_token(user):
    payload = {
        "user_id": str(user.id),
        "email": user.email,
        "role": user.role.name,
        "type": "access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=60),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_access_token(token):

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None
