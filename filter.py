from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///books.db")

def get_books(author=None, min_rating=None, max_pages=None):
    query = "SELECT title, authors, average_rating, num_pages FROM books WHERE 1=1"

    if author:
        query += f" AND authors LIKE '%{author}%'"
    if min_rating:
        query += f" AND average_rating >= {min_rating}"
    if max_pages:
        query += f" AND num_pages <= {max_pages}"

    query += " LIMIT 5"

    with engine.connect() as conn:
        result = conn.execute(text(query))
        books = result.fetchall()

    for book in books:
        print(f"Title: {book[0]} | Author: {book[1]} | Rating: {book[2]}")

# Test it
get_books(min_rating=4.5)
