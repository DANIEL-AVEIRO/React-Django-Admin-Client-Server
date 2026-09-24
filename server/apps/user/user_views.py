from .user_services import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.request import get_request_data


@api_view(["GET"])
def user_health_check(request):
    return Response(
        {
            "success": True,
            "message": "User module is working.",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def list(request):
    try:
        users = get_all_users()
        return Response(
            {
                "success": True,
                "message": "Users retrieved successfully.",
                "data": [
                    {
                        "id": str(user.id),
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "phone_number": user.phone_number,
                        "address": user.address,
                        "profile_photo": (
                            user.profile_photo.url if user.profile_photo else None
                        ),
                        "role": user.role.name,
                        "is_active": user.is_active,
                        "is_staff": user.is_staff,
                        "is_superuser": user.is_superuser,
                        "created_at": user.created_at,
                        "updated_at": user.updated_at,
                    }
                    for user in users
                ],
            },
            status=status.HTTP_200_OK,
        )
    except ValueError as error:
        return Response(
            {
                "success": False,
                "message": str(error),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def details(request, user_id):
    try:
        user = get_user_by_id(user_id)
        return Response(
            {
                "success": True,
                "message": "User retrieved successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                    "address": user.address,
                    "profile_photo": (
                        user.profile_photo.url if user.profile_photo else None
                    ),
                    "role": {
                        "id": str(user.role.id),
                        "name": user.role.name,
                        "description": user.role.description,
                        "is_active": user.role.is_active,
                        "created_at": user.role.created_at,
                        "updated_at": user.role.updated_at,
                    },
                    "is_active": user.is_active,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
            },
            status=status.HTTP_200_OK,
        )
    except ValueError as error:
        return Response(
            {
                "success": False,
                "message": str(error),
            },
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["POST"])
def create(request):
    data = get_request_data(request)
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    profile_photo = data.get("profile_photo")
    role = data.get("role")

    if not email:
        return Response(
            {
                "success": False,
                "message": "Email is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not password:
        return Response(
            {
                "success": False,
                "message": "Password is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not first_name:
        return Response(
            {
                "success": False,
                "message": "First name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not last_name:
        return Response(
            {
                "success": False,
                "message": "Role is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not role:
        return Response(
            {
                "success": False,
                "message": "Role is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            profile_photo=profile_photo,
            role=role,
        )
        return Response(
            {
                "success": True,
                "message": "User created successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                    "address": user.address,
                    "profile_photo": (
                        user.profile_photo.url if user.profile_photo else None
                    ),
                },
                "role": {
                    "id": str(user.role.id),
                    "name": user.role.name,
                    "description": user.role.description,
                    "is_active": user.role.is_active,
                    "created_at": user.role.created_at,
                    "updated_at": user.role.updated_at,
                },
                "is_active": user.is_active,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            },
            status=status.HTTP_201_CREATED,
        )
    except ValueError as error:
        return Response(
            {
                "success": False,
                "message": str(error),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
def update(request, user_id):
    data = get_request_data(request)
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    address = data.get("address")
    profile_photo = data.get("profile_photo")
    role = data.get("role")

    if not email:
        return Response(
            {
                "success": False,
                "message": "Email is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not password:
        return Response(
            {
                "success": False,
                "message": "Password is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not first_name:
        return Response(
            {
                "success": False,
                "message": "First name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not last_name:
        return Response(
            {
                "success": False,
                "message": "Last name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not role:
        return Response(
            {
                "success": False,
                "message": "Role is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = update_user(
            user_id=user_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            profile_photo=profile_photo,
            role=role,
        )
        return Response(
            {
                "success": True,
                "message": "User updated successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                    "address": user.address,
                    "profile_photo": (
                        user.profile_photo.url if user.profile_photo else None
                    ),
                },
                "role": {
                    "id": str(user.role.id),
                    "name": user.role.name,
                    "description": user.role.description,
                    "is_active": user.role.is_active,
                    "created_at": user.role.created_at,
                    "updated_at": user.role.updated_at,
                },
                "is_active": user.is_active,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            },
            status=status.HTTP_200_OK,
        )
    except ValueError as error:
        return Response(
            {
                "success": False,
                "message": str(error),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
def delete(request, user_id):
    try:
        delete_user(user_id)
        return Response(
            {
                "success": True,
                "message": "User deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )
    except ValueError as error:
        return Response(
            {
                "success": False,
                "message": str(error),
            },
            status=status.HTTP_404_NOT_FOUND,
        )
