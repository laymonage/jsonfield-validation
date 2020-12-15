# Generated by Django 3.1.2 on 2020-10-21 01:33

from django.db import migrations


def create_product_objects(apps, schema_editor):
    Smartphone = apps.get_model('app', 'Smartphone')
    Notebook = apps.get_model('app', 'Notebook')

    Smartphone.objects.bulk_create([
        Smartphone(
            name='Poco X3',
            price=300,
            stock_qty=1000,
            chipset='Snapdragon 732G',
            nfc=True,
        ),
        Smartphone(
            name='Galaxy S20',
            price=1500,
            stock_qty=100,
            chipset='Snapdragon 865',
            nfc=True,
        ),
    ])

    Notebook.objects.bulk_create([
        Notebook(
            name='Thinkpad T480',
            price=1200,
            stock_qty=50,
            cpu='Intel Core i5 8th Gen',
            gpu='Intel UHD Graphics',
        ),
        Notebook(
            name='Dell XPS 13',
            price=2000,
            stock_qty=100,
            cpu='Intel Core i7 10th Gen',
            gpu='Intel UHD Graphics',
        ),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_product_objects),
    ]
