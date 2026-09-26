from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel


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
def user_list(request):
    try:
        users = UserModel.objects.all().order_by("-created_at")
        return Response(
            {
                "success": True,
                "message": "Users retrieved successfully.",
                "data": [
                    {
                        "id": str(user.id),
                        "email": user.email,
                        "username": user.username,
                        "phone": user.phone,
                        "address": user.address,
                        "profile": (
                            user.profile.url if user.profile else None
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
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"User list failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def user_details(request, pk):
    try:
        user = UserModel.objects.get(id=pk)
        return Response(
            {
                "success": True,
                "message": "User retrieved successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                    "phone": user.phone,
                    "address": user.address,
                    "profile": (
                        user.profile.url if user.profile else None
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
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"User details failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def user_create(request):
    email = request.data.get("email")
    password = request.data.get("password")
    username = request.data.get("username")
    phone = request.data.get("phone")
    address = request.data.get("address")
    profile = request.data.get("profile")
    role = request.data.get("role")

    if not email or not password or not username or not role:
        return Response(
            {
                "success": False,
                "message": "Email, password, username and role are required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = UserModel.objects.create_user(
            email=email,
            password=password,
            username=username,
            phone=phone,
            address=address,
            profile=profile,
            role=role,
        )
        user.save()
        return Response(
            {
                "success": True,
                "message": "User created successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                    "phone": user.phone,
                    "address": user.address,
                    "profile": (
                        user.profile.url if user.profile else None
                    ),
                    "role": user.role.name,
                    "is_active": user.is_active,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
            },
            status=status.HTTP_201_CREATED,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"User creation failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def user_update(request, pk):
    email = request.data.get("email")
    password = request.data.get("password")
    username = request.data.get("username")
    phone = request.data.get("phone")
    address = request.data.get("address")
    profile = request.data.get("profile")
    role = request.data.get("role")

    if not email or not password or not username or not role:
        return Response(
            {
                "success": False,
                "message": "Email, password, username and role are required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = UserModel.objects.get(id=pk)
        if UserModel.objects.filter(email=email).exclude(id=pk).exists():
            return Response(
                {
                    "success": False,
                    "message": "Email already exists.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.email = email
        if password:
            user.set_password(password)
        user.username = username
        user.phone = phone
        user.address = address
        user.profile = profile
        user.role = role
        user.save()
        return Response(
            {
                "success": True,
                "message": "User updated successfully.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                    "phone": user.phone,
                    "address": user.address,
                    "profile": (
                        user.profile.url if user.profile else None
                    ),
                    "role": user.role.name,
                    "is_active": user.is_active,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
            },
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"User update failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["DELETE"])
def user_delete(request, pk):
    try:
        user = UserModel.objects.get(id=pk)
        if user.profile:
            user.profile.delete()
        user.delete()
        return Response(
            {
                "success": True,
                "message": "User deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"User deletion failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
