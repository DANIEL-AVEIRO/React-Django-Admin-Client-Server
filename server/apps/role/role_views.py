from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RoleModel
from django.contrib.auth.models import Permission


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
def role_list(request):
    try:
        roles = RoleModel.objects.all().order_by("-created_at")
        return Response(
            {
                "success": True,
                "message": "Roles retrieved successfully.",
                "data": [
                    {
                        "id": str(role.id),
                        "name": role.name,
                        "permissions": [
                            {
                                "id": str(permission.id),
                                "name": permission.name,
                                "codename": permission.codename,
                            }
                            for permission in role.permissions.all()
                        ],
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
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Role list failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def role_details(request, pk):
    try:
        role = RoleModel.objects.get(id=pk).order_by("-created_at")
        if role is None:
            return Response(
                {
                    "success": False,
                    "message": "Role not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {
                "success": True,
                "message": "Role retrieved successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "permissions": [
                        {
                            "id": str(permission.id),
                            "name": permission.name,
                            "codename": permission.codename,
                        }
                        for permission in role.permissions.all()
                    ],
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
                },
            },
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Role details failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def role_create(request):
    name = request.data.get("name")
    permissions = request.data.get("permissions", [])
    if permissions:
        permissions = Permission.objects.filter(codename__in=permissions)
    description = request.data.get("description", "")
    is_active = request.data.get("is_active", True)

    if not name:
        return Response(
            {
                "success": False,
                "message": "Role name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        role = RoleModel.objects.create(
            name=name,
            permissions=permissions,
            description=description,
            is_active=is_active,
        )
        role.save()
        role.permissions.set(permissions)
        return Response(
            {
                "success": True,
                "message": "Role created successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "permissions": [
                        {
                            "id": str(permission.id),
                            "name": permission.name,
                            "codename": permission.codename,
                        }
                        for permission in role.permissions.all()
                    ],
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
                },
            },
            status=status.HTTP_201_CREATED,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Role creation failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PUT"])
def role_update(request, pk):
    name = request.data.get("name")
    permissions = request.data.get("permissions", [])
    if permissions:
        permissions = Permission.objects.filter(codename__in=permissions)
    description = request.data.get("description", "")
    is_active = request.data.get("is_active", True)

    if not name:
        return Response(
            {
                "success": False,
                "message": "Role name is required.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        role = RoleModel.objects.get(id=pk)
        role.name = name
        role.permissions = permissions
        role.description = description
        role.is_active = is_active
        role.save()
        role.permissions.set(permissions)
        return Response(
            {
                "success": True,
                "message": "Role updated successfully.",
                "data": {
                    "id": str(role.id),
                    "name": role.name,
                    "permissions": [
                        {
                            "id": str(permission.id),
                            "name": permission.name,
                            "codename": permission.codename,
                        }
                        for permission in role.permissions.all()
                    ],
                    "description": role.description,
                    "is_active": role.is_active,
                    "created_at": role.created_at,
                    "updated_at": role.updated_at,
                },
            },
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Role update failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["DELETE"])
def role_delete(request, pk):
    try:
        role = RoleModel.objects.get(id=pk)
        role.delete()
        return Response(
            {
                "success": True,
                "message": "Role deleted successfully.",
            },
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        return Response(
            {
                "success": False,
                "message": f"Role deletion failed: {str(error)}",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
