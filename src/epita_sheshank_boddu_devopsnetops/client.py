import requests

from .config import config


def fetch_live_data() -> dict:
    """Fetch the authenticated user's GitHub profile."""
    config.validate()

    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"Bearer {config.api_key}",
        "User-Agent": "Epita-Student-CLI",
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "status": "LIVE_SUCCESS",
        "username": data.get("login"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
    }