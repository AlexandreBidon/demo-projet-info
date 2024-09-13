from fastapi import Body, FastAPI
import os
from dotenv import load_dotenv
import requests
import json
from pydantic import BaseModel, Field

load_dotenv()

cle_api = os.environ.get("API_KEY")


app = FastAPI()


@app.get("/rechercher_film/{name}")
async def get_providers_for_movie_api(name):
    return get_providers_for_movie(movie_name=name)


class User(BaseModel):
    name: str
    password: str


@app.post("/create_user")
async def update_item(user: User):
    return user

def get_providers_for_movie(movie_name: str):
    url_search_movie = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {cle_api}"
    }
    response = requests.get(url_search_movie, headers=headers)

    data = json.loads(response.content)
    premier_resultat = data["results"][0]
    movie_id = premier_resultat["id"]

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
