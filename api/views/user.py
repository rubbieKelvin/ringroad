from rest_framework.request import Request
from rest_framework.response import Response
from shared.view_tools.paths import Api
from shared.view_tools import body_tools
from api.models.user import User
from rest_framework import status
from django.contrib.auth import authenticate
from knox.models import AuthToken, AuthTokenManager
import pydantic
import typing


authentication_api = Api("auth/")

class UserInput(pydantic.BaseModel):
    first_name : str
    last_name : str
    email : pydantic.EmailStr
    password : str

class LoginUserInput(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str

@authentication_api.endpoint("signup", method="POST")
@body_tools.validate(UserInput)
def sign_up(request: Request) -> Response:
# def sign_up(request):
    data:UserInput = body_tools.get_validated_body(request)

    # check if the email already exists before creating the user

    User.objects.create_user(
        data.email,
        data.password,
        first_name=data.first_name, 
        last_name=data.last_name)

    return Response(status=status.HTTP_201_CREATED)

@authentication_api.endpoint("login", method="POST")
@body_tools.validate(LoginUserInput)
def login(request: Request) -> Response:

    #validate user credentials
    data: LoginUserInput = body_tools.get_validated_body(request)

    user = typing.cast(
        User,
        #verifies user
        authenticate(request=request, email=data.email, password=data.password)
    )
    #create tokens for user
    knox_token_manager: AuthTokenManager = typing.cast(
        AuthTokenManager, AuthToken.objects
    )
    _, token = knox_token_manager.create(user=user)

    #return user id
    return Response({"token": token}, status=status.HTTP_200_OK)






    



