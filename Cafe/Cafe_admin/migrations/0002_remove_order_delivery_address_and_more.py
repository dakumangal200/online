# Generated by Django 5.0 on 2024-04-08 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Delivery_status',
        ),
    ]
