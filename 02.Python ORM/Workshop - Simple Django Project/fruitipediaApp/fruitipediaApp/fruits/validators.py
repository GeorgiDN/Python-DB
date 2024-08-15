from django.core.exceptions import ValidationError


class OnlyLettersValidator:
    def __init__(self, message='Fruit name should contain only letters!'):
        self.message = message

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'fruitipediaApp.fruits.validators.OnlyLettersValidator', # Full import path to the validator class
            (), # Positional arguments (none in this case)
            {'message': self.message}  # Keyword arguments (the message in this case)
        )

