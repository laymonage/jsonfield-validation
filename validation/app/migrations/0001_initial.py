# Generated by Django 3.1.2 on 2020-10-19 09:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock_qty', models.PositiveIntegerField()),
                ('cpu', models.CharField(max_length=255)),
                ('gpu', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock_qty', models.PositiveIntegerField()),
                ('chipset', models.CharField(max_length=255)),
                ('nfc', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]