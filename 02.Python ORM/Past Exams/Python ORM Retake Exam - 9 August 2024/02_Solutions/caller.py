import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import House, Dragon, Quest
from django.db.models import Q, Count, F, Min, Avg


# 4.
def get_houses(search_string=None):
    if search_string is None or search_string == '':
        return 'No houses match your search.'

    query = Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)

    houses = House.objects.filter(query).order_by('-wins', 'name')
    if not houses:
        return 'No houses match your search.'

    result = []
    for house in houses:
        curr_motto = house.motto if house.motto else 'N/A'
        result.append(f'House: {house.name}, wins: {house.wins}, motto: {curr_motto}')

    return '\n'.join(result)


# print(get_houses('hou'))


def get_most_dangerous_house():
    most_dangerous_house = House.objects.get_houses_by_dragons_count().first()

    if not most_dangerous_house or most_dangerous_house.num_of_dragons == 0:
        return 'No relevant data.'

    current_ruling = 'ruling' if most_dangerous_house.is_ruling else 'not ruling'
    return (f"The most dangerous house is the House of {most_dangerous_house.name} "
            f"with {most_dangerous_house.num_of_dragons} dragons. "
            f"Currently {current_ruling} the kingdom.")


# print(get_most_dangerous_house())


def get_most_powerful_dragon():
    most_powerful_dragon = (Dragon.objects.annotate(num_quest=Count('dragons_quests'))
                            .filter(is_healthy=True).order_by('-power', 'name').first())

    if not most_powerful_dragon:
        return 'No relevant data.'

    return (f'The most powerful healthy dragon is {most_powerful_dragon.name} '
            f'with a power level of {most_powerful_dragon.power}, '
            f'breath type {most_powerful_dragon.breath}, and {most_powerful_dragon.wins} wins, '
            f'coming from the house of {most_powerful_dragon.house.name}. '
            f'Currently participating in {most_powerful_dragon.num_quest} quests.')

# print(get_most_powerful_dragon())


# 5.
def update_dragons_data():
    injured_dragons = Dragon.objects.filter(is_healthy=False, power__gt=1.0)
    if not injured_dragons:
        return 'No changes in dragons data.'

    num_of_affected_dragons = injured_dragons.update(
        power=F('power') - 0.1, is_healthy=True)

    min_power = Dragon.objects.aggregate(min_power=Min('power'))['min_power']

    return (f'The data for {num_of_affected_dragons} dragon/s has been changed. '
            f'The minimum power level among all dragons is {min_power:.1f}')


# print(update_dragons_data())


def get_earliest_quest():
    earliest_quest = Quest.objects.order_by('start_time').first()
    if not earliest_quest:
        return 'No relevant data.'

    # dragons_names = '*'.join(d.name for d in earliest_quest.dragons.all().order_by('-power', 'name'))
    # average_power_level = sum(d.power for d in earliest_quest.dragons.all()) / len(earliest_quest.dragons.all())
    dragons_names = '*'.join(earliest_quest.dragons.order_by('-power', 'name').values_list('name', flat=True))
    average_power_level = earliest_quest.dragons.aggregate(average_power=Avg('power'))['average_power']

    start_time = earliest_quest.start_time
    curr_day = start_time.day
    curr_month = start_time.month
    curr_year = start_time.year

    return (f'The earliest quest is: {earliest_quest.name}, code: {earliest_quest.code}, '
            f'start date: {curr_day}.{curr_month}.{curr_year}, host: {earliest_quest.host.name}. '
            f'Dragons: {dragons_names}. '
            f'Average dragons power level: {average_power_level:.2f}')


# print(get_earliest_quest())

def announce_quest_winner(quest_code):
    quest_winner = Quest.objects.filter(code__exact=quest_code).first()
    if not quest_winner:
        return 'No such quest.'

    dragon_winner = quest_winner.dragons.order_by('-power', 'name').first()
    dragon_winner.wins += 1
    dragon_winner.save()

    associated_house = dragon_winner.house
    associated_house.wins += 1
    associated_house.save()

    result = (f"The quest: {quest_winner.name} has been won by dragon {dragon_winner.name} "
              f"from house {associated_house.name}. "
              f"The number of wins has been updated as follows: "
              f"{dragon_winner.wins} total wins for the dragon and {associated_house.wins} total wins for the house. "
              f"The house was awarded with {quest_winner.reward:.2f} coins.")

    quest_winner.delete()
    return result


# print(announce_quest_winner("asd#"))
