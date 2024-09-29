from django.db import models
from django.core.validators import MinLengthValidator


class NameMixin(models.Model):
    name = models.CharField(max_length=80, unique=True,
                            validators=[MinLengthValidator(5)])

    class Meta:
        abstract = True


class ModifiedAtMixin(models.Model):
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WinsMixin(models.Model):
    wins = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
