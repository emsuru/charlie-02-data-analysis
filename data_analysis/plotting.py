import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import matplotlib.ticker as ticker


df_3 = pd.read_csv('data/cleaned/cleaned_extratypes.csv')
# Ensure that 'Price' is in numeric format
df_3['Price'] = pd.to_numeric(df_3['Price'], errors='coerce')

# Define bins and labels for all properties
bins = [0, 200000, 400000, 600000, 800000, 1000000, float('inf')]
labels = ['0-200k', '200k-400k', '400k-600k', '600k-800k', '800k-1M', '>1M']

# Create 'Price_Segment' for all properties
df_3['Price_Segment'] = pd.cut(df_3['Price'], bins=bins, labels=labels, right=False)

# Calculate the proportion of each price segment
price_segment_proportions = df_3['Price_Segment'].value_counts(normalize=True).sort_index()





# # Plot the proportions
# plt.figure(figsize=(10, 6))
# bars = sns.barplot(x=price_segment_proportions.index, y=price_segment_proportions.values, palette="Blues_d")

# plt.title('Proportion of Properties by Price Segment')
# plt.xlabel('Price Segment')
# plt.ylabel('Proportion')
# plt.xticks(rotation=45)  # Rotate labels to improve readability

# # Annotate each bar with the percentage value
# for bar in bars.patches:
#     # The text annotation for each bar should be its height (proportion) formatted as a percentage
#     bars.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
#                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
#                    ha='center',  # Center the text horizontally
#                    va='center',  # Center the text vertically within the bar
#                    size=10,  # Font size
#                    xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
#                    textcoords='offset points')  # Use offset points for positioning the text

# plt.show()

# #----This market segment by region

# # Filter the DataFrame for properties in the '200k-400k' price segment
properties_200k_400k = df_3[df_3['Price_Segment'] == '200k-400k']

# Filter the DataFrame for properties in the '200k-400k' price segment and of the "Apartment" type
apartments_200k_400k = properties_200k_400k[properties_200k_400k['Type'] == 'Apartment']

# Calculate the mean price for apartments within the '200k-400k' price segment
mean_price_apartments = apartments_200k_400k['Price'].mean()
print(len(apartments_200k_400k))

print(f"Mean Price for Apartments in the 200k-400k Segment: €{mean_price_apartments:,.2f}")

# # Count the number of properties in each region within this price segment
# region_counts = properties_200k_400k['Region'].value_counts()

# # Plot the results
# plt.figure(figsize=(10, 6))
# region_bars = sns.barplot(x=region_counts.index, y=region_counts.values, palette="coolwarm")

# plt.title('Distribution of Properties in the 200k-400k Segment by Region')
# plt.xlabel('Region')
# plt.ylabel('Number of Properties')
# plt.xticks(rotation=45)  # Rotate labels to improve readability

# # Annotate each bar with the count value
# for bar in region_bars.patches:
#     region_bars.annotate(format(bar.get_height(), '.0f'),  # Format the count as a whole number
#                          (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
#                          ha='center',  # Center the text horizontally
#                          va='center',  # Center the text vertically within the bar
#                          size=10,  # Font size
#                          xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
#                          textcoords='offset points')  # Use offset points for positioning the text

# plt.show()

# #------
# # Set the style of the seaborn plot to remove grid lines
# sns.set(style="white")

# # Assuming properties_200k_400k is already filtered for the '200k-400k' price segment

# # Calculate the mean price for each region within the '200k-400k' price segment
# mean_prices_by_region = properties_200k_400k.groupby('Region')['Price'].mean()

# # Print the mean prices for inspection
# print(mean_prices_by_region)

# # Optionally, you can plot the mean prices for a visual comparison
# plt.figure(figsize=(10, 6))
# mean_price_bars = sns.barplot(x=mean_prices_by_region.index, y=mean_prices_by_region.values, color="skyblue")

# plt.title('Mean Price of Properties in the 200k-400k Segment by Region')
# plt.xlabel('Region')
# plt.ylabel('Mean Price')
# plt.xticks(rotation=45)  # Rotate labels to improve readability

# # Set Y-axis labels manually
# plt.yticks([0, 150000, 300000], ['0', '150K', '300K'])

