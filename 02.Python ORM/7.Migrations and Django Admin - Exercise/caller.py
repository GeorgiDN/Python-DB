import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# from main_app.models import Shoe, Person
#
# print(Shoe.objects.values_list('brand', flat=True).distinct())

# print(Person.objects.all())

print(12)
