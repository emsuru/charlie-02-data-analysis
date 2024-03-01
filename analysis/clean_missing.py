# Cleaning Phase 2: MISSING VALUES

import pandas as pd

# Load the working dataset
df = pd.read_csv('data/cleaned/cleaned_duplicates.csv')

# How many rows and columns are in the dataset?
print("Number of observations (rows):", df.shape[0]) # 8760 rows
print("Number of features (columns):", df.shape[1]) # 43 columns

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

# Identify columns with more than 50% missing values
columns_to_drop = df.columns[df.isnull().mean() > 0.5]

# Identify columns with more than 50% missing values
columns_to_drop = df.columns[df.isnull().mean() > 0.5]

# Print out these columns and their data types
print("Columns with >50% missing values and their data types:")
for column in columns_to_drop:
    print(f"{column}: {df[column].dtype}")

# # Categorize these columns by their data types
# quantitative_missing = df[columns_to_drop].select_dtypes(include=['int64', 'float64']).columns
# qualitative_missing = df[columns_to_drop].select_dtypes(include=['object', 'category']).columns
# boolean_missing = df[columns_to_drop].select_dtypes(include=['bool']).columns

# # Print out the categorization
# print("\nQuantitative columns with >50% missing values:")
# for column in quantitative_missing:
#     print(column)

# print("\nQualitative columns with >50% missing values:")
# for column in qualitative_missing:
#     print(column)

# print("\nBoolean columns with >50% missing values:")
# for column in boolean_missing:
#     print(column)

# # Drop these columns from the DataFrame
# df_cleaned = df.drop(columns=columns_to_drop)

# # Save the cleaned DataFrame to a new CSV file
# df_cleaned.to_csv('data/cleaned/clean_missing_vals.csv', index=False)

# # Optionally, print out the shape of the new DataFrame to confirm the changes
# print("Shape of DataFrame after removing columns with >50% missing values:", df_cleaned.shape)
