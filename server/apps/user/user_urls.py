from django.urls import path
from .user_views import (
    user_health_check,
    user_list,
    user_details,
    user_create,
    user_update,
    user_delete,
)

urlpatterns = [
    path("health/", user_health_check, name="user-health-check"),
    path("list/", user_list, name="user_list"),
    path("details/<uuid:pk>/", user_details, name="user_details"),
    path("create/", user_create, name="user_create"),
    path("update/<uuid:pk>/", user_update, name="user_update"),
    path("delete/<uuid:pk>/", user_delete, name="user_delete"),
]
