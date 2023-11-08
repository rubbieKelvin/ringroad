import typing
import pydantic
from uuid import UUID

from django.db import models
from api.models.user import User
from api.models.store import Store

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
from shared.view_tools import exceptions
from shared.view_tools import body_tools
from shared.view_tools.paths import Api
from utils.typecheck import validateUUID


store_api = Api("stores/", name="Store")


class CreateStoreInput(pydantic.BaseModel):
    name: str
    description: str | None = None


class UpdateStoreInput(pydantic.BaseModel):
    name: str | None = None
    description: str | None = None


@store_api.endpoint_class("", name="list and create store", permission=IsAuthenticated)
class CreateListStoresView:
    @body_tools.validate(CreateStoreInput)
    def post(self, request: Request) -> Response:
        data: CreateStoreInput = body_tools.get_validated_body(request)
        user: User = typing.cast(User, request.user)

        store = Store.objects.create(
            name=data.name,
            description=data.description,
            owner=user,
        )

        return Response(store.serialize(), status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        user: User = typing.cast(User, request.user)
        stores = Store.objects.filter(owner=user)
        return Response([store.serialize() for store in stores])


@store_api.endpoint_class(
    "<store_id>", name="get, update, delete", permission=IsAuthenticated
)
class GetUpdateDeleteStoresView:
    def get(self, request: Request, store_id: str) -> Response:
        """Returns the id if the user owns it or it's public"""
        validateUUID(store_id, "Invalid store id")

        store: Store = Store.objects.get_or_raise_exception(
            models.Q(id=store_id)
            & (models.Q(owner=request.user) | models.Q(is_public=True)),
            exceptions.ResourceNotFound("Store not found"),
        )

        return Response(store.serialize())

    @body_tools.validate(UpdateStoreInput)
    def patch(self, request: Request, store_id: str) -> Response:
        data: UpdateStoreInput = body_tools.get_validated_body(request)

        validateUUID(store_id, "Invalid store id")

        store: Store = Store.objects.get_or_raise_exception(
            models.Q(id=store_id), exceptions.ResourceNotFound("Store does not exist")
        )

        if data.name:
            store.name = data.name

        if data.description:
            store.description = data.description

        store.save()

        return Response(store.serialize())


def delete_store(self, request: Request, store_id: str) -> Response:
    validateUUID(store_id, "Invalid store id")

    store: Store = Store.objects.get_or_raise_exception(
        models.Q(id=store_id), exceptions.ResourceNotFound("Store does not exist")
    )

    store.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
