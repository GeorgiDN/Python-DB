# Generated by Django 5.0.4 on 2024-07-01 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_owner_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=10, unique=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='main_app.car')),
            ],
        ),
    ]
