# Generated by Django 5.0.4 on 2024-05-28 05:06

from django.db import migrations


def set_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    items = item_model.objects.all()

    for record in items:
        if record.price <= 10:
            record.rarity = 'Rare'
        elif 11 <= record.price <= 20:
            record.rarity = 'Very Rare'
        elif 21 <= record.price <= 30:
            record.rarity = 'Extremely Rare'
        else:
            record.rarity = 'Mega Rare'

        # record.rarity = 'Rare' if record.price <= 10 \
        #     else record.rarity = 'Very Rare' if 11 <= record.price <= 20 \
        #     else record.rarity = 'Extremely Rare' if 21 <= record.price <= 30 \
        #     else record.rarity = 'Mega Rare'

    item_model.objects.bulk_update(items, ['rarity'])


def set_rarity_default(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    items = item_model.objects.all()

    rarity_default = item_model._meta.get_field('rarity').default

    for record in items:
        record.rarity = rarity_default

    item_model.objects.bulk_update(items, ['rarity'])


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_rarity, reverse_code=set_rarity_default)
    ]
