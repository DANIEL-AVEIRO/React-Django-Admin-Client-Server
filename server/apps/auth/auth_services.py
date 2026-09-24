from django.contrib.auth import authenticate
from apps.user.models import UserModel


def register_user(email, password, first_name, last_name=""):
    if UserModel.objects.filter(email=email).exists():
        raise ValueError("Email is already registered.")

    user = UserModel.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    return user


def login_user(email, password):
    user = authenticate(email=email, password=password)

    if user is None:
        raise ValueError("Invalid email or password.")

    if not user.is_active:
        raise ValueError("This account is inactive.")

    return user
