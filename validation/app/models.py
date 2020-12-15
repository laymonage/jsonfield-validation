import uuid

from django.contrib.auth.models import User
from django.db import models

from .utils import validate_cart_products_list, validate_cart_product_ids_exist


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock_qty = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} (Stock: {self.stock_qty})'


class Smartphone(Product):
    chipset = models.CharField(max_length=255)
    nfc = models.BooleanField()


class Notebook(Product):
    cpu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.JSONField(
        validators=[
            validate_cart_products_list,
            validate_cart_product_ids_exist,
        ],
        blank=True,
    )
