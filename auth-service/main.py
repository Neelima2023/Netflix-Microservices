import os
import time
import jwt
from fastapi import FastAPI, HTTPException, Header

app = FastAPI(title="Auth Service (JWT)")

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_ALG = "HS256"

USERS = {
    "admin": "admin123",
    "user": "user123",
}

def create_token(username: str) -> str:
    now = int(time.time())
    payload = {"sub": username, "iat": now, "exp": now + 3600}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def verify_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login(body: dict):
    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="username and password required")

    if USERS.get(username) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(username)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/verify")
def verify(authorization: str | None = Header(default=None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")

    token = authorization.split(" ", 1)[1].strip()
    decoded = verify_token(token)
    return {"ok": True, "user": decoded.get("sub")}
