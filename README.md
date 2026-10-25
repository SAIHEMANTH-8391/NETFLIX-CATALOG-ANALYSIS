# NETFLIX-CATALOG-ANALYSIS

<img width="960" alt="Logos-Readability-Netflix-logo" src="https://github.com/user-attachments/assets/caaf810c-a0cc-41c9-8f25-c63584d8dae1" />

![BrandAssets_Logos_02-NSymbol](https://github.com/user-attachments/assets/e63f7ead-ab00-4922-a275-027852db58b9)

# Netflix Catalog Analysis (Tableau, Excel, Python)

An interactive Tableau dashboard and supporting analysis of **6,234 titles** in the Netflix catalog, showing how the catalog splits between movies and TV shows, which ratings and genres dominate, and how many titles were released each year.

![Dashboard](Dashboard%201.png)

## Business question

> How is the Netflix catalog made up (content type, ratings, genres, countries) and how has it changed over time, and what does that suggest a content or catalog analyst should look at next?

This is a **catalog composition** analysis. It describes what is in the library, not what people watch (see "What this data can and cannot answer").

## Dataset

- **Source:** Netflix titles dataset on Kaggle (`netflix_titles.csv`, included in this repo). Link: [add the Kaggle dataset URL you used]
- **Size:** 6,234 titles (4,265 movies and 1,969 TV shows)
- **Key columns:** type, title, director, cast, country, date_added, release_year, rating, duration, listed_in (genres), description.
  The messy parts of the data
What I checked	What I found	What I did
Director	Missing for 1,969 titles (31.6%)	Left it out of anything involving directors
Cast	Missing for 570 titles (9.1%)	Left it out of anything involving cast
Country	Missing for 476 titles (7.6%)	Counted them as "Unknown"
Date added	Missing for 11 titles	Left them out of the release lag calculation
Rating	Missing for 10 titles	Kept them as "Null" instead of guessing
Duplicates	3 titles repeated	[say what you decided after checking them]

One thing I noticed: the 1,969 missing directors is exactly the same as the number of TV shows. That probably isn't a coincidence. [After checking in Excel, say whether most of the missing directors are TV shows. If so, director is rarely filled in for TV rather than randomly missing.]

What I found

## What this data can and cannot answer

| It can answer | It cannot answer |
|---|---|
| What mix of movies and TV shows is in the catalog | Which titles are most watched (there is no viewership data) |
| Which ratings, genres, and countries appear most | Which titles are popular, profitable, or well reviewed |
| How many titles were released per year | Why Netflix chose to add a title |

## Tools

- **Tableau:** dashboard (`Book1.twbx`)
- **Excel:** initial inspection and cleaning checks
- **Python (pandas):** missing-value check, genre splitting, and summary tables (`analysis.py`)

## Method

1. Collected the public Netflix titles dataset.
2. Inspected the data and counted missing values in each column (see the table below).
3. Cleaned and standardized fields (dates, genre text, country text).
4. Built the dashboard in Tableau.
5. Wrote the findings and limits below.

### Data quality

| Column | Missing values | Decision |
|---|---|---|
| director | [count from analysis.py] | Kept; flagged as "Unknown" in director views |
| cast | [count] | Kept; excluded from cast-based views |
| country | [count] | Kept; excluded from the country map |
| date_added | [count] | Excluded from "added by year" views only |
| rating | 10 shown as Null in the ratings chart | Kept and displayed as Null, not guessed |

Run `analysis.py` to fill in the counts above.

## Key findings

1. **The catalog is about two-thirds movies.** Of 6,234 titles, 4,265 are movies (68.4%) and 1,969 are TV shows (31.6%).
2. **The catalog skews toward mature content.** TV-MA (2,027 titles, 32.5%) and TV-14 (1,698, 27.2%) together make up 59.8% of all titles. Family and kids ratings are small by comparison: TV-Y7, TV-G, TV-Y, and G add up to 498 titles (8.0%).
3. **Documentaries and stand-up comedy lead the genre combinations.** Documentaries (299) and Stand-Up Comedy (273) are the two largest genre combinations, followed by Dramas and International Movies (248). The top 10 combinations account for 1,858 titles (29.8%), and 5 of those 10 include "International Movies".
4. **Catalog growth is recent.** The number of titles per release year stays low until the early 2000s, then rises steeply through the late 2010s, and TV shows start rising later than movies. [Add exact figures: titles released in 2008 vs 2018, from Tableau or `analysis.py`.]
5. **Country concentration.** [Add the top 5 countries and their share of titles, from `analysis.py`.]
6. **Release lag.** [Add the median gap between release year and the year added to Netflix, from `analysis.py`.]

> Note on finding 3: the "Top 10 genre" chart shows genre **combinations** (the `listed_in` field as written, for example "Dramas, International Movies"). Splitting the field into individual genres, which `analysis.py` does, gives the true count per genre.

## Takeaways for a catalog analyst

These are questions the data points to, not conclusions about Netflix's strategy:

- **Mix:** with about 68% movies, is the catalog balanced for viewers who prefer series? Compare against viewing data, if available.
- **Audience:** with under 10% of titles carrying family and kids ratings, is the library under-serving younger viewers? Check this against account types.
- **International content:** half of the top genre combinations include international titles, so tracking country share over time is a natural next analysis.

## Limitations

- **Catalog, not viewership.** The data cannot show what is watched. Any statement about popularity needs a different dataset.
- **Snapshot data.** The sharp drop in titles at the right edge of the "by year" chart reflects the dataset ending, not a real fall in content. Recent years are incomplete.
- **Genre combinations.** The genre chart counts combined genre strings, not individual genres.
- **Missing values** in director, cast, and country limit those views.
- **Single source.** One public dataset, with no way to verify its completeness.

## Next steps

- Compare country mix across years.
- Compare content type mix by rating.
- Join with a viewership or ratings dataset (for example, IMDb) to move from catalog to popularity.

## Files

| File | Purpose |
|---|---|
| `Book1.twbx` | Tableau workbook |
| `Dashboard 1.png` | Dashboard screenshot |
| `netflix_titles.csv` | Source data |
| `analysis.py` | Data checks and summary tables |
| `README.md` | This file |

## How to reproduce

1. Download `netflix_titles.csv` (or use the copy in this repo).
2. Run `python analysis.py` in the same folder. It prints the tables above and saves CSVs to an `outputs/` folder.
3. Open `Book1.twbx` in Tableau Public or Tableau Desktop.
