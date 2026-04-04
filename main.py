from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from services.github_oauth import (
    get_github_login_url,
    exchange_code_for_token,
    get_user_repos
)

app = FastAPI(title="GitHub OAuth Connector")

# Temporary storage (use DB in real apps)
user_tokens = {}


@app.get("/")
def home():
    return {"message": "GitHub OAuth Connector 🚀"}


# 🔐 Step 1: Redirect user to GitHub
@app.get("/login")
def login():
    url = get_github_login_url()
    return RedirectResponse(url)


# 🔁 Step 2: Callback from GitHub
@app.get("/auth/callback")
def callback(code: str):
    try:
        token = exchange_code_for_token(code)

        # Store token (for demo)
        user_id = "demo_user"
        user_tokens[user_id] = token

        return {"message": "Authentication successful", "token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 📦 Step 3: Use token → Fetch repos
@app.get("/repos")
def fetch_repos():
    user_id = "demo_user"
    token = user_tokens.get(user_id)

    if not token:
        raise HTTPException(status_code=401, detail="User not authenticated")

    try:
        repos = get_user_repos(token)
        return {"repos": repos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))