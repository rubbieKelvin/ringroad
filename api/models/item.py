from django.db import models
from shared.abstractmodel import AbstractModel, serialization


class Item(AbstractModel):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=9)
    selling_price = models.DecimalField(decimal_places=2, max_digits=9)
    quantity = models.IntegerField()
