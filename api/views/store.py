import typing
import pydantic

from api.models.store import Store
from api.models.user import User

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers

from shared.view_tools import exceptions
from shared.view_tools import body_tools
from shared.view_tools.paths import Api


store_api = Api("store/", name="Store")


# TODO: review
class UpdateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["name", "description"]


class CreateStoreInput(pydantic.BaseModel):
    store_name: str
    store_description: str


@store_api.endpoint("create", method="POST", permission=IsAuthenticated)
@body_tools.validate(CreateStoreInput)
def create_store(request: Request) -> Response:
    data: CreateStoreInput = body_tools.get_validated_body(request=request)
    user: User = typing.cast(request.user, User)

    store = Store.objects.create(
        store_name=data.store_name, store_description=data.store_description, owner=user
    )

    return Response(status=status.HTTP_201_CREATED)


@store_api.endpoint("update-store/<id>", method="PATCH", permission=IsAuthenticated)
@body_tools.validate(CreateStoreInput)
def update_store(request: Request, id: str) -> Response:
    data: CreateStoreInput = body_tools.get_validated_body(request=request)
    user: User = typing.cast(request.user, User)

    try:
        store = Store.objects.get(id=id)
        if store:
            store_update_data = UpdateStoreSerializer(instance=user, data=request.data, partial=True)  # type: ignore
            if store_update_data.is_valid():
                store_update_data.save()
                return Response(status=status.HTTP_201_CREATED)

            else:
                return Response("invalid data format")
        else:
            return Response("store is not the right store")

    except Store.DoesNotExist:
        raise exceptions.ApiException("store does not exist!")


@store_api.endpoint("delete/<id>", method="POST", permission=IsAuthenticated)
def delete_store(request: Request, id: str) -> Response:
    user = request.user

    try:
        store = Store.objects.get(id=id)
        store.delete()
        return Response("successfully deleted")
    except Store.DoesNotExist:
        raise exceptions.ResourceNotFound("Store not found")
