from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.user"
    label = "user_module"
    verbose_name = "User"
