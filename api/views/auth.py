import typing
import pydantic

from shared.view_tools.paths import Api
from shared.view_tools import exceptions
from shared.view_tools import body_tools

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from django.contrib.auth import authenticate
from api.models.user import User
from knox.models import AuthToken, AuthTokenManager

authentication_api = Api("auth/", name="Authentication")


class CreateUserInput(pydantic.BaseModel):
    """
    Input model for creating a user account.

    Attributes:
        - `first_name` (str): The first name of the user.
        - `last_name` (str): The last name of the user.
        - `email` (pydantic.EmailStr): The email address of the user.
        - `password` (str): The password for the user's account.
    """

    first_name: str
    last_name: str
    email: pydantic.EmailStr
    password: str


@authentication_api.endpoint("signup", method="POST", name="Create account")
@body_tools.validate(CreateUserInput)
def sign_up(request: Request) -> Response:
    """
    Endpoint for user registration.

    Args:
        - `request` (Request): The HTTP request object.

    Returns:
        Response: HTTP response indicating the success or failure of the registration process.
    """

    data: CreateUserInput = body_tools.get_validated_body(request)

    # check if the email already exists before creating the user
    if User.objects.filter(email=data.email).exists():
        raise exceptions.ApiException("A user with this email already exists")

    User.create(
        email=data.email,
        password=data.password,
        first_name=data.first_name,
        last_name=data.last_name,
    )

    return Response(status=status.HTTP_201_CREATED)


class LoginUserInput(pydantic.BaseModel):
    """
    Input model for user login.

    Attributes:
        - `email` (pydantic.EmailStr): The email address of the user.
        - `password` (str): The password for the user's account.
    """

    email: pydantic.EmailStr
    password: str


@authentication_api.endpoint("login", method="POST", name="Create token")
@body_tools.validate(LoginUserInput)
def login(request: Request) -> Response:
    """
    Endpoint for user login and token creation.

    Args:
        - `request` (Request): The HTTP request object.

    Returns:
        Response: HTTP response containing the authentication token upon successful login.
    """

    data: LoginUserInput = body_tools.get_validated_body(request)

    user = authenticate(request=request, email=data.email, password=data.password)

    knox_token_manager: AuthTokenManager = typing.cast(
        AuthTokenManager, AuthToken.objects
    )
    _, token = knox_token_manager.create(user=user)

    # return user id
    return Response({"token": token}, status=status.HTTP_200_OK)
