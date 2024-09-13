from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/rechercher_film/{recherche}")
async def rechercher_film(recherche):
    return get_providers_for_movie(movie_name=name)

