from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from recommender import recommend_books

app = FastAPI()

# This allows our HTML file to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pagemate.netlify.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserPreference(BaseModel):
    preference: str
    last_book: str = None
    mood: str = None
    min_rating: float = 4.0
    author: str = None
    genre: str = None

@app.post("/recommend")
def get_recommendations(data: UserPreference):
    full_preference = f"{data.preference}"
    if data.last_book:
        full_preference += f". The last book I enjoyed was {data.last_book}"
    if data.mood:
        full_preference += f". My current mood is {data.mood}"

    result = recommend_books(full_preference, data.min_rating, None, data.author, data.genre)
    return {"recommendations": result}
