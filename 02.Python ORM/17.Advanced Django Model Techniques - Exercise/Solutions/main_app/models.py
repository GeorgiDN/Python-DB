from django.db import models
from decimal import Decimal

from django.contrib.postgres.search import SearchVectorField
from django.core.validators import MinLengthValidator

from main_app.validators import validate_name, validate_age, validate_phone_number


# # 1. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name],
    )
    age = models.PositiveIntegerField(
        validators=[validate_age],
    )
    email = models.EmailField(
        error_messages={
            "invalid": "Enter a valid email address"
        }
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[validate_phone_number],
    )
    website_url = models.URLField(
        error_messages={
            'invalid': "Enter a valid URL"
        }
    )


# # 2. Media
class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_at', "title"]

    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    genre = models.CharField(
        max_length=50
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, message="Author must be at least 5 characters long")
        ],
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(6, message="ISBN must be at least 6 characters long")
        ],
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, message="Director must be at least 8 characters long")
        ],
    )


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"

    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, message="Artist must be at least 9 characters long")
        ],
    )


# # 3.Tax-Inclusive Pricing
class Product(models.Model):
    TAX_RATE = Decimal("0.08")
    MULTIPLIER = Decimal('2.00')
    DISCOUNTED_TAX_RATE = Decimal('0.05')
    DISCOUNTED_MULTIPLIER = Decimal('1.50')

    name = models.CharField(
        max_length=100,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def calculate_tax(self)  -> Decimal:
        if type(self).__name__ == 'Product':
            tax = Product.TAX_RATE
        else:
            tax = Product.DISCOUNTED_TAX_RATE
        return self.price * tax

    def calculate_shipping_cost(self, weight: Decimal):
        if type(self).__name__ == 'Product':
            multiplier = Product.MULTIPLIER
        else:
            multiplier = Product.DISCOUNTED_MULTIPLIER
        return weight * multiplier

    def format_product_name(self):
        if type(self).__name__ == 'Product':
            product_type = type(self).__name__
        else:
            product_type = "Discounted Product"
        return f"{product_type}: {self.name}"


class DiscountedProduct(Product):
    MARKUP = Decimal("1.20")

    class Meta:
        proxy = True

    def calculate_price_without_discount(self) -> Decimal:
        return self.price * DiscountedProduct.MARKUP


# # 4.Superhero Universe
class RechargeEnergyMixin:
    def recharge_energy(self, amount: int):
        increased_amount = self.energy + amount
        self.energy = min(increased_amount, 100)
        self.save()


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(
        max_length=100,
    )
    hero_title = models.CharField(
        max_length=100,
    )
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy < 80:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        self.energy -= 80
        if self.energy == 0:
            self.energy = 1
        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):

    class Meta:
        proxy = True

    def run_at_super_speed(self):
        if self.energy < 65:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        self.energy -= 65
        if self.energy == 0:
            self.energy = 1
        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"



# # 05. *Vector Searching
class Document(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['search_vector']),
        ]

    title = models.CharField(max_length=200, )
    content = models.TextField()
    search_vector = SearchVectorField(null=True)
