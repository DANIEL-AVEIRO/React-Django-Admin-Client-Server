from django.urls import path
from .role_views import role_health_check, list, details, create, update, delete

urlpatterns = [
    path("health/", role_health_check, name="role-health-check"),
    path("list/", list, name="list"),
    path("details/<str:role_id>/", details, name="details"),
    path("create/", create, name="create"),
    path("update/<str:role_id>/", update, name="update"),
    path("delete/<str:role_id>/", delete, name="delete"),
]
