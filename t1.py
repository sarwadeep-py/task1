import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df.head()

# missing values
missing=df.isnull().sum()
print("Missing values before cleaning:")
print(missing)

# replacing null values
fill_cols=["director", "cast", "country", "rating", "duration", "listed_in", "description"]
for col in fill_cols:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

# dropping duplicates
duplicates=df.duplicated().sum()
df = df.drop_duplicates()

# standardization
if "rating" in df.columns:
    df["rating"]=df["rating"].str.upper()
    df["rating"]=df["rating"].replace({"UNKNOWN": "Unknown", "UNRATED": "Unrated"})

# converting date format
if "date_added" in df.columns:
    df["date_added"]=pd.to_datetime(df["date_added"], errors="coerce")
    df["date_added"]=df["date_added"].dt.strftime("%d-%m-%Y")
    df["date_added"]=df["date_added"].fillna("")

# changing datatypes
if "show_id" in df.columns:
    df["show_id"]=df["show_id"].astype("string")

# saving cleaned dataset
df.to_csv("netflix_titles_cleaned_only_user_changes.csv", index=False)

print("Duplicates removed:", duplicates)
print("Cleaned dataset saved as netflix_titles_cleaned_only_user_changes.csv")
