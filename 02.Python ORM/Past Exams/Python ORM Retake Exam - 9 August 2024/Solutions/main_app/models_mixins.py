from django.core.validators import MinLengthValidator
from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=80, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        abstract = True


class ModifiedAtAtMixin(models.Model):
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
