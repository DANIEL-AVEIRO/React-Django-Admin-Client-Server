from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.user.models import UserModel
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


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
    email = request.data.get("email")
    password = request.data.get("password")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name", "")

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

    try:
        user = UserModel.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        return Response(
            {
                "success": True,
                "message": "Registration successful.",
                "data": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
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
                "message": f"Registration failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response(
            {
                "success": False,
                "message": "Email and password are required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = authenticate(email=email, password=password)

        if user is None:
            return Response(
                {
                    "success": False,
                    "message": "Invalid email or password.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.is_active:
            return Response(
                {
                    "success": False,
                    "message": "This account is inactive.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "id": str(user.id),
                    "token": token.key,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
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
                "message": f"Login failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def profile(request):
    try:
        if request.user.is_authenticated:
            return Response(
                {
                    "success": True,
                    "message": "Profile retrieved successfully.",
                    "data": {
                        "id": str(request.user.id),
                        "email": request.user.email,
                        "first_name": request.user.first_name,
                        "last_name": request.user.last_name,
                        "created_at": request.user.created_at,
                        "updated_at": request.user.updated_at,
                    },
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "Unauthorized.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Profile retrieval failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def update_profile(request):
    try:
        if request.user.is_authenticated:
            email = request.data.get("email")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            password = request.data.get("password")
            profile_photo = request.data.get("profile_photo")
            address = request.data.get("address")
            phone_number = request.data.get("phone_number")
            if not email or not first_name:
                return Response(
                    {
                        "success": False,
                        "message": "Email and first name are required.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = UserModel.objects.get(id=request.user.id)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.profile_photo = profile_photo
            user.address = address
            user.phone_number = phone_number
            if password:
                user.set_password(password)
            user.save()
            return Response(
                {
                    "success": True,
                    "message": "Profile updated successfully.",
                    "data": {
                        "id": str(user.id),
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "profile_photo": user.profile_photo,
                        "address": user.address,
                        "phone_number": user.phone_number,
                        "created_at": user.created_at,
                        "updated_at": user.updated_at,
                    },
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "Unauthorized.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Profile update failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def change_password(request):
    try:
        if request.user.is_authenticated:
            current_password = request.data.get("current_password")
            new_password = request.data.get("new_password")
            if not current_password or not new_password:
                return Response(
                    {
                        "success": False,
                        "message": "Current password and new password are required.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = UserModel.objects.get(id=request.user.id)
            if not user.check_password(current_password):
                return Response(
                    {
                        "success": False,
                        "message": "Invalid current password.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if current_password == new_password:
                return Response(
                    {
                        "success": False,
                        "message": "New password cannot be the same as the current password.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(new_password)
            user.save()
            return Response(
                {
                    "success": True,
                    "message": "Password changed successfully.",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "Unauthorized.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Password change failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def logout(request):
    if request.user.is_authenticated:
        Token.objects.filter(user=request.user).delete()
    return Response(
        {"success": True, "message": "Logged out successfully."},
        status=status.HTTP_200_OK,
    )
