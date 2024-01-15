from django.db import models
from shared.abstractmodel import AbstractModel, serialization


class Product(AbstractModel):
    """
    Represents a product in the store.
    """

    name = models.CharField(max_length=200, help_text="Product name")
    description = models.CharField(
        max_length=200, null=True, help_text="Product description"
    )
    code = models.CharField(max_length=200, null=True, help_text="Product code")
    brand = models.CharField(max_length=200, null=True, help_text="Product brand")
    category = models.CharField(max_length=200, null=True)
    quantity = models.PositiveBigIntegerField(default=0)
    store = models.ForeignKey(
        "Store", on_delete=models.CASCADE, help_text="The store that owns the product"
    )
    purchase_price = models.DecimalField(decimal_places=2, max_digits=9)
    selling_price = models.DecimalField(decimal_places=2, max_digits=9)
    product_image = models.CharField(
        max_length=200, null=True, help_text="Product image"
    )
