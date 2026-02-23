import pandas as pd

df = pd.read_csv("goodreads_data.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst row:")
print(df.head(1))
