# 🚀 GitHub OAuth Connector (FastAPI + Docker)

A simple cloud connector built using **FastAPI** that integrates with GitHub using **OAuth 2.0**, allowing users to authenticate and perform API actions like fetching repositories.

---

## 🔥 Features

* 🔐 GitHub OAuth 2.0 Authentication
* 📦 Fetch authenticated user repositories
* ⚡ FastAPI backend with clean architecture
* 🐳 Dockerized for easy deployment
* ☁️ Ready for cloud deployment (AWS / Render)

---

## 🧱 Project Structure

```
github-connector/
│── main.py
│── services/
│   └── github_oauth.py
│── requirements.txt
│── Dockerfile
│── .env (not committed)
```

---

## ⚙️ Prerequisites

* Python 3.8+
* Git
* Docker (optional)
* GitHub account

---

## 🔑 Setup GitHub OAuth App

1. Go to GitHub Developer Settings

2. Create a new OAuth App

3. Set:

   * **Homepage URL** → `http://localhost:8000`
   * **Authorization Callback URL** →
     `http://localhost:8000/auth/callback`

4. Copy:

   * Client ID
   * Client Secret

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
GITHUB_REDIRECT_URI=http://localhost:8000/auth/callback
```

---

## ▶️ Run Locally (Without Docker)

### 1. Create Virtual Environment

```
python -m venv venv
```

### 2. Activate

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Server

```
uvicorn main:app --reload
```

---

## 🌐 Usage

### 1. Start OAuth Login

Open:

```
http://localhost:8000/login
```

### 2. Authorize via GitHub

### 3. Fetch Repositories

```
GET /repos
```

---

## 🐳 Run with Docker

### 1. Build Image

```
docker build -t github-connector .
```

### 2. Run Container

```
docker run -d -p 8000:8000 \
-e GITHUB_CLIENT_ID=your_client_id \
-e GITHUB_CLIENT_SECRET=your_client_secret \
-e GITHUB_REDIRECT_URI=http://localhost:8000/auth/callback \
github-connector
```

---

## 📌 Tech Stack

* FastAPI
* Python
* GitHub REST API
* OAuth 2.0
* Docker

---

## 🙌 Author

Harshit Ruprela

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
