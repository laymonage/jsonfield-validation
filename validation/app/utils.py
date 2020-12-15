from django.core.exceptions import ValidationError
from django.db.models import Q

def add_product_to_cart(product, cart):
    for p in cart.products:
        if product.id == p['id']:
            p['quantity'] += 1
            break
    else:
        product_data = {
            'id': product.id,
            'type': type(product).__name__.lower(),
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        }
        cart.products.append(product_data)


def validate_cart_products_list(products):
    if not isinstance(products, list):
        raise ValidationError('Cart products should be a list.')


def validate_cart_product_ids_exist(products):
    from .models import Smartphone, Notebook
    models = {
        'smartphone': Smartphone,
        'notebook': Notebook,
    }
    model_ids = {
        'smartphone': [],
        'notebook': [],
    }

    for product in products:
        model_ids[product['type']].append(product['id'])

    for name, model in models.items():
        query = model.objects.filter(id__in=model_ids[name])
        valid_ids = query.values_list('id', flat=True)
        invalid_ids = set(valid_ids) - set(model_ids[name])
        if invalid_ids:
            raise ValidationError(
                f'Invalid IDs found for {name}: {invalid_ids}'
            )