# # Annotate each bar with the mean price value, formatted as requested
# for bar in mean_price_bars.patches:
#     # Format the mean price as a rounded integer with the Euro sign and a comma
#     annotation = f'€{int(round(bar.get_height())):,}'
#     mean_price_bars.annotate(annotation,
#                              (bar.get_x() + bar.get_width() / 2, bar.get_height()),
#                              ha='center',
#                              va='center',
#                              size=10,
#                              xytext=(0, 8),
#                              textcoords='offset points')

# # Remove the top and right spines
# sns.despine()

# # Remove grid lines (by not specifying them to begin with in sns.set)
# plt.grid(False)

# plt.show()



# # check how many null values fo the "Facades" column
# print("Total null values in Facades:", df_3['Facades'].isnull().sum())
# # what is the proportion of null values to total values in the "Facades" column
# print("Percentage of null values in total:", f"{(df_3['Facades'].isnull().sum() / df_3['Facades'].shape[0]):.2f}")  # 0.3% of the values are null

# # drop the rows with null values & make a copy of the dataframe
# df_3_facades = df_3.dropna(subset=['Facades']).copy()

# # what are the unique values in the "Facades" column
# print("Unique values in Facades:", df_3_facades['Facades'].unique()) # [2. 3. 4. 1. 6. 5. 7. 8. 9. 0. 10. 11. 12. 14. 13. 15. 16. 18. 17. 19. 20. 21. 22. 24. 25. 23. 26. 27. 28. 29. 30. 32. 31. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53. 54. 55. 56. 57. 58. 59. 60. 61. 62. 63. 64. 65. 66. 67. 68. 69. 70. 71. 72. 73. 74. 75. 76. 77. 78. 79. 80. 81. 82. 83. 84. 85. 86. 87. 88. 89. 90. 91. 92. 93. 94. 95. 96. 97. 98. 99. 100. 101. 102. 103. 104. 105. 106. 107. 108. 109. 110. 111. 112. 113. 114. 115. 116. 117. 118. 119. 120. 121. 122. 123. 124. 125. 126. 127. 128. 129. 130. 131. 132. 133. 134. 135. 136. 137. 138. 139. 140. 141. 142. 143. 144. 145. 146. 147. 148. 149. 150. 151. 152. 153. 154. 155. 156. 157. 158. 159. 160. 161.

# #what are the proportions the unique values in the "Facades" column
# facades_proportions = df_3_facades['Facades'].value_counts(normalize=True).sort_index()
# # print each unique value in Facades column and its proportion of total values in the column
# for index, value in facades_proportions.items():
#     print("Percentage for unique value", f'{index}: {value:.4f}')

# Subset into three groups: "Attached house" : 2 facades, "Semi-attached house": 3 facades, Detached house: 4 facades or more:


# # # GRAPH 1--------------------------


# # # Ensure that 'Price' is in numeric format
# # df_3['Price'] = pd.to_numeric(df_3['Price'], errors='coerce')

# # # Define bins and labels for all properties
# # bins = [0, 200000, 400000, 600000, 800000, 1000000, float('inf')]
# # labels = ['0-200k', '200k-400k', '400k-600k', '600k-800k', '800k-1M', '>1M']

# # # Create 'Price_Segment' for all properties
# # df_3['Price_Segment'] = pd.cut(df_3['Price'], bins=bins, labels=labels, right=False)

# # # Calculate the proportion of each price segment
# # price_segment_proportions = df_3['Price_Segment'].value_counts(normalize=True).sort_index()

# # # Plot the proportions
# # plt.figure(figsize=(10, 6))
# # bars = sns.barplot(x=price_segment_proportions.index, y=price_segment_proportions.values, palette="Blues_d")

# # plt.title('Proportion of Properties by Price Segment')
# # plt.xlabel('Price Segment')
# # plt.ylabel('Proportion')
# # plt.xticks(rotation=45)  # Rotate labels to improve readability

# # # Annotate each bar with the percentage value
# # for bar in bars.patches:
# #     # The text annotation for each bar should be its height (proportion) formatted as a percentage
# #     bars.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
# #                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
# #                    ha='center',  # Center the text horizontally
# #                    va='center',  # Center the text vertically within the bar
# #                    size=10,  # Font size
# #                    xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
# #                    textcoords='offset points')  # Use offset points for positioning the text

# # plt.show()


# # # GRAPH 2 ------------------------------

# # # Calculate the count of each combination of 'Price_Segment' and 'Type'
# # segment_type_counts = df_3.groupby(['Price_Segment', 'Type']).size().reset_index(name='counts')

