from django.core.validators import MinLengthValidator
from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LaunchDatedMixin(models.Model):
    launch_date = models.DateField()

    class Meta:
        abstract = True
