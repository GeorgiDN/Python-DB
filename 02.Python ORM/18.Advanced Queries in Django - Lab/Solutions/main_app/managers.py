from django.db import models
from django.db.models import QuerySet


# # 1.Available Products
class ProductManager(models.Manager):
    def available_products(self) -> QuerySet:
        return self.filter(is_available=True)

    def available_products_in_category(self, category_name: str):
        return self.filter(category__name=category_name, is_available=True)
