from django.db import models
from django.utils.translation import gettext_lazy as translate


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(BaseModel):
    name = models.TextField(default="<product name>")
    price = models.FloatField(default=0.0)
    currency_symbol = models.CharField(max_length=3)


class Discount(BaseModel):
    class Conditions(models.TextChoices):
        PRICE_GREATER_THAN = "PGT", translate("Price >")
        PRICE_LESS_THAN = "PLT", translate("Price <")
        PRICE_GREATER_THAN_OR_EQUAL_TO = "PGE", translate("Price >=")
        PRICE_LESS_THAN_OR_EQUAL_TO = "PLE", translate("Price <=")
        QUANTITY_GREATER_THAN = "QGT", translate("Quantity >")
        QUANTITY_LESS_THAN = "QLT", translate("Quantity <")
        QUANTITY_GREATER_THAN_OR_EQUAL_TO = "QGE", translate("Quantity >=")
        QUANTITY_LESS_THAN_OR_EQUAL_TO = "QLE", translate("Quantity <=")

    class Type(models.TextChoices):
        PERCENT = "PCT", translate("Discount %")
        PRICE = "PRC", translate("New price per unit")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    condition = models.CharField(
        max_length=3,
        choices=Conditions.choices
    )
    test_value = models.FloatField(default=0)
    type = models.CharField(
        max_length=3,
        choices=Type.choices,
        default=Type.PRICE
    )
    discount_value = models.FloatField(default=0)


class Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
