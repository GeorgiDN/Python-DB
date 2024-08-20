from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from main_app.custom_models_manager import AstronautManager
from main_app.models_mixins import NameMixin, UpdatedAtMixin, LaunchDatedMixin


class Astronaut(NameMixin, UpdatedAtMixin, models.Model):
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex=r"^\d+$")])
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(NameMixin, UpdatedAtMixin, LaunchDatedMixin, models.Model):
    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name


class Mission(NameMixin, UpdatedAtMixin, LaunchDatedMixin, models.Model):
    STATUS_CHOICES = [
        ("Planned", "Planned"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
    ]

    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=9, default="Planned", choices=STATUS_CHOICES)
    spacecraft = models.ForeignKey(to=Spacecraft, on_delete=models.CASCADE, related_name="spacecraft_missions")
    astronauts = models.ManyToManyField(to=Astronaut, related_name="astronauts_missions")
    commander = models.ForeignKey(to=Astronaut, on_delete=models.SET_NULL,
                                  related_name="commander_missions",
                                  null=True, blank=True)

    def __str__(self):
        return self.name
