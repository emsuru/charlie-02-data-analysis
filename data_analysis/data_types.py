import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# from data_cleaning.clean_duplicates import inspect_dataset

# Load the working dataset
df = pd.read_csv('data/cleaned/bear_cleaned_extracols.csv')

# inspect_dataset(df)

def inspect_data_types(df):
    # How many rows and columns are in the dataset?
    print("Number of observations (rows):", df.shape[0])
    print("Number of features (columns):", df.shape[1])

    # Display data types of each column so I know what to include below for quantitative and qualitative variables
    print(df.dtypes)

    # Count of quantitative variables (represented by int64 or float64)
    quantitative_vars_count = df.select_dtypes(include=['int64', 'float64']).shape[1] # 21 quantitative variables
    print("Number of quantitative variables:", quantitative_vars_count)

    # Count of qualitative variables (represented by object or category)
    qualitative_vars_count = df.select_dtypes(include=['object', 'category']).shape[1] # 17 qualitative variables
    print("Number of qualitative variables:", qualitative_vars_count)

    # Count of Boolean variables
    boolean_vars_count = df.select_dtypes(include=['bool']).shape[1] # 5 Boolean variables
    print("Number of Boolean variables:", boolean_vars_count)

# Create a violin plot to compare prices between provinces
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

# Calculate the IQR for each province
Q1 = df.groupby('Province')['Price'].quantile(0.25)
Q3 = df.groupby('Province')['Price'].quantile(0.75)
IQR = Q3 - Q1

# Define a multiplier for the IQR to determine what is considered an outlier
# Typically, this multiplier is 1.5 for a moderate outlier definition
multiplier = 1.5

# Filter out outliers
filtered_df = pd.DataFrame()
for province in df['Province'].unique():
    province_df = df[df['Province'] == province]
    province_IQR = IQR[province]
    lower_bound = Q1[province] - (multiplier * province_IQR)
    upper_bound = Q3[province] + (multiplier * province_IQR)
    filtered_province_df = province_df[(province_df['Price'] >= lower_bound) & (province_df['Price'] <= upper_bound)]
    filtered_df = pd.concat([filtered_df, filtered_province_df], axis=0)

sns.violinplot(y='Price', x='Province', data=filtered_df, cut=0)
plt.title('Price Distribution by Province (Outliers Removed)')
plt.ylabel('Price')
plt.xlabel('Province')

# Set the y-axis to start at 0
plt.ylim(bottom=0)

# Format the y-axis tick labels to show prices in euros with one decimal place
tick_labels = ['€{:,.1f}M'.format(y / 1e6) for y in plt.yticks()[0]]
plt.yticks(plt.yticks()[0], tick_labels)

plt.show()
