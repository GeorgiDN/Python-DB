import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import House, Dragon, Quest
from django.db.models import Q, Count, F, Min
from decimal import Decimal


# # 4.
def get_houses(search_string=None):
    if search_string is None or search_string == "":
        return "No houses match your search."

    query = Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)

    houses = House.objects.filter(query).order_by("-wins", "name")
    if not houses:
        return "No houses match your search."

    result = []

    for house in houses:
        curr_motto = house.motto if house.motto else "N/A"
        result.append(f"House: {house.name}, wins: {house.wins}, motto: {curr_motto}")

    return "\n".join(result)


# print(get_houses(""))


def get_most_dangerous_house():
    most_dangerous_house = House.objects.get_houses_by_dragons_count().first()

    if not most_dangerous_house or most_dangerous_house.num_of_dragons == 0:
        return "No relevant data."

    curr_ruling = "ruling" if most_dangerous_house.is_ruling else "not ruling"

    return (f"The most dangerous house is the House of {most_dangerous_house.name} with {most_dangerous_house.num_of_dragons} dragons. "
            f"Currently {curr_ruling} the kingdom.")


# print(get_most_dangerous_house())


def get_most_powerful_dragon():
    found_dragon = (Dragon.objects.annotate(num_quests=Count("dragons_quests"))
                            .filter(is_healthy=True).order_by("-power", "name").first())

    if not found_dragon:
        return "No relevant data."

    return (f"The most powerful healthy dragon is {found_dragon.name} with a power level of {found_dragon.power:.1f}, "
            f"breath type {found_dragon.breath}, and {found_dragon.wins} wins, coming from the house of {found_dragon.house.name}. "
            f"Currently participating in {found_dragon.num_quests} quests.")


# print(get_most_powerful_dragon())


# # 5.

def update_dragons_data():
    injured_dragons = Dragon.objects.filter(is_healthy=False, power__gt=1.0)
    if not injured_dragons:
        return "No changes in dragons data."

    num_of_dragons_affected = injured_dragons.count()
    for dragon in injured_dragons:
        dragon.power -= Decimal("0.1")
        dragon.is_healthy = True
        dragon.save()

    injured_dragons.update(power=F("power") - 0.1)
    min_power = Dragon.objects.aggregate(min_power=Min("power"))["min_power"]

    return (f"The data for {num_of_dragons_affected} dragon/s has been changed. "
            f"The minimum power level among all dragons is {min_power:.1f}")


# print(update_dragons_data())


def get_earliest_quest():
    found_quest = Quest.objects.order_by("start_time").first()
    if not found_quest:
        return "No relevant data."

    dragons_names = "*".join(d.name for d in found_quest.dragons.all().order_by("-power", "name"))
    avg_power_level = sum(d.power for d in found_quest.dragons.all()) / len(found_quest.dragons.all()) if found_quest else 0

    start_time = found_quest.start_time
    curr_day = start_time.day
    curr_month = start_time.month
    curr_year = start_time.year

    return (f"The earliest quest is: {found_quest.name}, "
            f"code: {found_quest.code}, "
            f"start date: {curr_day}.{curr_month}.{curr_year}, "
            f"host: {found_quest.host.name}. "
            f"Dragons: {dragons_names}. "
            f"Average dragons power level: {avg_power_level:.2f}")


# print(get_earliest_quest())


def announce_quest_winner(quest_code):
    quest_winner = Quest.objects.filter(code=quest_code).first()
    if not quest_winner:
        return "No such quest."

    winner = quest_winner.dragons.order_by("-power", "name").first()

    winner.wins += 1
    winner.save()

    associated_house = winner.house
    associated_house.wins += 1
    associated_house.save()

    result = (
        f"The quest: {quest_winner.name} has been won by dragon {winner.name} from house {associated_house.name}. "
        f"The number of wins has been updated as follows: {winner.wins} "
        f"total wins for the dragon and {associated_house.wins} total wins for the house. "
        f"The house was awarded with {quest_winner.reward:.2f} coins.")

    quest_winner.delete()

    return result


# print(announce_quest_winner("zxcv"))
