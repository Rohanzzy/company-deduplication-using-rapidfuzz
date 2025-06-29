# Company Deduplication Tool

This project is a simple Streamlit app that helps identify duplicate company names in any list. It uses data cleaning and fuzzy matching to find companies that are written slightly differently but are essentially the same.

## Problem Statement

When working with outbound lead lists, enrichment data, or scraped company databases, duplicates often slip in due to minor differences in spelling, formatting, or naming conventions (for example, “Amazon”, “Amazon Inc”, and “amazon.com”).

Manually cleaning these lists is time-consuming and error-prone. This tool automates that process by:

- Cleaning company names to a standard format internally
- Using fuzzy matching to find potential duplicates based on similarity scores
- Allowing users to download a clean list for further use

---

## How It Works

1. **Upload your CSV file**  
   The CSV should contain at least one column for company names. It can have any number of other columns.

2. **Select the company name column**  
   The app asks you to choose which column contains the company names.

3. **Internal cleaning**  
   The app cleans the names by:
   - Lowercasing all text
   - Removing special characters and punctuations
   - Removing common suffixes like “Inc”, “LLC”, “Ltd”, “AI” at the end
   - Replacing long forms like “Technologies” or “Technology” with “Tech”

4. **Fuzzy matching**  
   The cleaned names are compared using fuzzy string matching to find potential duplicates with a similarity score above 85%.

5. **Output**  
   - Displays a table of duplicate pairs with their similarity score
   - Lets you download the duplicates CSV for further cleaning or deduplication in your workflow

---

## Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit app code |
| `requirements.txt` | List of packages to run the app |
| `README.md` | Project description file |

---

## Why This Matters

Data cleaning is one of the most important parts of a data scientist’s job. This project demonstrates my ability to:

- Build and deploy a user-facing tool
- Write scalable and clean code
- Apply practical data cleaning and fuzzy matching to real-world GTM problems

---


---

## Deployment

I’ve also deployed this project on Streamlit Cloud for easy access.
https://company-deduplication-using-rapidfuzz.streamlit.app/

---

## About Me

I’m Rohan Pathak. Currently Head of Growth at Persana AI, I work on building outbound workflows and GTM strategies. I’m learning data science to combine my growth experience with data-driven product and pipeline optimization.

- **LinkedIn:** https://www.linkedin.com/in/pathakrohan/
- **GitHub:** https://github.com/Rohanzzy

Feel free to connect if you’re working on problems around outbound data, lead scoring, or sales automation.



