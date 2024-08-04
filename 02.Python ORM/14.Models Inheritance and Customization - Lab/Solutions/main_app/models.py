from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


# # 7.Veterinarian Availability
class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (True, "Available"),
            (False, "Not Available"),
        )
        kwargs['default'] = True
        super().__init__(*args, **kwargs)


# # 1.Zoo Animals
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    # # 6. Animals' Age
    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


# # 2.Zoo Employees
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class SpecialtyChoices(models.TextChoices):
        Mammals = ('Mammals', 'Mammals')
        Birds = ('Birds', 'Birds')
        Reptiles = ('Reptiles', 'Reptiles')
        Others = ('Others', 'Others')

    specialty = models.CharField(max_length=10,
                                 choices=SpecialtyChoices.choices)

    managed_animals = models.ManyToManyField(to='Animal',
                                             related_name='animals')

    # # 04. Zookeeper's Specialty
    def clean(self):
        super().clean()

        if self.specialty not in self.SpecialtyChoices:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)

    # # 7.
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability


# # 3. Animal Display System
class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    # # 5. Animal Display System Logic
    def display_info(self):
        return (f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. "
                f"It makes a noise like '{self.sound}'.")

    def is_endangered(self):
        if self.species in ["Cross River Gorilla", "Orangutan",  "Green Turtle"]:
            return f"{self.species} is at risk!"
        return f"{self.species} is not at risk."



