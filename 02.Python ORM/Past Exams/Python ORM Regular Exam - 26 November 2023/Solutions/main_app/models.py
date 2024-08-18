from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.custom_model_manage import AuthorManager
from main_app.models_mixins import ContentMixin, PublishedOnMixin


class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2005)])
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()

    def __str__(self):
        return self.full_name


class Article(ContentMixin, PublishedOnMixin):
    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Science", "Science"),
        ("Education", "Education"),
    ]

    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="Technology")
    authors = models.ManyToManyField(to=Author, related_name="author_articles")

    def __str__(self):
        return self.title


class Review(ContentMixin, PublishedOnMixin):
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5)])
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="author_reviews")
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="article_reviews")

