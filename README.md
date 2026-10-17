# Gurgaon Real Estate Market Analysis

Exploratory Data Analysis (EDA) of residential property listings in Gurgaon, answering business questions on pricing, localities, builders and property types.

Problem statement and dataset are from a project brief; the analysis code is written by me.

## Tools
Python, Pandas, Matplotlib, Seaborn

## Business Questions
1. Which is the costliest flat in the dataset?
2. Which locality has the highest average price?
3. Which locality has the highest rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does area (sqft) impact property price?
7. Which BHK configuration is the most expensive on average?
8. Which property type (Apartment, Floor, Plot) is the costliest?
9. Do certain builders or companies consistently price higher?
10. Are larger homes always more expensive per square foot?

## Key Findings
- Dataset has 19,515 listings; 14,223 remain after removing duplicates
- Costliest property: a 6 BHK apartment in DLF Camellias (Sector 42), priced at ₹122.63 crore (16,500 sqft)
- Highest average price: Baliawas (about ₹58.3 crore), followed by Sector 42 (about ₹50.2 crore)
- Highest average rate per sqft: Sector 42
- Ready-to-move properties have a higher average price than under-construction ones
- Non-RERA-approved properties have a higher average price than RERA-approved ones (based on averages, so very high-priced listings may influence this)
- Area vs price and area vs rate per sqft are visualised with scatter plots in `main.py`
- Highest average rate per sqft by BHK count: 114 BHK, which looks like a data entry error rather than a real configuration
- Highest average rate per sqft by property type: villa
- Top 5 companies by average rate per sqft: Camelliaass (about 44,724), Cameliaas (about 40,000), Tulip (about 28,571), Prom (about 27,359), Magnoliaass (about 26,666)
- The highest rate per sqft values belong to small areas (208, 204, 263, 173 and 267 sqft), so larger homes are not always more expensive per sqft

## Limitations
- Averages are used, so a few extreme values can influence results
- BHK and property type comparisons use average rate per sqft, not total price
- Some entries look unreliable: 114 BHK, homes of about 200 sqft with very high rates, and company names with spelling variants

## Files
- `main.py` - data cleaning and analysis code
- `data.csv` - dataset of residential listings

## Data
Source: [Gurgaon Real Estate Dataset on Kaggle](https://www.kaggle.com/datasets/nikhilmehrahr26/gurgaon-real-estate-dataset)

## How to Run
1. Install the libraries: `pip install pandas matplotlib seaborn`
2. Keep `data.csv` in the same folder as `main.py`
3. Run `python main.py`