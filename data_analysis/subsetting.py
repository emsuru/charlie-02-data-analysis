import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np
# from data_cleaning.clean_duplicates import inspect_dataset

df = pd.read_csv('data/cleaned/bear_cleaned_extracols.csv')
print(df.shape)

def price_per_sqm(df):
    df['LivingArea'] = df['LivingArea'].replace(0, np.nan) # Replace zeros in 'HabitableSurfaceArea' with NaN to avoid division by zero
    df['PricePerSqm'] = np.where(df['LivingArea'] > 0, df['Price'] / df['LivingArea'], np.nan) # Create the new column 'PricePerSqm' with a condition to avoid division by zero
    return df



# LOGIC FOR OUTLIERS
# 1. Calculate the IQR for each province
# Q1 = df.groupby('Province')['Price'].quantile(0.25)
# Q3 = df.groupby('Province')['Price'].quantile(0.75)
# IQR = Q3 - Q1

# 2. Define a multiplier for the IQR to determine what is considered an outlier
# Typically, this multiplier is 1.5 for a moderate outlier definition
# multiplier = 1.5

# 3. Filter out outliers
# filtered_df = pd.DataFrame()
# for province in df['Province'].unique():
#     province_df = df[df['Province'] == province]
#     province_IQR = IQR[province]
#     lower_bound = Q1[province] - (multiplier * province_IQR)
#     upper_bound = Q3[province] + (multiplier * province_IQR)
#     filtered_province_df = province_df[(province_df['Price'] >= lower_bound) & (province_df['Price'] <= upper_bound)]
#     filtered_df = pd.concat([filtered_df, filtered_province_df], axis=0)

# Create a violin plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Price', y='Province', data=df, cut=0)
plt.title('Price Distribution by Province')
plt.xlabel('Province')
plt.ylabel('Price')
# Set the y-axis to start at 0
# plt.ylim(bottom=0)
# Format the x-axis tick labels to show prices in euros with one decimal place
tick_labels = ['€{:,.1f}M'.format(y / 1e6) for y in plt.yticks()[0]]
plt.yticks(plt.yticks()[0], tick_labels)
plt.show()
# # Create a box plot
# plt.figure(figsize=(12, 8))
# sns.boxplot(x='Province', y='Price', data=df)
# plt.title('Price Distribution by Province (Outliers Removed)')
# plt.xlabel('Province')
# plt.ylabel('Price')
# # Set the y-axis to start at 0
# plt.ylim(bottom=0)
# # Format the y-axis tick labels to show prices in euros with one decimal place
# tick_labels = ['€{:,.1f}M'.format(y / 1e6) for y in plt.yticks()[0]]
# plt.yticks(plt.yticks()[0], tick_labels)

# plt.show()
