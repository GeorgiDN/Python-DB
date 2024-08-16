import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from django.db.models import Q, Count, Avg, F


# # 4.
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    if search_name is not None and search_nationality is not None:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
    elif search_name is not None and search_nationality is None:
        query = Q(full_name__icontains=search_name)
    else:
        query = Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query).order_by('full_name')
    if directors is None:
        return ''

    result = []
    for director in directors:
        result.append(f'Director: {director.full_name}, nationality: {director.nationality}, '
                      f'experience: {director.years_of_experience}')

    return '\n'.join(result)


# print(get_directors())


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    if not top_director:
        return ''

    return f"Top Director: {top_director.full_name}, movies: {top_director.num_movies}."


# print(get_top_director())


def get_top_actor():
    top_actor = (Actor.objects.prefetch_related('starring_actor_movies')
                 .annotate(num_movies=Count('starring_actor_movies'),
                           average_rating=Avg('starring_actor_movies__rating'))
                 .order_by('-num_movies', 'full_name')).first()

    if not top_actor or top_actor.num_movies == 0:
        return ''

    all_movies = ', '.join(m.title for m in top_actor.starring_actor_movies.all())

    return (f"Top Actor: {top_actor.full_name}, starring in movies: {all_movies}, "
            f"movies average rating: {top_actor.average_rating:.1f}")


# print(get_top_actor())


# # 5.
def get_actors_by_movies_count():
    top_three_actors = Actor.objects.annotate(
        num_movies=Count('actor_movies')).order_by('-num_movies', 'full_name')[:3]

    if not top_three_actors or top_three_actors[0].num_movies == 0:
        return ''

    result = []
    for actor in top_three_actors:
        result.append(f'{actor.full_name}, participated in {actor.num_movies} movies')

    return '\n'.join(result)


# print(get_actors_by_movies_count())


def get_top_rated_awarded_movie():
    top_rated_movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()

    if not top_rated_movie:
        return ''

    main_actor = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor else 'N/A'
    actors_in_top_rated_movie = top_rated_movie.actors.all().order_by('full_name')
    actors_full_names = ', '.join(a.full_name for a in actors_in_top_rated_movie)

    return (f"Top rated awarded movie: {top_rated_movie.title}, "
            f"rating: {top_rated_movie.rating:.1f}. "
            f"Starring actor: {main_actor}. Cast: {actors_full_names}.")


# print(get_top_rated_awarded_movie())


def increase_rating():
    movies_for_increase = Movie.objects.filter(is_classic=True, rating__lt=10)
    if not movies_for_increase:
        return "No ratings increased."

    num_of_updated_movies = movies_for_increase.update(rating=F('rating') + 0.1)

    return f"Rating increased for {num_of_updated_movies} movies."


# print(increase_rating())
