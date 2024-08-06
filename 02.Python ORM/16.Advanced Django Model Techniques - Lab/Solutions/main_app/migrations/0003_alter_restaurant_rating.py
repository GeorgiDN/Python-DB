# Generated by Django 5.0.4 on 2024-07-04 05:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0, message='Rating must be at least 0.00.'), django.core.validators.MaxValueValidator(5.0, message='Rating must be at least 5.00.')]),
        ),
    ]
