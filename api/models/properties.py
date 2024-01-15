from django.db import models
from shared.abstractmodel import AbstractModel
from api.constants.choices import PropertyTypes


class PropertyTemplate(AbstractModel):
    """
    Property templates are used to define the properties that can be added to
    products. They are not directly linked to products.
    """

    name = models.CharField(max_length=200, help_text="Property name")
    type = models.CharField(
        max_length=200, choices=PropertyTypes.choices, help_text="Property type"
    )


class ProductProperties(AbstractModel):
    """
    Products can have custom properties. This model represents those properties.
    """

    property = models.ForeignKey(
        "api.PropertyTemplate", on_delete=models.CASCADE, help_text="The property"
    )
    product = models.ForeignKey(
        "api.Product",
        on_delete=models.CASCADE,
        help_text="The product that owns the property",
    )
    value = models.TextField(
        help_text="The value of the property", null=True, blank=True
    )
