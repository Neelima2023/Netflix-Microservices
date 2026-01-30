import os
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Movies Service (Netflix)")

INSTANCE_ID = os.getenv("INSTANCE_ID", "movies-1")

MOVIES = [
    {"id": 1, "title": "Extraction", "year": 2020, "genre": "Action", "rating": 6.7},
    {"id": 2, "title": "The Irishman", "year": 2019, "genre": "Crime", "rating": 7.8},
    {"id": 3, "title": "Marriage Story", "year": 2019, "genre": "Drama", "rating": 7.9},
    {"id": 4, "title": "Bird Box", "year": 2018, "genre": "Thriller", "rating": 6.6},
]

@app.get("/health")
def health():
    return {"status": "ok", "instance": INSTANCE_ID}

@app.get("/movies")
def list_movies(q: str | None = None, min_year: int | None = None):
    results = MOVIES

    if q:
        q_lower = q.lower()
        results = [m for m in results if q_lower in m["title"].lower()]

    if min_year:
        results = [m for m in results if m["year"] >= min_year]

    return {"instance": INSTANCE_ID, "count": len(results), "movies": results}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for m in MOVIES:
        if m["id"] == movie_id:
            return {"instance": INSTANCE_ID, "movie": m}
    raise HTTPException(status_code=404, detail="Movie not found")
