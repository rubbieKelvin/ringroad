from shared.serializers import Serializer

class ItemSerializer(Serializer):
    id = Serializer.field(cast=str)
    name = Serializer.field()
    brand = Serializer.field()
    category = Serializer.field()
    purchase_price = Serializer.field()
    selling_price = Serializer.field()
    quantity = Serializer.field()