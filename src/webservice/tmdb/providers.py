import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

cle_api = os.environ.get("API_KEY")


def get_providers_for_movie(movie_id: int, ):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {cle_api}"
    }

    url_movie_providers = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"

    response = requests.get(url_movie_providers, headers=headers)

    data = json.loads(response.content)

    result_fr = data["results"]["FR"]

    liste_providers = []
    if "flatrate" in result_fr.keys():
        result_flatrate = result_fr["flatrate"]
        for provider in result_flatrate:
            liste_providers.append(provider["provider_name"])

    return liste_providers
