from django.urls import path
from .role_views import (
    role_health_check,
    role_list,
    role_details,
    role_create,
    role_update,
    role_delete,
)

urlpatterns = [
    path("health/", role_health_check, name="role_health_check"),
    path("list/", role_list, name="role_list"),
    path("details/<uuid:pk>/", role_details, name="role_details"),
    path("create/", role_create, name="role_create"),
    path("update/<uuid:pk>/", role_update, name="role_update"),
    path("delete/<uuid:pk>/", role_delete, name="role_delete"),
]
