import json
from tmdb.utils import get_tmdb_session


def get_providers_for_movie(movie_id: int):
    session = get_tmdb_session()

    url_movie_providers = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"

    response = session.get(url_movie_providers)

    data = json.loads(response.content)

    result_fr = data["results"]["FR"]

    liste_providers = []
    if "flatrate" in result_fr.keys():
        result_flatrate = result_fr["flatrate"]
        for provider in result_flatrate:
            liste_providers.append(provider["provider_name"])

    return liste_providers


def get_providers_for_serie(serie_id: int):
    pass
