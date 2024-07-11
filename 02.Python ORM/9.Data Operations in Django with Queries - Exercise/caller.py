import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# 1. Pet #####################################################
def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


# 2. Artifact #######################################################
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)

    if artifact.age > 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)


# 3. Location #########################################
def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    return '\n'.join(map(str, locations))


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()

    # Location.objects.filter(pk=1).update(is_capital=True)


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


# 4. Car ########################################################
def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        discount = car.price * sum(int(x) for x in str(car.year)) / 100
        car.price_with_discount = car.price - discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.all().filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# function to put data in tables
# def insert_data_in_table_cars(model, year, color, price):
#     Car.objects.create(
#         model=model,
#         year=year,
#         color=color,
#         price=price,
#     )

# Test codes
# insert_data_in_table_cars("golf", 2000, 'red', 1000)
# apply_discount()
# delete_last_car()


# insert_data_in_table_cars("Mercedes C63 AMG", 2019, 'white', 120000.00)
# insert_data_in_table_cars("Audi Q7 S line", 2023, 'black', 183900.00)
# insert_data_in_table_cars("Chevrolet Corvette", 2021, 'dark grey', 199999.00)
#
# apply_discount()
# print(get_recent_cars())


# 5. Car ####################################################################
def show_unfinished_tasks():
    unfinished_tasks = Task.objects.all().filter(is_finished=False)
    return '\n'.join(map(str, unfinished_tasks))


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.all()
    decoded_text = ''.join(chr(ord(c) - 3) for c in text)
    tasks.filter(title=task_title).update(description=decoded_text)


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


# 6 HotelRoom #################################################################################
def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = [room for room in deluxe_rooms if room.id % 2 == 0]

    return '\n'.join(map(str, even_id_deluxe_rooms))


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")
    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id
        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_hotel_room = HotelRoom.objects.last()
    if last_hotel_room and not last_hotel_room.is_reserved:
        last_hotel_room.delete()


# function to put data in tables
# def insert_data_in_table_hotel_rooms(room_number, room_type, capacity, amenities, price_per_night):
#     HotelRoom.objects.create(
#         room_number=room_number,
#         room_type=room_type,
#         capacity=capacity,
#         amenities=amenities,
#         price_per_night=price_per_night
#     )


# insert_data_in_table_hotel_rooms(401, 'Standard', 2, 'Tv', 100.00)
# insert_data_in_table_hotel_rooms(501, 'Deluxe', 3, 'Wi-Fi', 200.00)
# insert_data_in_table_hotel_rooms(601, 'Deluxe', 6, 'Jacuzzi', 400.00)
#
#
#  # Test
# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)


# 7. #######################################################################################

def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + ' ' + second_character.name
    fusion_class_name = 'Fusion'
    fusion_level = int((first_character.level + second_character.level) // 2)
    fusion_strength = int((first_character.strength + second_character.strength) * 1.2)
    fusion_dexterity = int((first_character.dexterity + second_character.dexterity) * 1.4)
    fusion_intelligence = int((first_character.intelligence + second_character.intelligence) * 1.5)
    fusion_hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ("Mage", "Scout"):
        fusion_inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    else:
        fusion_inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class_name,
        level=fusion_level,
        strength=fusion_strength,
        dexterity=fusion_dexterity,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(
        dexterity=30,
    )


def grand_intelligence() -> None:
    Character.objects.update(
        intelligence=40,
    )


def grand_strength() -> None:
    Character.objects.update(
        strength=50,
    )


def delete_characters() -> None:
    Character.objects.filter(inventory='The inventory is empty').delete()


# Test code
# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
