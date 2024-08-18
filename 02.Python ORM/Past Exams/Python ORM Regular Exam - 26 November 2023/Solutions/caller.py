import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Count, Q, Avg


# # 4.
def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    if search_name is not None and search_email is not None:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name is not None and search_email is None:
        query = Q(full_name__icontains=search_name)
    else:
        query = Q(email__icontains=search_email)

    all_authors = Author.objects.filter(query).order_by("-full_name")
    result = []

    for author in all_authors:
        status = "Banned" if author.is_banned else "Not Banned"
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return "\n".join(result)


# print(get_authors(search_name="author", search_email="Author"))


def get_top_publisher():
    top_publisher = Author.objects.get_authors_by_article_count().first()
    if not top_publisher or top_publisher.author_articles.count() == 0:
        return ""

    return f"Top Author: {top_publisher.full_name} with {top_publisher.num_articles} published articles."


# print(get_top_publisher())


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(
        num_of_reviews=Count("author_reviews")).filter(
        num_of_reviews__gt=0).order_by("-num_of_reviews", "email").first()

    if not top_reviewer:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_of_reviews} published reviews."


# print(get_top_reviewer())

# # 5.
def get_latest_article():
    last_article = Article.objects.order_by("-published_on").first()
    if not last_article:
        return ""

    all_authors = ", ".join(a.full_name for a in last_article.authors.all().order_by("full_name"))
    num_reviews = last_article.article_reviews.count()
    average_rating = (sum(r.rating for r in last_article.article_reviews.all()) /
                      len(last_article.article_reviews.all())) \
                      if len(last_article.article_reviews.all()) > 0 else 0

    return (f"The latest article is: {last_article.title}. "
            f"Authors: {all_authors}. "
            f"Reviewed: {num_reviews} times. "
            f"Average Rating: {average_rating:.2f}.")


# print(get_latest_article())


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(
        avg_rating=Avg("article_reviews__rating"),
        num_reviews=Count("article_reviews"))\
        .filter(num_reviews__gt=0).\
        order_by("-avg_rating", "title").first()

    if not top_rated_article:
        return ""

    return (f"The top-rated article is: {top_rated_article.title}, "
            f"with an average rating of {top_rated_article.avg_rating:.2f}, "
            f"reviewed {top_rated_article.num_reviews} times.")


# print(get_top_rated_article())


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    current_author = Author.objects.filter(email__exact=email).first()
    if not current_author:
        return "No authors banned."

    num_reviews = current_author.author_reviews.count()
    current_author.is_banned = True
    current_author.save()

    current_author.author_reviews.all().delete()

    return f"Author: {current_author.full_name} is banned! {num_reviews} reviews deleted."


# print(ban_author(email="Author1@Author1.com"))