# # # Calculate the total count of properties in each 'Price_Segment'
# # segment_counts = df_3['Price_Segment'].value_counts().reset_index()
# # segment_counts.columns = ['Price_Segment', 'total_counts']

# # # Merge to get total counts in each segment for normalization
# # segment_type_counts = pd.merge(segment_type_counts, segment_counts, on='Price_Segment')

# # # Calculate the proportion of each type within each price segment
# # segment_type_counts['proportion'] = segment_type_counts['counts'] / segment_type_counts['total_counts']

# # # Now plot using sns.barplot with the 'hue' parameter
# # plt.figure(figsize=(12, 6))
# # sns.barplot(data=segment_type_counts, x='Price_Segment', y='proportion', hue='Type', palette='viridis')

# # plt.title('Proportion of Property Types by Price Segment')
# # plt.xlabel('Price Segment')
# # plt.ylabel('Proportion')
# # plt.xticks(rotation=45)

# # plt.show()

# # # GRAPH 3 ------------------------------

# # df_below_1m = df_3[df_3['Price'] < 1000000].copy()
# # df_above_1m = df_3[df_3['Price'] >= 1000000].copy()


# # # Ensure that 'Price' is in numeric format
# # df_below_1m['Price'] = pd.to_numeric(df_below_1m['Price'], errors='coerce')

# # # Define bins and labels for all properties below 1 million Euros
# # bins_below_1m = [0, 200000, 400000, 600000, 800000, 1000000] #
# # labels_below_1m = ['0-200k', '200k-400k', '400k-600k', '600k-800k', '800k-1M']

# # # Create 'Price_Segment' for all properties
# # df_below_1m['Price_Segment'] = pd.cut(df_below_1m['Price'], bins=bins_below_1m, labels=labels_below_1m, right=False)

# # # Calculate the proportion of each price segment
# # price_segment_proportions = df_below_1m['Price_Segment'].value_counts(normalize=True).sort_index()

# # # Plot the proportions
# # plt.figure(figsize=(10, 6))
# # bars = sns.barplot(x=price_segment_proportions.index, y=price_segment_proportions.values, palette="Blues_d")

# # plt.title('Proportion of Properties by Price Segment')
# # plt.xlabel('Price Segment')
# # plt.ylabel('Proportion')
# # plt.xticks(rotation=45)  # Rotate labels to improve readability

# # # Annotate each bar with the percentage value
# # for bar in bars.patches:
# #     # The text annotation for each bar should be its height (proportion) formatted as a percentage
# #     bars.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
# #                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
# #                    ha='center',  # Center the text horizontally
# #                    va='center',  # Center the text vertically within the bar
# #                    size=10,  # Font size
# #                    xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
# #                    textcoords='offset points')  # Use offset points for positioning the text

# # plt.show()

# # # GRAPH 4 ------------------------------

# # df_above_1m['Price'] = pd.to_numeric(df_above_1m['Price'], errors='coerce')

# # # Define bins and labels for all properties above 1 million Euros
# # bins_above_1m = [1000000, 2000000, 3000000, 4000000] #
# # labels_above_1m = ['1M-2M', '2M-3M', '3M-4M']

# # # Create 'Price_Segment' for all properties
# # df_above_1m['Price_Segment'] = pd.cut(df_above_1m['Price'], bins=bins_above_1m, labels=labels_above_1m, right=False)

# # # Calculate the proportion of each price segment
# # price_segment_proportions_above = df_above_1m['Price_Segment'].value_counts(normalize=True).sort_index()

# # # Plot the proportions
# # plt.figure(figsize=(10, 6))
# # bars_above = sns.barplot(x=price_segment_proportions_above.index, y=price_segment_proportions_above.values, palette="Blues_d")

# # plt.title('Proportion of Properties by Price Segment')
# # plt.xlabel('Price Segment')
# # plt.ylabel('Proportion')
# # plt.xticks(rotation=45)  # Rotate labels to improve readability

# # # Annotate each bar with the percentage value
# # for bar in bars_above.patches:
# #     # The text annotation for each bar should be its height (proportion) formatted as a percentage
# #     bars_above.annotate(format(bar.get_height(), '.1%'),  # Format the proportion as a percentage with one decimal place
# #                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),  # Position for the text (x, y)
# #                    ha='center',  # Center the text horizontally
# #                    va='center',  # Center the text vertically within the bar
# #                    size=10,  # Font size
# #                    xytext=(0, 8),  # Position offset for the text (to be slightly above the bar)
# #                    textcoords='offset points')  # Use offset points for positioning the text

