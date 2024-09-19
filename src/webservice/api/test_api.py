from fastapi import FastAPI
import requests
import json
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

@app.get("/rechercher_film/{recherche}")
async def rechercher_film(recherche):
    return get_providers_for_movie(movie_name=name)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)