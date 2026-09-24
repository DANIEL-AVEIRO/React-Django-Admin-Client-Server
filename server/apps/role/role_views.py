from rest_framework.decorators import api_view
from utils.request import get_request_data
from rest_framework.response import Response
from .role_services import (
    create_role,
    delete_role,
    get_all_roles,
    get_role_by_id,
    update_role,
)
from rest_framework import status


@api_view(["GET"])
def role_health_check(request):
    return Response(
        {
            "success": True,
            "message": "Role module is working.",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def list(request):
    try:
        roles = get_all_roles()
        return Response(
            {
                "success": True,
                "message": "Roles retrieved successfully.",
                "data": [
                    {
                        "id": str(role.id),
                        "name": role.name,
                        "description": role.description,
                        "is_active": role.is_active,
                        "created_at": role.created_at,
                        "updated_at": role.updated_at,
                    }
                    for role in roles
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
def details(request, role_id):
    try:
        role = get_role_by_id(role_id)
        return Response(
            {
                "success": True,
                "message": "Role retrieved successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
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
    name = data.get("name")
    description = data.get("description", "")
    is_active = data.get("is_active", True)

    if not name:
        return Response(
            {
                "success": False,
                "message": "Role name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        role = create_role(
            name=name,
            description=description,
            is_active=is_active,
        )
        return Response(
            {
                "success": True,
                "message": "Role created successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
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


@api_view(["PUT"])
def update(request, role_id):
    data = get_request_data(request)
    name = data.get("name")
    description = data.get("description", "")
    is_active = data.get("is_active", True)

    if not name:
        return Response(
            {
                "success": False,
                "message": "Role name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        role = update_role(
            role_id=role_id,
            name=name,
            description=description,
            is_active=is_active,
        )
        return Response(
            {
                "success": True,
                "message": "Role updated successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
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


@api_view(["DELETE"])
def delete(request, role_id):
    try:
        delete_role(role_id)
        return Response(
            {
                "success": True,
                "message": "Role deleted successfully.",
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
