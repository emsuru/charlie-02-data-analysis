import pandas as pd  # Importing the pandas library for data manipulation
import os  # Importing the os library to interact with the operating system


# Function to load data from a specified path
def load_data(path):
    # Getting the current directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Creating a new path by joining the current directory with the relative path to the data
    newpath = os.path.join(current_dir, "..", "data", "raw", path)
    # Reading the CSV file from the new path into a pandas DataFrame
    data = pd.read_csv(newpath)
    # Removing duplicate rows based on the "ID" column
    data.drop_duplicates(subset="ID", inplace=True)
    # Setting the "ID" column as the index of the DataFrame - WHY?
    data.set_index("ID", drop=True, inplace=True)
    return data  # Returning the cleaned DataFrame

# Function to fill empty data in specific columns
def fill_empty_data(data):
    # Filling missing values in "Swimming Pool" column with 0
    data.loc[data["Swimming Pool"].isna(), "Swimming Pool"] = 0
    # Setting "Fireplace Count" to 0 where "Openfire" is False
    data.loc[data["Openfire"] == False, "Fireplace Count"] = 0
    # For rows where "Openfire" is True, fill missing "Fireplace Count" with 1 and keep existing positive values
    data.loc[data["Openfire"] == True, "Fireplace Count"] = (
        data["Fireplace Count"].abs().fillna(1)
    )
    # Setting "Terrace Surface" to 0 where "Terrace" is False
    data.loc[data["Terrace"] == False, "Terrace Surface"] = 0
    # Setting "Garden Surface" to 0 where "Garden Exists" is False
    data.loc[data["Garden Exists"] == False, "Garden Surface"] = 0
    return data  # Returning the DataFrame with filled values

# Function to append additional data from another file to the existing DataFrame
def append_data(data):
    # Getting the current directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Reading a CSV file containing postal codes into a pandas DataFrame
    postals = pd.read_csv(os.path.join("data", "src", "zipcodes.csv"))
    # Looping through each postal code in the data
    for postalcode in data["Postal Code"]:
        # Extracting the municipality and province for the current postal code
        municipality = postals[postals["Postcode"] == postalcode]["Hoofdgemeente"]
        province = postals[postals["Postcode"] == postalcode]["Provincie"]
        # If the municipality is found, update the "Municipality" column in the data
        if not municipality.empty:
            data.loc[data["Postal Code"] == postalcode, "Municipality"] = (
                municipality.values[0]
            )
        # If the province is found, update the "Province" column in the data
        if not province.empty:
            data.loc[data["Postal Code"] == postalcode, "Province"] = province.values[0]
    return data  # Returning the updated DataFrame

# Main function to execute the data cleaning process
def main():
    raw_data = load_data("rawdata.csv")  # Loading raw data
    filled_data = fill_empty_data(raw_data)  # Filling empty data
    appended_data = append_data(filled_data)  # Appending additional data

    # Construct the path to the 'data/cleaned' directory dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(current_dir, "..", "data", "cleaned", "appended_data.csv")

    # Ensure the directory exists before saving
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the appended data to the constructed path
    appended_data.to_csv(save_path)

# Checking if this script is the main program and not an imported module
if __name__ == "__main__":
    main()



# def to_html(fig, path):
#     # Save the plot as an HTML file
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     newpath = os.path.join(current_dir, "data", "cleaned", path)
#     fig.write_html(newpath)


# def exclude_outliers(df: DataFrame):
#     # drop the row where type is not house or appartment
#     df = df[df["Type"].isin(["APARTMENT", "HOUSE"]) | df["Type"].isna()]

#     # drop Kitchen Surface > 100
#     df = df[(df["Kitchen Surface"] < 100) | df["Kitchen Surface"].isna()]

#     # drop Build year "< 1850"
#     df = df[(df["Build Year"] > 1850) | df["Build Year"].isna()]

#     # facades <2 -> 2, >4 -> 4
#     df["Facades"] = df["Facades"].apply(lambda x: 2 if x < 2 else x)
#     df["Facades"] = df["Facades"].apply(lambda x: 4 if x > 4 else x)

#     # drop Bathroom Count > 4
#     df = df[(df["Bathroom Count"] < 4) | df["Bathroom Count"].isna()]

#     # drop bedroom count > 5
#     df = df[(df["Bedroom Count"] < 5) | df["Bedroom Count"].isna()]

#     # drop colum fireplace count
#     df.drop(columns=["Fireplace Count"], inplace=True)

#     # drop garden surface > 5000
#     df = df[(df["Garden Surface"] < 5000) | df["Garden Surface"].isna()]

#     # habitable surface > 700
#     df = df[(df["Habitable Surface"] < 700) | df["Habitable Surface"].isna()]

#     # drop Landsurface > 3000
#     df = df[(df["Land Surface"] < 3000) | df["Land Surface"].isna()]

#     # drop the column parking box count
#     df.drop(columns=["Parking box count"], inplace=True)

#     # drop items with price > 1_000_000
#     df = df[(df["Price"] < 1000000) | df["Price"].isna()]

#     # drop items that have sale type LIFE_ANNUITY_SALE
#     df = df[df["Sale Type"] != "LIFE_ANNUITY_SALE"]

#     # drop sewer column
#     df.drop(columns=["Sewer"], inplace=True)

#     # only keep items that have SubType == HOUSE, VILLA, TOWN_HOUSE, BUNGALOW, or not specified
#     # df = df[df['Subtype'].isin(['HOUSE', 'VILLA', 'TOWN_HOUSE', 'BUNGALOW', None, '']) | df['Subtype'].isna()]

#     # only keep items that have toilets of < 6
#     df = df[(df["Toilet Count"] < 6) | df["Toilet Count"].isna()]

#     return df
