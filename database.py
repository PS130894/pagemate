import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///books.db")

df = pd.read_csv("goodreads_data.csv")

# Clean up column names
df.columns = df.columns.str.strip()

# Drop the unnamed column
df = df.drop(columns=["Unnamed: 0"])

# Load into database
df.to_sql("books", engine, if_exists="replace", index=False)

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM books"))
    print(f"Total books in database: {result.fetchone()[0]}")

print("Database created successfully!")
