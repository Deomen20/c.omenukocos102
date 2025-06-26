import pandas as pd
df = pd.read_csv('Top-Apps-in-Google-Play.csv')

print("First 7 rows of the dataset:")
print(df.head(7))
first_three_columns = df.columns[:3]

print("\nFirst 3 columns of the dataset:")
print(df[first_three_columns])

print("\nHeader and one row of the dataset:")
print(df.head(1))
