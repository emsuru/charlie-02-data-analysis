# Cleaning Phase 1: DUPLICATES
import pandas as pd

# Load the raw dataset
df = pd.read_csv('data/raw/rawdata.csv')

# How many rows and columns are in the dataset?
print("Number of observations (rows):", df.shape[0]) #12,388 rows
print("Number of features (columns):", df.shape[1]) # 43 columns


# Check if there are duplicates
print(df.duplicated().sum()) # there are 3628 duplicated rows in the raw dataset

# Identify the duplicated rows & print them
duplicates = df[df.duplicated(keep=False)]
print(duplicates)

# # Remove duplicates, keeping the first occurrence
# df_cleaned = df.drop_duplicates(keep='first')

# # Save the cleaned DataFrame to a new CSV file
# df_cleaned.to_csv('data/cleaned/cleaned_duplicates.csv', index=False)
