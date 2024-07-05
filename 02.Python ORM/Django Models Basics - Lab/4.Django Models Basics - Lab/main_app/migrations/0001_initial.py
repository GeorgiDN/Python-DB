# Generated by Django 4.2.4 on 2024-05-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('photo', models.URLField()),
                ('birth_date', models.DateField()),
                ('works_full_time', models.BinaryField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
