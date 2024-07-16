import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from typing import List
from django.db.models import Q, When, Value, QuerySet, Case, F


# 1. ArtworkGallery
def show_highest_rated_art():
    highest_rated_art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{highest_rated_art.art_name} is the highest-rated art with a {highest_rated_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    art_with_negative_rating = ArtworkGallery.objects.filter(rating__lt=0)
    art_with_negative_rating.delete()


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)

# Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


# 2.Laptop
def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(*args: List[Laptop]):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)

    #Laptop.objects.filter(Q(brand='Asus') | Q(brand='Lenovo')).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)

    # Laptop.objects.filter(Q(brand="Apple") | Q(brand="Dell") | Q(brand="Acer")).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value('Windows')),
            When(brand='Apple', then=Value('MacOS')),
            When(brand__in=['Dell', 'Acer'], then=Value('Linux')),
            When(brand='Lenovo', then=Value('Chrome OS')),
            default=F('operation_system')
        )
    )


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='MacOS',
#     price=899.99
# )
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Chrome OS',
#     memory=16,
#     storage=256,
#     operation_system='MacOS',
#     price=1399.99
# )
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=256,
#     operation_system='Linux',
#     price=999.99,
# )

# Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
#
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)

# update_to_512_GB_storage()
# update_operation_systems()

# # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)


# 3.
def bulk_create_chess_players(*args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2299, 2200)).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(2199,0)).update(title="regular player")


player1 = ChessPlayer(
    username='Player1',
    title='no title',
    rating=2200,
    games_played=50,
    games_won=20,
    games_lost=25,
    games_drawn=5,
)
player2 = ChessPlayer(
    username='Player2',
    title='IM',
    rating=2350,
    games_played=80,
    games_won=40,
    games_lost=25,
    games_drawn=15,
)

# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])
#
# # Call the delete_chess_players function
# delete_chess_players()
#
# # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())


# 4. Meal
def set_new_chefs():
    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value('Gordon Ramsay')),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller")),
            default=F('chef'),
        )
    )


def set_new_preparation_times():
    Meal.objects.filter(meal_type="Breakfast").update(preparation_time="10 minutes")
    Meal.objects.filter(meal_type="Lunch").update(preparation_time="12 minutes")
    Meal.objects.filter(meal_type="Dinner").update(preparation_time="15 minutes")
    Meal.objects.filter(meal_type="Snack").update(preparation_time="5 minutes")


    # Meal.objects.update(
    #     preparation_time=Case(
    #         When(meal_type='Breakfast', then=Value('10 minutes')),
    #         When(meal_type='Lunch', then=Value('12 minutes')),
    #         When(meal_type='Dinner', then=Value('15 minutes')),
    #         When(meal_type='Snack', then=Value('5 minutes')),
    #         default=F('preparation_time')
    #     )
    # )


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=["Breakfast", "Dinner"]).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()


# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )
# Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()

# Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)


# 5.
def show_hard_dungeons():
    hard_dungeons = Dungeon.objects.filter(difficulty="Hard").order_by("-location")
    result = [
        f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!"
        for d in hard_dungeons]

    return "\n".join(result)


def bulk_create_dungeons(*args: List[Dungeon]):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


############################ Helper function ######################
def update_dungeon_fields(search_field, criteria, **update_fields):
    filter_kwargs = {search_field: criteria}
    Dungeon.objects.filter(**filter_kwargs).update(**update_fields)
######################################################################################


def update_dungeon_names():
    update_dungeon_fields("difficulty", "Easy", name="The Erased Thombs")
    update_dungeon_fields("difficulty", "Medium", name="The Coral Labyrinth")
    update_dungeon_fields("difficulty", "Hard", name="The Lost Haunt")

    # Dungeon.objects.update(
    #     name=Case(
    #         When(difficulty="Easy", then=Value('The Erased Thombs')),
    #         When(difficulty="Medium", then=Value('The Coral Labyrinth')),
    #         When(difficulty="Hard", then=Value('The Lost Haunt')),
    #         default=F('name')
    #     )
    # )


def update_dungeon_recommended_levels():
    update_dungeon_fields("difficulty", "Easy", recommended_level=25)
    update_dungeon_fields("difficulty", "Medium", recommended_level=50)
    update_dungeon_fields("difficulty", "Hard", recommended_level=75)


def update_dungeon_rewards():
    update_dungeon_fields("boss_health", 500, reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations():
    update_dungeon_fields("recommended_level", 25, location="Enchanted Maze")
    update_dungeon_fields("recommended_level", 50, location="Grimstone Mines")
    update_dungeon_fields("recommended_level", 75, location="Shadowed Abyss")


# # Create two instances
# dungeon1 = Dungeon(
#     name="Dungeon 1",
#     boss_name="Boss 1",
#     boss_health=1000,
#     recommended_level=75,
#     reward="Gold",
#     location="Eternal Hell",
#     difficulty="Hard",
# )
#
# dungeon2 = Dungeon(
#     name="Dungeon 2",
#     boss_name="Boss 2",
#     boss_health=400,
#     recommended_level=25,
#     reward="Experience",
#     location="Crystal Caverns",
#     difficulty="Easy",
# )
#
# # Bulk save the instances
# bulk_create_dungeons([dungeon1, dungeon2])
#
# # Update boss's health
# update_dungeon_bosses_health()
#
# # Show hard dungeons
# hard_dungeons_info = show_hard_dungeons()
# print(hard_dungeons_info)
#
# # Change dungeon names based on difficulty
# update_dungeon_names()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].name)
# print(dungeons[1].name)
#
# # Change the dungeon rewards
# update_dungeon_rewards()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].reward)
# print(dungeons[1].reward)


# 6.
############################ Helper function ######################
def update_workout_fields(search_field, criteria, **update_fields):
    filter_kwargs = {search_field: criteria}
    Workout.objects.filter(**filter_kwargs).update(**update_fields)
######################################################################################


def show_workouts() -> str:
    workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"]).order_by("id")
    return "\n".join(map(str, workouts))


def get_high_difficulty_cardio_workouts() -> QuerySet:
    workers = Workout.objects.filter(workout_type="Cardio", difficulty="High").order_by("instructor")
    return workers


def set_new_instructors():
    update_workout_fields("workout_type", "Cardio", instructor="John Smith")
    update_workout_fields("workout_type", "Strength", instructor="Michael Williams")
    update_workout_fields("workout_type", "Yoga", instructor="Emily Johnson")
    update_workout_fields("workout_type", "CrossFit", instructor="Sarah Davis")
    update_workout_fields("workout_type", "Calisthenics", instructor="Chris Heria")


def set_new_duration_times():
    update_workout_fields("instructor", "John Smith", duration="15 minutes")
    update_workout_fields("instructor", "Sarah Davis", duration="30 minutes")
    update_workout_fields("instructor", "Chris Heria", duration="45 minutes")
    update_workout_fields("instructor", "Michael Williams", duration="1 hour")
    update_workout_fields("instructor", "Emily Johnson", duration="1 hour and 30 minutes")


def delete_workouts():
    Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()


# # Create two Workout instances
# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Bob"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="Lilly"
# )
#
# # Run the functions
# print(show_workouts())
#
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")
#
# set_new_instructors()
# for workout in Workout.objects.all():
#     print(f"Instructor: {workout.instructor}")
#
# set_new_duration_times()
# for workout in Workout.objects.all():
#     print(f"Duration: {workout.duration}")
