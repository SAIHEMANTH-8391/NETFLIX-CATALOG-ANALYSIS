"""
Netflix catalog analysis: data checks and summary tables.

Usage:
    pip install pandas
    python analysis.py

Reads netflix_titles.csv from the same folder and prints the tables used in
the README. Also saves each table as a CSV in an "outputs" folder.

Note: this script was written without access to your data file, so run it and
fix any column-name differences. Expected columns: show_id, type, title,
director, cast, country, date_added, release_year, rating, duration,
listed_in, description.
"""

import os
import pandas as pd

DATA_FILE = "netflix_titles.csv"
OUT_DIR = "outputs"

os.makedirs(OUT_DIR, exist_ok=True)
df = pd.read_csv(DATA_FILE)

print(f"Rows: {len(df)}  Columns: {list(df.columns)}\n")


def save(table, name):
    path = os.path.join(OUT_DIR, name)
    table.to_csv(path)
    print(f"(saved {path})\n")


# ---------------------------------------------------------------
# 1. DATA QUALITY: missing values per column (fill the README table)
# ---------------------------------------------------------------
missing = df.isna().sum().to_frame("missing")
missing["pct_missing"] = (missing["missing"] / len(df) * 100).round(1)
print("MISSING VALUES")
print(missing.sort_values("missing", ascending=False))
save(missing, "missing_values.csv")

print("Duplicate titles (same type, title, release_year):",
      df.duplicated(subset=["type", "title", "release_year"]).sum(), "\n")

# ---------------------------------------------------------------
# 2. CONTENT TYPE SHARE
# ---------------------------------------------------------------
type_share = df["type"].value_counts().to_frame("titles")
type_share["pct"] = (type_share["titles"] / len(df) * 100).round(1)
print("CONTENT TYPE")
print(type_share)
save(type_share, "type_share.csv")

# ---------------------------------------------------------------
# 3. RATINGS
# ---------------------------------------------------------------
ratings = df["rating"].fillna("Null").value_counts().to_frame("titles")
ratings["pct"] = (ratings["titles"] / len(df) * 100).round(1)
print("RATINGS")
print(ratings)
save(ratings, "ratings.csv")

# ---------------------------------------------------------------
# 4. GENRES: split the combined 'listed_in' field into single genres
#    (the Tableau "Top 10 genre" chart shows combinations, not genres)
# ---------------------------------------------------------------
genres = (
    df.assign(genre=df["listed_in"].fillna("Unknown").str.split(","))
      .explode("genre")
)
genres["genre"] = genres["genre"].str.strip()
genre_counts = genres["genre"].value_counts().head(10).to_frame("titles")
genre_counts["pct_of_titles"] = (genre_counts["titles"] / len(df) * 100).round(1)
print("TOP 10 INDIVIDUAL GENRES (a title can have several genres)")
print(genre_counts)
save(genre_counts, "top_genres.csv")

# ---------------------------------------------------------------
# 5. COUNTRIES: split multi-country titles
# ---------------------------------------------------------------
countries = (
    df.assign(country=df["country"].fillna("Unknown").str.split(","))
      .explode("country")
)
countries["country"] = countries["country"].str.strip()
country_counts = countries["country"].value_counts().head(10).to_frame("titles")
country_counts["pct_of_titles"] = (country_counts["titles"] / len(df) * 100).round(1)
print("TOP 10 COUNTRIES (a title can list several countries)")
print(country_counts)
save(country_counts, "top_countries.csv")

# ---------------------------------------------------------------
# 6. TITLES BY RELEASE YEAR AND TYPE
# ---------------------------------------------------------------
by_year = (
    df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
)
print("TITLES BY RELEASE YEAR (last 15 years in the data)")
print(by_year.tail(15))
save(by_year, "titles_by_release_year.csv")
print("The last year is often incomplete because the data is a snapshot.\n")

# ---------------------------------------------------------------
# 7. RELEASE LAG: years between release and being added to Netflix
# ---------------------------------------------------------------
df["date_added_parsed"] = pd.to_datetime(
    df["date_added"].astype("string").str.strip(), errors="coerce"
)
df["year_added"] = df["date_added_parsed"].dt.year
df["release_lag_years"] = df["year_added"] - df["release_year"]

lag = df["release_lag_years"].dropna()
lag = lag[lag >= 0]  # ignore bad rows where added is before release
print("RELEASE LAG (years from release to being added)")
print(lag.describe().round(2))
print("Median lag (years):", lag.median(), "\n")
lag_by_type = df[df["release_lag_years"] >= 0].groupby("type")["release_lag_years"].median()
print("Median lag by type:")
print(lag_by_type)
save(lag_by_type.to_frame("median_lag_years"), "release_lag_by_type.csv")

print("Latest date_added in the file:", df["date_added_parsed"].max())
