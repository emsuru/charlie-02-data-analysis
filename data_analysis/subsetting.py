import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# from data_cleaning.clean_duplicates import inspect_dataset

# Load the working dataset
# Assuming your DataFrame is named df
# And assuming the column for overall price is named 'Price'
# And the column for habitable surface area is named 'HabitableSurfaceArea'

# Replace zeros in 'HabitableSurfaceArea' with NaN to avoid division by zero
df['HabitableSurfaceArea'] = df['HabitableSurfaceArea'].replace(0, np.nan)

# Create the new column 'PricePerSqm' with a condition to avoid division by zero
df['PricePerSqm'] = np.where(df['HabitableSurfaceArea'] > 0, df['Price'] / df['HabitableSurfaceArea'], np.nan)

# Now df includes the new column 'PricePerSqm' with the computed values
# Entries with zero 'HabitableSurfaceArea' will have 'PricePerSqm' as NaN
df = pd.read_csv('data/cleaned/bear_cleaned_extracols.csv')

print(df.shape)

def price_per_sqm(df):
   ['PricePerSqm'] = np.where(df['HabitableSurfaceArea'] > 0, df['Price'] / df['HabitableSurfaceArea'], np.nan)
   df['HabitableSurfaceArea'] = df['HabitableSurfaceArea'].replace(0, np.nan) # Replace zeros in 'HabitableSurfaceArea' with NaN to avoid division by zero
   df['PricePerSqm'] = df['Price'] / df['HabitableSurfaceArea'] # Create the new column 'PricePerSqm' with a condition to avoid division by zerodf
  pass

print(df.head)
