from django.db import IntegrityError
from .models import RoleModel


def create_role(name, description="", is_active=True):
    if RoleModel.objects.filter(name=name).exists():
        raise ValueError("Role name already exists.")

    try:
        role = RoleModel.objects.create(
            name=name,
            description=description,
            is_active=is_active,
        )
    except IntegrityError:
        raise ValueError("Role name already exists.")

    return role


def get_all_roles():
    return RoleModel.objects.all().order_by("-created_at")


def get_role_by_id(role_id):
    try:
        return RoleModel.objects.get(id=role_id).order_by("-created_at")
    except RoleModel.DoesNotExist:
        raise ValueError("Role not found.")


def update_role(role_id, name, description, is_active):
    role = get_role_by_id(role_id)

    if RoleModel.objects.filter(name=name).exclude(id=role_id).exists():
        raise ValueError("Role name already exists.")

    role.name = name
    role.description = description
    role.is_active = is_active

    role.save()

    return role


def delete_role(role_id):
    role = get_role_by_id(role_id)

    if role.users.exists():
        raise ValueError("Cannot delete role because users are assigned to this role.")

    role.delete()

    return True
