import datetime
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
from main_app.custom_models_managers import HouseManager
from main_app.models_mixins import NameMixin, ModifiedAtAtMixin


class House(NameMixin, ModifiedAtAtMixin, models.Model):
    motto = models.TextField(null=True, blank=True)
    is_ruling = models.BooleanField(default=False)
    castle = models.CharField(max_length=80, null=True, blank=True)
    wins = models.PositiveSmallIntegerField(default=0)

    objects = HouseManager()

    def __str__(self):
        return self.name


class Dragon(NameMixin, ModifiedAtAtMixin, models.Model):
    BREATH_CHOICES = [
        ("Fire", "Fire"),
        ("Ice", "Ice"),
        ("Lightning", "Lightning"),
        ("Unknown", "Unknown"),
    ]

    power = models.DecimalField(max_digits=3, decimal_places=1, default=1.0,
                                validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    breath = models.CharField(max_length=9, choices=BREATH_CHOICES, default="Unknown")
    is_healthy = models.BooleanField(default=True)
    birth_date = models.DateField(default=datetime.date.today)
    wins = models.PositiveSmallIntegerField(default=0)
    house = models.ForeignKey(to=House, on_delete=models.CASCADE, related_name="house_dragons")

    def __str__(self):
        return self.name


class Quest(NameMixin, ModifiedAtAtMixin, models.Model):
    code = models.CharField(max_length=4, unique=True, validators=[RegexValidator(regex=r'^[A-Za-z#]{4}$')])
    reward = models.FloatField(default=100.0)
    start_time = models.DateTimeField()
    dragons = models.ManyToManyField(to=Dragon, related_name='dragons_quests')
    host = models.ForeignKey(to=House, on_delete=models.CASCADE, related_name='host_quests')

    def __str__(self):
        return self.name
