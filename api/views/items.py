import pydantic

from uuid import UUID
from decimal import Decimal

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from shared.view_tools import body_tools
from shared.view_tools.paths import Api
from shared.view_tools.exceptions import ApiException

from api.models.item import Item


item_api = Api("item/", name="Items")


class CreateItemInput(pydantic.BaseModel):
    name: str
    brand: str | None
    category: str | None
    purchase_price: Decimal
    selling_price: Decimal
    quantity: int


def create_item(request: Request) -> Response:
    return Response()


@item_api.endpoint_class("<item_id>", permission=IsAuthenticated)
class ItemGetUpdateDelete:
    def check_item_id(self, item_id: str) -> str:
        try:
            UUID(item_id)
        except ValueError:
            raise ApiException("Invalid item_id string")
        return item_id

    def get(self, request: Request, item_id: str) -> Response:
        item_id = self.check_item_id(item_id=item_id)
        item = Item.objects.get(id=item_id)
        return Response(item.serialize())

    class UpdateItemInput(pydantic.BaseModel):
        name: str | None
        brand: str | None
        category: str | None
        purchase_price: Decimal | None
        selling_price: Decimal | None
        quantity: int | None


    @body_tools.validate(UpdateItemInput)
    def update(self, request: Request, item_id: str) -> Response:
        data: ItemGetUpdateDelete.UpdateItemInput = body_tools.get_validated_body(request=request)

        item = Item.objects.get(id=item_id)

        if not all(
            [
                getattr(data, i)
                for i in [
                    "name",
                    "brand",
                    "category",
                    "purchase_price",
                    "selling_price",
                    "quantity",
                ]
            ]
        ):
            raise ApiException("Provide at least one parameter to be update")

        if data.name:
            item.name = data.name
        if data.brand:
            item.brand = data.brand
        if data.category:
            item.category = data.category
        if data.purchase_price:
            item.purchase_price = data.purchase_price
        if data.selling_price:
            item.selling_price = data.selling_price
        if data.quantity:
            item.quantity = data.quantity
        item.save()
        return Response()

    def delete(self, request: Request, item_id: str) -> Response:
        return Response()
