from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.auth.auth_services import register_user, login_user
from rest_framework import status
from utils.request import get_request_data


@api_view(["GET"])
def auth_health_check(request):
    return Response(
        {
            "success": True,
            "message": "Auth module is working.",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def register(request):
    data = get_request_data(request)

    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name", "")

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

    if len(password) < 8:
        return Response(
            {
                "success": False,
                "message": "Password must be at least 8 characters.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = register_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        return Response(
            {
                "success": True,
                "message": "Registration successful.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role.name,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
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


def login(request):
    data = get_request_data(request)

    email = data.get("email")
    password = data.get("password")

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

    try:

        user = login_user(
            email=email,
            password=password,
        )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role.name,
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
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def profile(request):
    return Response(
        {
            "success": True,
            "message": "Profile retrieved successfully.",
            "data": {
                "id": str(request.user.id),
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "role": request.user.role.name,
                "created_at": request.user.created_at,
                "updated_at": request.user.updated_at,
            },
        },
        status=status.HTTP_200_OK,
    )
