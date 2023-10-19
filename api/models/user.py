from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from shared.abstractmodel import AbstractModel


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    This manager provides methods for creating both regular users and superusers.
    """

    def create_user(
        self, email: str, password: str, **extra_fields: str | bool | None
    ) -> "User":
        """
        Create and save a regular user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The created user instance.

        Raises:
            ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(
        self, email: str, password: str, **extra_fields: str | bool | None
    ) -> "User":
        """
        Create and save a superuser with the given email and password.

        Args:
            email (str): The superuser's email address.
            password (str): The superuser's password.
            **extra_fields: Additional fields for the superuser model.

        Returns:
            User: The created superuser instance.
        """
        extra_fields["is_active"] = True
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True

        return self.create_user(email, password, **extra_fields)


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with email authentication.

    This model represents a user with email-based authentication. It extends
    the AbstractBaseUser and PermissionsMixin classes and includes additional
    fields for user information.
    """

    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: UserManager = UserManager()

    @staticmethod
    def create(
        email: str,
        password: str,
        first_name: str | None = None,
        last_name: str | None = None,
    ):
        """
        Create and save a user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str, optional): The user's first name.
            last_name (str, optional): The user's last name.

        Returns:
            User: The created user instance.
        """

        return User.objects.create_user(
            email, password, first_name=first_name, last_name=last_name
        )
