# Cleaning Phase 2: MISSING VALUES

import pandas as pd

# Load the working dataset
df_bear = pd.read_csv('data/cleaned/bear_cleaned_duplicates.csv')

def clean_missing_vals(df):
    # How many rows and columns are in the dataset?
    print("Number of observations (rows):", df.shape[0])
    print("Number of features (columns):", df.shape[1])
    # Identify columns with more than 50% missing values
    columns_to_drop = df.columns[df.isnull().mean() > 0.5]
    # Print out these columns and their data types
    print("Columns with >50% missing values and their data types:")
    for column in columns_to_drop:
        print(f"{column}: {df[column].dtype}")

    # Categorize these columns by their data types
    quantitative_missing = df[columns_to_drop].select_dtypes(include=['int64', 'float64']).columns
    qualitative_missing = df[columns_to_drop].select_dtypes(include=['object', 'category']).columns
    boolean_missing = df[columns_to_drop].select_dtypes(include=['bool']).columns

    # Print out the categorization
    print("\nQuantitative columns with >50% missing values:")
    for column in quantitative_missing:
        print(column)

    print("\nQualitative columns with >50% missing values:")
    for column in qualitative_missing:
        print(column)

    print("\nBoolean columns with >50% missing values:")
    for column in boolean_missing:
        print(column)

    df_cleaned = df.drop(columns=columns_to_drop) # Drop these columns from the DataFrame
    df_cleaned.to_csv('data/cleaned/bear_cleaned_missing_vals.csv', index=False) # Save the cleaned DataFrame to a new CSV file

    print("Shape of DataFrame after removing columns with >50% missing values:", df_cleaned.shape)
    #print name of columns that remained after removing columns with >50% missing values
    print("Columns that remained after removing columns with >50% missing values:", df_cleaned.columns)


clean_missing_vals(df_bear)
