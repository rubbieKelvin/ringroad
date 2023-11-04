from django.db import models
from shared.apps.authentication.models import ExtensibleUser


class User(ExtensibleUser):
    """
    Custom User model with email authentication.

    This model represents a user with email-based authentication. It extends
    the AbstractBaseUser and PermissionsMixin classes and includes additional
    fields for user information.
    """
    
    first_name = models.CharField(max_length=30, null=True, default=None)
    last_name = models.CharField(max_length=30, null=True, default=None)

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