# # plt.show()

# # # GRAPH 5 ------------------------------

# # # Ensure that 'Price' is in numeric format
# # df_above_1m['Price'] = pd.to_numeric(df_above_1m['Price'], errors='coerce')

# # # Define bins and labels for all properties above 1 million Euros
# # bins_above_1m = [1000000, 2000000, 3000000, 4000000, float('inf')]
# # labels_above_1m = ['1M-2M', '2M-3M', '3M-4M', '>4M']

# # # Create 'Price_Segment' for all properties
# # df_above_1m['Price_Segment'] = pd.cut(df_above_1m['Price'], bins=bins_above_1m, labels=labels_above_1m, right=False)

# # # Now plot using sns.boxplot to see the distribution within each price segment
# # plt.figure(figsize=(10, 6))
# # sns.boxplot(data=df_above_1m, x='Price_Segment', y='Price', palette="Blues_d")

# # plt.title('Distribution of Property Prices by Price Segment')
# # plt.xlabel('Price Segment')
# # plt.ylabel('Price')
# # plt.xticks(rotation=45)  # Rotate labels to improve readability

# # plt.show()

# # GRAPH 6 ------------------------------
# # check how many null values fo the "Facades" column

# print("Total null values in Facades:", df_3['Facades'].isnull().sum())
# # what is the proportion of null values to total values in the "Facades" column
# print("Percentage of null values in total:", f"{(df_3['Facades'].isnull().sum() / df_3['Facades'].shape[0]):.2f}")  # 0.3% of the values are null

# # drop the rows with null values & make a copy of the dataframe
# df_3_facades = df_3.dropna(subset=['Facades']).copy()

# # what are the unique values in the "Facades" column
# print("Unique values in Facades:", df_3_facades['Facades'].unique()) # [2. 3. 4. 1. 6. 5. 7. 8. 9. 0. 10. 11. 12. 14. 13. 15. 16. 18. 17. 19. 20. 21. 22. 24. 25. 23. 26. 27. 28. 29. 30. 32. 31. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53. 54. 55. 56. 57. 58. 59. 60. 61. 62. 63. 64. 65. 66. 67. 68. 69. 70. 71. 72. 73. 74. 75. 76. 77. 78. 79. 80. 81. 82. 83. 84. 85. 86. 87. 88. 89. 90. 91. 92. 93. 94. 95. 96. 97. 98. 99. 100. 101. 102. 103. 104. 105. 106. 107. 108. 109. 110. 111. 112. 113. 114. 115. 116. 117. 118. 119. 120. 121. 122. 123. 124. 125. 126. 127. 128. 129. 130. 131. 132. 133. 134. 135. 136. 137. 138. 139. 140. 141. 142. 143. 144. 145. 146. 147. 148. 149. 150. 151. 152. 153. 154. 155. 156. 157. 158. 159. 160. 161.

# #what are the proportions the unique values in the "Facades" column
# facades_proportions = df_3_facades['Facades'].value_counts(normalize=True).sort_index()
# # print each unique value in Facades column and its proportion of total values in the column
# for index, value in facades_proportions.items():
#     print("Percentage for unique value", f'{index}: {value:.4f}')

# # Subset into three groups: "Attached house" : 2 facades, "Semi-attached house": 3 facades, Detached house: 4 facades or more:
# df_3_facades['Facades_Group'] = pd.cut(df_3_facades['Facades'], bins=[1, 2, 3, float('inf')], labels=['Attached house', 'Semi-attached house', 'Detached house'])
# #print all column names in the dataframe
# print(df_3_facades.columns)

# # create a a bar plot showing the three types of Facades groups





# # -------------------HOW I CREATED REGION---------------------
# # Function to determine the region based on the province
# def province_to_region(province):
#     if province in ['LUIK', 'LIMBURG', 'WAALS-BRABANT', 'LUXEMBURG', 'NAMEN', 'HENEGOUWEN']:
#         return 'Wallonia'
#     elif province == 'BRUSSEL':
#         return 'Brussels'
#     elif province in ['OOST-VLAANDEREN', 'ANTWERPEN', 'VLAAMS-BRABANT', 'WEST-VLAANDEREN']:
#         return 'Flanders'
#     else:
#         return 'Unknown'  # For any province value not listed above

# # Apply the function to the 'Province' column to create the new 'Region' column
# df_2['Region'] = df_2['Province'].apply(province_to_region)
