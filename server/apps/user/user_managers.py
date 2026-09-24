from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")

        if role is None:
            raise ValueError("Role is required.")

        email = self.normalize_email(email)

        user = self.model(email=email, role=role, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)

        extra_fields.setdefault("is_superuser", True)

        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email=email, password=password, role=role, **extra_fields
        )
