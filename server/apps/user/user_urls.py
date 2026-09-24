from django.urls import path
from .user_views import user_health_check, list, details, create, update, delete

urlpatterns = [
    path("health/", user_health_check, name="user-health-check"),
    path("list/", list, name="list"),
    path("details/<str:user_id>/", details, name="details"),
    path("create/", create, name="create"),
    path("update/<str:user_id>/", update, name="update"),
    path("delete/<str:user_id>/", delete, name="delete"),
]
