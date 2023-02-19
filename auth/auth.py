from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend

cookie_transport = CookieTransport(cookie_max_age=14400, cookie_name='fastapiusersauth')

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=14400)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)