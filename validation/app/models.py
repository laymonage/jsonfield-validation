import uuid

from django.contrib.auth.models import User
from django.db import models

from .utils import validate_cart_products_list, validate_cart_product_ids_exist


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock_qty = models.PositiveIntegerField()
    data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f'{self.name} (Stock: {self.stock_qty})'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.JSONField(
        default=list,
        blank=True,
        validators=[
            validate_cart_products_list,
            validate_cart_product_ids_exist,
        ],
    )

    def __str__(self):
        return f'{self.user.username} ({len(self.products)} kinds)'

    def add_product(self, product):
        for existing in self.products:
            if existing['id'] == product.id.hex:
                existing['quantity'] += 1
                break
        else:
            product_data = {
                'id': product.id.hex,
                'name': product.name,
                'price': float(product.price),
                'quantity': 1,
            }
            self.products.append(product_data)
