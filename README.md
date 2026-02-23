# Pagemate 📚
Your personal reading companion — an AI-powered book recommendation app.

## What it does
- Tell Pagemate what kind of book you're looking for
- Share the last book you enjoyed
- Pick your mood
- Get 3 personalized recommendations with Goodreads links

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI, Uvicorn
- Database: SQLite, SQLAlchemy
- AI: Groq (Llama 3.3)

## Setup
1. Clone the repo
2. Create a virtual environment and install dependencies
3. Copy `.env.example` to `.env` and add your Groq API key
4. Run `python3 database.py` to set up the database
5. Run `uvicorn api:app --reload` to start the backend
6. Open `index.html` in your browser
