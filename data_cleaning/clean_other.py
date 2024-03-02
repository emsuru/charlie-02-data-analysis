import pandas as pd
import numpy as np

# Load the working dataset
df = pd.read_csv('data/cleaned/bear_cleaned_missing_vals.csv')

# How many rows and columns are in the dataset?
print("Number of observations (rows):", df.shape[0])
print("Number of features (columns):", df.shape[1])

# Print shape of the DataFrame
print(df.head())

# FURTHER CLEANUP
# Remove leading and trailing spaces in string columns
for col in df.select_dtypes(include=['object']).columns:
     df[col] = df[col].str.strip()

# Replace empty strings with NaN
df.replace('', np.nan, inplace=True)



# This code snippet first attempts to clean a hypothetical 'price' column by coercing non-numeric values to NaN, which you can then handle according to your needs
# (e.g., filling with a default value or dropping them). It then iterates over all string-type columns in the DataFrame, removing leading and trailing spaces from each value.
# Remember to adjust the column names and handling of NaN values according to your specific dataset and requirements.

# Example: Cleaning a 'price' column which should only contain numeric values
# Convert non-numeric values to NaN, then you can decide to fill with a value or drop them
# df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Optionally, fill NaN values with a value or drop them
# df['price'].fillna(0, inplace=True)  # Example: fill with 0
# df.dropna(subset=['price'], inplace=True)  # Example: drop rows with NaN in 'price'



# Now, your DataFrame 'df' has cleaned numeric columns and trimmed string columns
