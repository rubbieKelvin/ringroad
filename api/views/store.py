import typing
import pydantic

from api.models.store import Store
from api.models.user import User

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
from uuid import UUID
from shared.view_tools import exceptions
from shared.view_tools import body_tools
from shared.view_tools.paths import Api
from utils.typecheck import validateUUID


store_api = Api("store/", name="Store")


class CreateStoreInput(pydantic.BaseModel):
    name: str
    description: str


@store_api.endpoint("create", method="POST", permission=IsAuthenticated)
@body_tools.validate(CreateStoreInput)
def create_store(request: Request) -> Response:
    data: CreateStoreInput = body_tools.get_validated_body(request)
    user: User = typing.cast(User, request.user)

    store = Store.objects.create(
        name=data.name,
        description=data.description,
        owner=user,
    )

    return Response(store.serialize(), status=status.HTTP_201_CREATED)


class UpdateStoreInput(pydantic.BaseModel):
    name: str | None = None
    description: str | None = None


@store_api.endpoint("update/<id>", method="PATCH", permission=IsAuthenticated)
@body_tools.validate(UpdateStoreInput)
def update_store(request: Request, id: str) -> Response:
    data: UpdateStoreInput = body_tools.get_validated_body(request)
    if data.name==None and  data.description==None:
        raise exceptions.ApiException("Pass in atlest one")

    validateUUID(id, "Invalid store id")

    try:
        store: Store = Store.objects.get(id=id)

        if data.name:
            store.name = data.name
        if data.description:
            store.description = data.description
        store.save()
        return Response(store.serialize())

    except Store.DoesNotExist:
        raise exceptions.ResourceNotFound("Store does not exist")


@store_api.endpoint("delete/<id>", method="DELETE", permission=IsAuthenticated)
def delete_store(request: Request, id: str) -> Response:
    validateUUID(id, "Invalid store id")

    try:
        store: Store = Store.objects.get(id=id)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Store.DoesNotExist:
        raise exceptions.ResourceNotFound("Store does not exist")


@store_api.endpoint("get", method="GET", permission=IsAuthenticated)
def get_stores(request: Request) -> Response:
    user: User = typing.cast(User, request.user)
    stores = Store.objects.filter(owner=user)
    return Response([store.serialize() for store in stores])

#"4207364a-1525-4f02-8d07-4ec3c94fcdab"
# "04a25d81-dd53-4466-b229-5df76f243577"