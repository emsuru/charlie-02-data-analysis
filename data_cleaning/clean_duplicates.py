# Cleaning Phase 1: DUPLICATES
import pandas as pd


def inspect_dataset(df):
    print("Number of observations (rows):", df.shape[0])
    print("Number of features (columns):", df.shape[1])
    print("Number of duplicated rows:", df.duplicated().sum())
    print("Column names:", df.columns)
    print("Data types:", df.dtypes)
    print("Missing values:", df.isnull().sum())
    print("Unique values:", df.nunique())
    print("Descriptive statistics:", df.describe())
    print("First 5 rows:", df.head())
    print("Last 5 rows:", df.tail())

def remove_duplicates(df):
    df_cleaned = df.drop_duplicates(keep='first')
    print("Number of observations (rows):", df_cleaned.shape[0])
    print("Number of features (columns):", df_cleaned.shape[1])
    df_cleaned.to_csv('data/cleaned/cleaned_duplicates.csv', index=False)
    return df_cleaned


# Load raw dataset: Charlie or Bear
df = pd.read_csv('data/raw/rawdata.csv')
# Load test dataset: Bear
df_bear = pd.read_csv('data/raw/bear_rawdata.csv')

# Raw Charlie vs Bear dataset stats:
# 12,388 rows vs 72,986 rows
# 43 columns vs 32 columns
# 3628 duplicated rows vs 11 duplicated rows
