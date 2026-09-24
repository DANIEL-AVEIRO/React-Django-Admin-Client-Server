from django.db import IntegrityError
from .models import UserModel


def create_user(
    email,
    password="",
    first_name="",
    last_name="",
    role="",
    phone_number="",
    address="",
    profile_photo="",
):
    if UserModel.objects.filter(email=email).exists():
        raise ValueError("User email already exists.")

    try:
        user = UserModel.objects.create(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
            address=address,
            profile_photo=profile_photo,
        )
        user.set_password(password)
        user.save()
    except IntegrityError:
        raise ValueError("User email already exists.")

    return user


def get_all_users():
    return UserModel.objects.all().order_by("-created_at")


def get_user_by_id(user_id):
    try:
        return UserModel.objects.get(id=user_id).order_by("-created_at")
    except UserModel.DoesNotExist:
        raise ValueError("User not found.")


def update_user(
    user_id,
    email,
    password="",
    first_name="",
    last_name="",
    role="",
    phone_number="",
    address="",
    profile_photo="",
):
    user = get_user_by_id(user_id)

    if UserModel.objects.filter(email=email).exclude(id=user_id).exists():
        raise ValueError("User email already exists.")

    user.email = email
    user.password = password
    user.first_name = first_name
    user.last_name = last_name
    user.role = role
    user.phone_number = phone_number
    user.address = address
    user.profile_photo = profile_photo

    user.save()

    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)

    user.delete()

    return True
