import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

cle_api = os.environ.get("API_KEY")


def get_providers_for_movie(movie_name: str):
    url_search_movie = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {cle_api}"
    }
    response = requests.get(url_search_movie, headers=headers)

    data = json.loads(response.content)
    premier_resultat = data["results"][0]
    print("film: " + premier_resultat["original_title"])
    movie_id = premier_resultat["id"]

    url_movie_providers = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"

    response = requests.get(url_movie_providers, headers=headers)

    data = json.loads(response.content)

    result_fr = data["results"]["FR"]

    if "flatrate" in result_fr.keys():
        print("--- Plateforme ---")
        result_flatrate = result_fr["flatrate"]
        for provider in result_flatrate:
            print(provider["provider_name"])
    else:
        print("pas dispo en streaming")


get_providers_for_movie("the batman")
