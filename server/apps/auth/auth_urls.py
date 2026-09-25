from django.urls import path
from .auth_views import (
    auth_health_check,
    login,
    register,
    profile,
    change_password,
    logout,
)

urlpatterns = [
    path("health/", auth_health_check, name="auth-health-check"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("change-password/", change_password, name="change-password"),
    path("logout/", logout, name="logout"),
]
