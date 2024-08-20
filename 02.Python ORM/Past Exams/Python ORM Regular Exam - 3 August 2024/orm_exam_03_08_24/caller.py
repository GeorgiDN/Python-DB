import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, Avg
from main_app.models import Astronaut, Spacecraft, Mission


# # 4.
def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    found_astronauts = Astronaut.objects.filter(query).order_by('name')
    if not found_astronauts:
        return ""

    result = []
    for astronauts in found_astronauts:
        status = "Active" if astronauts.is_active else "Inactive"
        result.append(f"Astronaut: {astronauts.name}, phone number: {astronauts.phone_number}, status: {status}")

    return "\n".join(result)


# print(get_astronauts(search_string="Astronau"))

def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()
    if not top_astronaut or top_astronaut.missions_count == 0:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


# print(get_top_astronaut())


def get_top_commander():
    top_commander = (Astronaut.objects.annotate(num_of_missions=Count('commander_missions')).
                     order_by('-num_of_missions', 'phone_number').first())

    if not top_commander or top_commander.num_of_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_missions} commanded missions."


# print(get_top_astronaut())


# # 5.
def get_last_completed_mission():
    last_mission = Mission.objects.filter(status="Completed").order_by("-launch_date").first()
    if not last_mission:
        return "No data."

    commander_name = last_mission.commander.name if last_mission.commander else "TBA"
    astronauts_names = ", ".join(a.name for a in last_mission.astronauts.all().order_by("name"))
    total_spacewalks = sum(a.spacewalks for a in last_mission.astronauts.all())

    return (f"The last completed mission is: {last_mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts_names}. "
            f"Spacecraft: {last_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


# print(get_last_completed_mission())


def get_most_used_spacecraft():
    top_spacecraft = (Spacecraft.objects.annotate(missions_number=Count("spacecraft_missions"))
                      .order_by("-missions_number", "name").first())

    if not top_spacecraft or top_spacecraft.missions_number == 0:
        return "No data."

    all_missions = top_spacecraft.spacecraft_missions.all()
    astronauts_participated = []
    for mission in all_missions:
        for astronaut in mission.astronauts.all():
            if astronaut not in astronauts_participated:
                astronauts_participated.append(astronaut)

    num_astronauts = len(astronauts_participated)

    return (f"The most used spacecraft is: {top_spacecraft.name}, "
            f"manufactured by {top_spacecraft.manufacturer}, "
            f"used in {top_spacecraft.missions_number} missions, "
            f"astronauts on missions: {num_astronauts}.")


# print(get_most_used_spacecraft())


def decrease_spacecrafts_weight():
    spacecrafts_to_update = Spacecraft.objects.filter(spacecraft_missions__status="Planned", weight__gte=200).distinct()

    count_updated_weights = spacecrafts_to_update.count()
    if count_updated_weights == 0:
        return "No changes in weight."

    for spacecraft in spacecrafts_to_update:
        spacecraft.weight = max(0.0, spacecraft.weight - 200.0)
        spacecraft.save()

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg("weight"))["avg_weight"]
    # avg_weight = f"{avg_weight:.1f}" if avg_weight is not None else "0.0"

    return (f"The weight of {count_updated_weights} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")


# print(decrease_spacecrafts_weight())
