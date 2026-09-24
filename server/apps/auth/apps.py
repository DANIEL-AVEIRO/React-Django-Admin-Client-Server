from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.auth"
    label = "auth_module"
    verbose_name = "Authentication"
