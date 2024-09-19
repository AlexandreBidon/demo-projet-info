import requests
import os
from dotenv import load_dotenv

load_dotenv()

cle_api = os.environ.get("API_KEY")


def get_tmdb_session() -> requests.Session:
    """
    Returns a session with credentials
    """
    session = requests.Session()
    session.headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {cle_api}"
    }
    return session