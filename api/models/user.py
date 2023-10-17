from django.db import models
from shared.abstractmodel import AbstractModel
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: str, **extra_fields: str | bool
    ) -> "User":
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(
            self, email: str, password: str, **extra_fields: str | bool
    ) -> "User":
         extra_fields["is_active"] = True
         extra_fields["is_staff"] = True
         extra_fields["is_superuser"] = True
         
         return self.create_user(email, password, **extra_fields)

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    

    objects: UserManager = UserManager()
