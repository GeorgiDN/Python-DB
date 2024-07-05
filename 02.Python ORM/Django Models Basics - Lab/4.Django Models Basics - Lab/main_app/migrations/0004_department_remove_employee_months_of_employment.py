# Generated by Django 4.2.4 on 2024-05-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_employee_months_of_employment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employees_count', models.PositiveIntegerField(default=1, verbose_name='Employees Count')),
                ('location', models.CharField(blank=True, choices=[('Sofia', 'Sofia'), ('Plovdiv', 'Plovdiv'), ('Burgas', 'Burgas'), ('Varna', 'Varna')], max_length=20, null=True)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='months_of_employment',
        ),
    ]
