from django.core.exceptions import ValidationError


def validate_menu_categories(value: str):
    required_categories = ["Appetizers", "Main Course", "Desserts"]
    all_categories_are_included = all(category.lower() in value.lower() for category in required_categories)
    if not all_categories_are_included:
        raise ValidationError(
            'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
        )
