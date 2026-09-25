from common.base_models import BaseModel
from django.db import models
from django.contrib.auth.models import Permission


class RoleModel(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True, related_name="roles")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["-created_at"]
