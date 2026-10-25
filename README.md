# NETFLIX-CATALOG-ANALYSIS

<img width="960" alt="Logos-Readability-Netflix-logo" src="https://github.com/user-attachments/assets/caaf810c-a0cc-41c9-8f25-c63584d8dae1" />

![BrandAssets_Logos_02-NSymbol](https://github.com/user-attachments/assets/e63f7ead-ab00-4922-a275-027852db58b9)


An interactive Tableau dashboard and supporting analysis of **6,234 titles** in the Netflix catalog, showing how the catalog splits between movies and TV shows, which ratings and genres dominate, and how many titles were released each year.

![Dashboard](Dashboard%201.png)

## Business question

> How is the Netflix catalog made up (content type, ratings, genres, countries) and how has it changed over time, and what does that suggest a content or catalog analyst should look at next?

This is a **catalog composition** analysis. It describes what is in the library, not what people watch (see "What this data can and cannot answer").

## Dataset

- **Source:** Netflix titles dataset on Kaggle (`netflix_titles.csv`, included in this repo).
- **Size:** 6,234 titles (4,265 movies and 1,969 TV shows)
- **Key columns:** type, title, director, cast, country, date_added, release_year, rating, duration, listed_in (genres), description.


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

### What I found

1. About two-thirds of the catalog is movies. 4,265 of the 6,234 titles are movies (68.4%) and 1,969 are TV shows (31.6%).

2. The catalog leans toward mature content. TV-MA (2,027 titles) and TV-14 (1,698) together make up almost 60% of everything. Kids and family ratings (TV-Y7, TV-G, TV-Y, and G) add up to just 498 titles, about 8%.

3. International content is a big part of the library. "International Movies" is the single most common genre, with 1,927 titles (30.9%), followed by Dramas (1,623) and Comedies (1,113). Counting International Movies and International TV Shows together, about 47% of titles carry an international tag.

4. My own genre chart was misleading, and I fixed it. My first dashboard showed Documentaries as the top genre. That was wrong in a subtle way: the chart counted whole genre strings like "Dramas, International Movies" as one item, so titles with several genres were being split up. Once I separated the genres properly, Documentaries dropped to fifth place (668 titles, 10.7%), and International Movies, Dramas, Comedies, and International TV Shows moved ahead of it.

5. The United States and India dominate by country. The US appears on 2,610 titles (41.9%), India on 838 (13.4%), and the UK on 602 (9.7%). Titles can list more than one country, so these percentages don't add up to 100%. Another 476 titles (7.6%) have no country at all.

6. TV shows are growing faster than movies. Comparing titles released in 2008 and 2018, movies went from 87 to 646 (roughly 7 times more), while TV shows went from 20 to 417 (roughly 21 times more). In 2019, TV show releases (443) overtook movie releases (400).

7. Most titles arrive on Netflix quickly. The typical title is added about 1 year after it was released, and a quarter are added in the same year. The average is higher (4.6 years) because a small number of very old titles, some up to 93 years old, pull it up, so I used the median.

### What I would look at next

These are questions the data raised, not conclusions about Netflix's strategy:

1. Is the balance really shifting toward TV shows? I would track the share of TV by year.
2. Is the library thin for younger viewers? Only about 8% of titles have a kids or family rating, but I would need viewing data to say whether that matters.
3. Is international content growing as a share of the catalog? I would track country share over time.
4. How much does the catalog rely on brand new releases, given that the typical title arrives within a year?

## Takeaways for a catalog analyst

These are questions the data points to, not conclusions about Netflix's strategy:

- **Mix:** with about 68% movies, is the catalog balanced for viewers who prefer series? Compare against viewing data, if available.
- **Audience:** with under 10% of titles carrying family and kids ratings, is the library under-serving younger viewers? Check this against account types.
- **International content:** half of the top genre combinations include international titles, so tracking country share over time is a natural next analysis.

## Limitations

- **Catalog, not viewership.** The data cannot show what is watched. Any statement about popularity needs a different dataset.
- **Snapshot data.** The sharp drop in titles at the right edge of the "by year" chart reflects the dataset ending, not a real fall in content. Recent years   are incomplete.
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
