import typing

from api.models.user import User
from api.models.store import Store

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


@user_api.endpoint("last-viewed-store", method="GET", permission=IsAuthenticated)
def getLastViewdStore(request: Request) -> Response:
    """Returns the last store (belonging to the user) opened by this user."""
    user = typing.cast(User, request.user)
    store = typing.cast(Store | None, user.last_accessed_store)

    if store:
        return Response(store.serialize())
    elif Store.objects.count():
        store = typing.cast(Store | None, Store.objects.first())

        if store:
            return Response(store.serialize())

    return Response(None)
