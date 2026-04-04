import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI")

GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_API_URL = "https://api.github.com"


def get_github_login_url():
    return f"{GITHUB_AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=repo"


def exchange_code_for_token(code: str):
    response = requests.post(
        GITHUB_TOKEN_URL,
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI
        },
    )
    response.raise_for_status()
    return response.json().get("access_token")


def get_user_repos(token: str):
    response = requests.get(
        f"{GITHUB_API_URL}/user/repos",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        },
    )
    response.raise_for_status()
    return response.json()