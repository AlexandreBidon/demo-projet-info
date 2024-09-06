import os
from dotenv import load_dotenv
import requests

load_dotenv()

cle_api = os.environ.get("API_KEY")

movie_name = "batman"
url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {cle_api}"
}

response = requests.get(url, headers=headers)

print(response.text)
