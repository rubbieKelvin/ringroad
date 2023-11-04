import typing

from shared.abstractmodel import AbstractModel
from shared.view_tools.paths import Api
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

user_api = Api("user/")


@user_api.endpoint("me", method="GET", permission=IsAuthenticated)
def getCurrentUser(request: Request) -> Response:
    user = request.user
    user = typing.cast(AbstractModel, user)
    return Response(user.serialize())
