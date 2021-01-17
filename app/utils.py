from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Cast


def validate_cart_products_list(products):
    if not isinstance(products, list):
        raise ValidationError('Cart products should be a list.')


def validate_cart_product_ids_exist(products):
    if not isinstance(products, list):
        return

    from .models import Product
    product_ids = [product['id'] for product in products]

    query = Product.objects.filter(id__in=product_ids)
    valid_ids = query.annotate(
        id_str=Cast('id', output_field=models.CharField())
    ).values_list('id_str', flat=True)

    invalid_ids = set(product_ids) - set(valid_ids)
    if invalid_ids:
        raise ValidationError(
            f'Invalid IDs found: {invalid_ids}'
        )
