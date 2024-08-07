from django.core.exceptions import ValidationError
import re


def validate_name(value):
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError("Name can only contain letters and spaces")


def validate_age(value):
    if value < 18:
        raise ValidationError("Age must be greater than or equal to 18")


def validate_phone_number(value):
    pattern = r"^\+359\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError("Phone number must start with '+359' followed by 9 digits")
