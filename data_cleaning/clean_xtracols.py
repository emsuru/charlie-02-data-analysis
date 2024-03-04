import pandas as pd
import numpy as np

# Load the working dataset
df = pd.read_csv('data/cleaned/bear_cleaned_missing_vals.csv')

# How many rows and columns are in the dataset?
print("Number of observations (rows):", df.shape[0])
print("Number of features (columns):", df.shape[1])

## Remove custom columns from the data set (whatever is found irrelevant to the analysis)
def drop_custom_cols(df):
    df_cleaned_cols = df.drop(columns=['Property url', 'SaleType', 'Latitude', 'Longitude', 'ID', 'HouseNumber', 'Street'])
    # Save the cleaned DataFrame to a new CSV file
    df_cleaned_cols.to_csv('data/cleaned/bear_cleaned_extracols.csv', index=False)
    print("Shape of DataFrame after removing irrelevant columns:", df_cleaned_cols.shape)
    print("Columns that remained after removing irrelevant columns:", df_cleaned_cols.columns)

drop_custom_cols(df)
