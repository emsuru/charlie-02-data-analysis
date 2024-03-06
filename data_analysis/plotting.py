import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


df_3 = pd.read_csv('data/cleaned/cleaned_extratypes.csv')


# GRAPH 1--------------------------


# Ensure that 'Price' is in numeric format
df_3['Price'] = pd.to_numeric(df_3['Price'], errors='coerce')

# Define bins and labels for all properties
bins = [0, 200000, 400000, 600000, 800000, 1000000, float('inf')]
labels = ['0-200k', '200k-400k', '400k-600k', '600k-800k', '800k-1M', '>1M']

# Create 'Price_Segment' for all properties
df_3['Price_Segment'] = pd.cut(df_3['Price'], bins=bins, labels=labels, right=False)

# Calculate the proportion of each price segment
price_segment_proportions = df_3['Price_Segment'].value_counts(normalize=True).sort_index()

# Plot the proportions
plt.figure(figsize=(10, 6))
bars = sns.barplot(x=price_segment_proportions.index, y=price_segment_proportions.values, palette="Blues_d")

plt.title('Proportion of Properties by Price Segment')
plt.xlabel('Price Segment')
plt.ylabel('Proportion')
plt.xticks(rotation=45)  # Rotate labels to improve readability

# Annotate each bar with the percentage value
for bar in bars.patches:
    # The text annotation for each bar should be its height (proportion) formatted as a percentage
    bars.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
                   (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
                   ha='center',  # Center the text horizontally
                   va='center',  # Center the text vertically within the bar
                   size=10,  # Font size
                   xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
                   textcoords='offset points')  # Use offset points for positioning the text

plt.show()


# GRAPH 2 ------------------------------

# Calculate the count of each combination of 'Price_Segment' and 'Type'
segment_type_counts = df_3.groupby(['Price_Segment', 'Type']).size().reset_index(name='counts')

# Calculate the total count of properties in each 'Price_Segment'
segment_counts = df_3['Price_Segment'].value_counts().reset_index()
segment_counts.columns = ['Price_Segment', 'total_counts']

# Merge to get total counts in each segment for normalization
segment_type_counts = pd.merge(segment_type_counts, segment_counts, on='Price_Segment')

# Calculate the proportion of each type within each price segment
segment_type_counts['proportion'] = segment_type_counts['counts'] / segment_type_counts['total_counts']

# Now plot using sns.barplot with the 'hue' parameter
plt.figure(figsize=(12, 6))
sns.barplot(data=segment_type_counts, x='Price_Segment', y='proportion', hue='Type', palette='viridis')

plt.title('Proportion of Property Types by Price Segment')
plt.xlabel('Price Segment')
plt.ylabel('Proportion')
plt.xticks(rotation=45)

plt.show()

# GRAPH 3 ------------------------------

df_below_1m = df_3[df_3['Price'] < 1000000].copy()
df_above_1m = df_3[df_3['Price'] >= 1000000].copy()


# Ensure that 'Price' is in numeric format
df_below_1m['Price'] = pd.to_numeric(df_below_1m['Price'], errors='coerce')

# Define bins and labels for all properties below 1 million Euros
bins_below_1m = [0, 200000, 400000, 600000, 800000, 1000000] #
labels_below_1m = ['0-200k', '200k-400k', '400k-600k', '600k-800k', '800k-1M']

# Create 'Price_Segment' for all properties
df_below_1m['Price_Segment'] = pd.cut(df_below_1m['Price'], bins=bins_below_1m, labels=labels_below_1m, right=False)

# Calculate the proportion of each price segment
price_segment_proportions = df_below_1m['Price_Segment'].value_counts(normalize=True).sort_index()

# Plot the proportions
plt.figure(figsize=(10, 6))
bars = sns.barplot(x=price_segment_proportions.index, y=price_segment_proportions.values, palette="Blues_d")

plt.title('Proportion of Properties by Price Segment')
plt.xlabel('Price Segment')
plt.ylabel('Proportion')
plt.xticks(rotation=45)  # Rotate labels to improve readability

# Annotate each bar with the percentage value
for bar in bars.patches:
    # The text annotation for each bar should be its height (proportion) formatted as a percentage
    bars.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
                   (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
                   ha='center',  # Center the text horizontally
                   va='center',  # Center the text vertically within the bar
                   size=10,  # Font size
                   xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
                   textcoords='offset points')  # Use offset points for positioning the text

plt.show()

# GRAPH 4 ------------------------------

df_above_1m['Price'] = pd.to_numeric(df_above_1m['Price'], errors='coerce')

# Define bins and labels for all properties above 1 million Euros
bins_above_1m = [1000000, 2000000, 3000000, 4000000] #
labels_above_1m = ['1M-2M', '2M-3M', '3M-4M']

# Create 'Price_Segment' for all properties
df_above_1m['Price_Segment'] = pd.cut(df_above_1m['Price'], bins=bins_above_1m, labels=labels_above_1m, right=False)

# Calculate the proportion of each price segment
price_segment_proportions_above = df_above_1m['Price_Segment'].value_counts(normalize=True).sort_index()

# Plot the proportions
plt.figure(figsize=(10, 6))
bars_above = sns.barplot(x=price_segment_proportions_above.index, y=price_segment_proportions_above.values, palette="Blues_d")

plt.title('Proportion of Properties by Price Segment')
plt.xlabel('Price Segment')
plt.ylabel('Proportion')
plt.xticks(rotation=45)  # Rotate labels to improve readability

# Annotate each bar with the percentage value
for bar in bars_above.patches:
    # The text annotation for each bar should be its height (proportion) formatted as a percentage
    bars_above.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
                   (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
                   ha='center',  # Center the text horizontally
                   va='center',  # Center the text vertically within the bar
                   size=10,  # Font size
                   xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
                   textcoords='offset points')  # Use offset points for positioning the text

plt.show()

# GRAPH 5 ------------------------------

# Ensure that 'Price' is in numeric format
df_above_1m['Price'] = pd.to_numeric(df_above_1m['Price'], errors='coerce')

# Define bins and labels for all properties above 1 million Euros
bins_above_1m = [1000000, 2000000, 3000000, 4000000, float('inf')]
labels_above_1m = ['1M-2M', '2M-3M', '3M-4M', '>4M']

# Create 'Price_Segment' for all properties
df_above_1m['Price_Segment'] = pd.cut(df_above_1m['Price'], bins=bins_above_1m, labels=labels_above_1m, right=False)

# Now plot using sns.boxplot to see the distribution within each price segment
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_above_1m, x='Price_Segment', y='Price', palette="Blues_d")

plt.title('Distribution of Property Prices by Price Segment')
plt.xlabel('Price Segment')
plt.ylabel('Price')
plt.xticks(rotation=45)  # Rotate labels to improve readability

plt.show()
