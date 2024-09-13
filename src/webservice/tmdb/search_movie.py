import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

cle_api = os.environ.get("API_KEY")


def get_movie_by_id(movie_id: int):
    """
    On cherche un film par son id et on retourne une liste d'information sur ce film.
    Si l'id n'est pas bon, la fonction retourne une erreur.
    """
    url_search_movie = f"https://api.themoviedb.org/3/movie/{str(movie_id)}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {cle_api}"
    }
    response = requests.get(url_search_movie, headers=headers)
    if response.status_code == 200:
        content = json.loads(response.content)
        result = {
            "name": content["original_title"],
            "description": content["overview"]
        }
        return result
    else:
        raise Exception("Le film n'a pas été trouvé (pas le bon id).")
