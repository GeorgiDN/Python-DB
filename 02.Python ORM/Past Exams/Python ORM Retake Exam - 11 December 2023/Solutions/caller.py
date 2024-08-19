import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.db.models import Count, Q
from main_app.models import TennisPlayer, Tournament, Match


# # 4.
def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ""

    if search_name is not None and search_country is not None:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)
    elif search_name is not None and search_country is None:
        query = Q(full_name__icontains=search_name)
    else:
        query = Q(country__icontains=search_country)

    tennis_players = TennisPlayer.objects.filter(query).order_by("ranking")

    result = []
    for player in tennis_players:
        result.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

    return "\n".join(result)


# print(get_tennis_players(search_country="bg"))


def get_top_tennis_player():
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.wins_count} wins."


# print(get_top_tennis_player())


def get_tennis_player_by_matches_count():
    top_player = (TennisPlayer.objects.
                  annotate(matches_count=Count("players_matches"))
                  .filter(matches_count__gt=0)
                  .order_by("-matches_count", "ranking")).first()

    if not top_player:
        return ""

    return f"Tennis Player: {top_player.full_name} with {top_player.matches_count} matches played."


# print(get_tennis_player_by_matches_count())


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(Q(surface_type__icontains=surface)).order_by("-start_date")
    if not tournaments:
        return ""

    result = []
    for tournament in tournaments:
        num_matches = tournament.tournament_matches.count()
        result.append(f"Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {num_matches}")

    return "\n".join(result)


# print(get_tournaments_by_surface_type("clay"))


def get_latest_match_info():
    latest_match = Match.objects.order_by("-date_played", "id").first()
    if not latest_match:
        return ""

    all_players = " vs ".join(p.full_name for p in latest_match.players.all().order_by("full_name"))
    winner = latest_match.winner.full_name if latest_match.winner else "TBA"

    return (f"Latest match played on: {latest_match.date_played}, "
            f"tournament: {latest_match.tournament.name}, "
            f"score: {latest_match.score}, "
            f"players: {all_players}, "
            f"winner: {winner}, "
            f"summary: {latest_match.summary}")


# print(get_latest_match_info())


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    found_matches = Match.objects.filter(tournament__name__exact=tournament_name).order_by("-date_played")
    if not found_matches:
        return "No matches found."

    result = []
    for match in found_matches:
        winner = match.winner.full_name if match.winner else "TBA"
        result.append(f"Match played on: {match.date_played}, score: {match.score}, winner: {winner}")

    return "\n".join(result)


# print(get_matches_by_tournament("tournament1"))
