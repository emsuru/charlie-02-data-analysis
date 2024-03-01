## Project Description

You are given a raw data set containing information about real estate properties in Belgium. Your task is to clean the data, analyze it, and present your findings to the management of a real estate company.

Broadly speaking, you should answer two main questions:

1. What are currently the most interesting insights about the Belgian real estate market?
2. What variables are the most important when determining the price of a property?

## Mission Objectives
- Be able to use pandas
- Be able to use a data visualization library of your choice (such as matplotlib, seaborn, plotly)
- Be able to clean a dataset for analysis
- Be able to use colors in visualizations correctly
- Be able to establish conclusions about a dataset
- Be able to find and answer creative questions about data
- Be able to present your insights to a non-technical audience


## Steps

### Step 1: Data Cleaning
You have collected your data, time to further clean it.

A cleaned dataset is a dataset that doesn't contain any duplicates, has no blank spaces, and has no other obvious errors. The rest of the analysis is worthless if you neglect this step; Garbage In, Garbage Out.

Take care of the following:


No duplicates
No blank spaces (e.g. " I love python " => "I love python")
No empty values (set them to None or NaN)
No wrongly encoded values (e.g. a text value in the price column)

### Step 2: Data Analysis

Now that the data has been both collected and cleaned, let's move on to the analysis.

You must be able to answer following questions (with a vizualization if appropriate):

1. How many observations and features do you have?
2. What is the proportion of missing values per column?
3. Which variables would you delete and why?
4. What variables are most subject to outliers?
5. How many qualitative and quantitative variables are there? How would you transform the qualitative values into numerical values?
6. What is the correlation between the variables and the price? Why do you think some variables are more correlated than others?
7. How are the variables themselves correlated to each other? Can you find groups of variables that are correlated together?
8. How are the number of properties distributed according to their surface?
8. Which five variables do you consider the most important and why?
10. What are the least/most expensive municipalities in Belgium/Wallonia/Flanders? (in terms of price per m², average price, and median price)

This is a non-exhaustive list of possible questions. Try to make a maximum number of interpretations from the dataset. Bonus points for creative and out-of-the-box insights.

Use tools such as matplotlib, seaborn, plotly, or [insert whatever visualization tool you find useful]...

Do your analysis in notebooks. No real need for scripting in this case, you'll want to have your hands free to experiment and explore the data in many directions. Writing functions for code you reuse is still a good idea, don't lose track of your good habits. Don't make it too messy though, your results should be reproducible and Immo Eliza's CEO might ask to rerun an analysis with a slight change :-)

### Step 3: Presentation

After analyzing your data, you're finally ready to present your results. You have to communicate your analysis using simple words and clear graphs, and ideally also deliver a few recommendations.

You can make your plots presentation-ready by accounting for the following points:

A clear title
A legend (if applicable)
Add axis labels (in understandable language, no variable names)
Add axis units
Have comparable scales
Have no overlapping text
A main takeaway
Remove all clutter that doesn't contribute to the message
Smart use of colors
Don't mention data cleaning in your presentation as this is a technical background task. You should focus on the insights you found and the recommendations you can make.

## Repository

Create a new repository for the analysis and modeling steps of the project.

Establish the following:

- In your data/ folder:
    - Have a raw/ folder with the original dataset
    - Have a cleaned/ folder with the cleaned dataset
- Make a clean.py script for any additional cleaning
- Add your notebooks in an analysis/ folder
- Put your finalized presentation in .pdf format in a reports/ folder

In general, think modular! You do not want to run all steps at once, so your code should be tailored to that gradual process: scrape, clean, analyze, model, deploy, ...
