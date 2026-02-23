import pandas as pd
from sqlalchemy import create_engine, text

def setup_database():
    engine = create_engine("sqlite:///books.db")
    df = pd.read_csv("goodreads_data.csv")
    df.columns = df.columns.str.strip()
    df = df.drop(columns=["Unnamed: 0"])
    df.to_sql("books", engine, if_exists="replace", index=False)
    print("Database created successfully!")
