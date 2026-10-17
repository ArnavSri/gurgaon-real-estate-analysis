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

## Files
- `main.py` - data cleaning and analysis code
- `data.csv` - dataset of residential listings

## Data
Source: [Gurgaon Real Estate Dataset on Kaggle](https://www.kaggle.com/datasets/nikhilmehrahr26/gurgaon-real-estate-dataset)

## How to Run
1. Install the libraries: `pip install pandas matplotlib seaborn`
2. Keep `data.csv` in the same folder as `main.py`
3. Run `python main.py`