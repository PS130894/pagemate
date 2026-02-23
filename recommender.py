import os
from groq import Groq
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
engine = create_engine("sqlite:///books.db")

def get_filtered_books(min_rating=4.0, max_pages=None, author=None, genre=None):
    query = "SELECT Book, Author, Avg_Rating, Genres, Description, URL FROM books WHERE 1=1"

    if author:
        query += f" AND Author LIKE '%{author}%'"
    if min_rating:
        query += f" AND CAST(Avg_Rating AS FLOAT) >= {min_rating}"
    if genre:
        query += f" AND Genres LIKE '%{genre}%'"

    query += " GROUP BY Author LIMIT 10"

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()

def recommend_books(preference, min_rating=4.0, max_pages=None, author=None, genre=None):
    books = get_filtered_books(min_rating, max_pages, author, genre)

    books_text = "\n".join([
        f"- {b[0]} by {b[1]} (Rating: {b[2]}, Genres: {b[3]})\n  Description: {b[4][:150]}\n  URL: {b[5]}"
        for b in books
    ])

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": """You are Pagemate, a warm and knowledgeable book recommendation assistant.
                Recommend exactly 3 books from the list provided.
                IMPORTANT: If the user mentions a book they have already read, do NOT recommend that book or any other book in the same series.
                IMPORTANT: Never recommend the same book or different editions more than once. All 3 must be different books by different authors.
                CRITICAL: You must ONLY recommend books from the list provided. Do not use your own knowledge.
                Only recommend books that are clearly a good match. Skip non-fiction, poetry collections, or bibliographies unless the user asks for them.

                Format each recommendation EXACTLY like this with no deviation:

                BOOK_START
                Title: [book title]
                Author: [author name]
                Rating: [rating]
                URL: [url]
                Reason: [2 sentence explanation]
                BOOK_END"""},
            {"role": "user", "content": f"Here are available books:\n{books_text}\n\nUser preference: {preference}\n\nRecommend the 3 best matches."}
        ]
    )

    return response.choices[0].message.content
