import pandas as pd
from data_cleaning.clean_duplicates import inspect_dataset

# Load the working dataset
df = pd.read_csv('data/cleaned/bear_cleaned_extracols.csv')

inspect_dataset(df)

# How many rows and columns are in the dataset?
# print("Number of observations (rows):", df.shape[0])
# print("Number of features (columns):", df.shape[1])

# Display data types of each column so I know what to include below for quantitative and qualitative variables
# print(df.dtypes)

# Count of quantitative variables (represented by int64 or float64)
quantitative_vars_count = df.select_dtypes(include=['int64', 'float64']).shape[1] # 21 quantitative variables
print("Number of quantitative variables:", quantitative_vars_count)

# Count of qualitative variables (represented by object or category)
qualitative_vars_count = df.select_dtypes(include=['object', 'category']).shape[1] # 17 qualitative variables
print("Number of qualitative variables:", qualitative_vars_count)

# Count of Boolean variables
boolean_vars_count = df.select_dtypes(include=['bool']).shape[1] # 5 Boolean variables
print("Number of Boolean variables:", boolean_vars_count)
