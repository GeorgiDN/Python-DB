# Generated by Django 5.0.4 on 2024-05-28 06:33

from django.db import migrations
from django.utils import timezone


def update_delivery_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    for delivery_order in orders:
        if delivery_order.status == 'Pending':
            delivery_order.delivery = delivery_order.delivery_order.order_date + timezone.timedelta(days=3)
            delivery_order.save()
        elif delivery_order.status == 'Completed':
            delivery_order.warranty = '24 months'
            delivery_order.save()
        elif delivery_order.status == 'Cancelled':
            delivery_order.delete()


def reverse_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    default_delivery = None
    default_warranty = order_model._meta.get_field('warranty').default

    for delivery_order in orders:
        delivery_order.delivery = default_delivery
        delivery_order.warranty = default_warranty

    order_model.objects.bulk_update(orders, ['delivery', 'warranty'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_order'),
    ]

    operations = [
        migrations.RunPython(update_delivery_warranty, reverse_code=reverse_delivery_and_warranty)
    ]
