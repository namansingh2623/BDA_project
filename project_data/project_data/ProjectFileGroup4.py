import pandas as pd
import os
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.tools as tls 

import dataprocessing as dp

dataframes = dp.process_and_clean_data()

# Access a specific DataFrame
education_53_2333 = dataframes["education_53_2333"]
print(education_53_2333)



# correlation_matrix = education_53_1929[numerical_columns].corr()

# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True, square=True)
# plt.title('Feature Correlation Matrix')
# plt.show()

import plotly.express as px

def generate_correlation_heatmap(dataframes,  title='Feature Correlation Matrix', figsize=(8, 6), cmap='coolwarm'):
    """
    Generate a heatmap for the correlation matrix of specified numerical columns.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    numerical_columns (list): List of numerical column names to compute the correlation matrix.
    title (str): Title of the heatmap. Default is 'Feature Correlation Matrix'.
    figsize (tuple): Size of the figure. Default is (8, 6).
    cmap (str): Colormap for the heatmap. Default is 'coolwarm'.

    Returns:
    matplotlib.figure.Figure: The figure object containing the heatmap.
    """
    dataframe = dataframes['education_53_1929']
    numerical_columns = [
    "High school diploma or equivalent", 
    "Some college, no degree", 
    "Associate's degree",
    "Bachelor's degree", 
    "Master's degree", 
    "Doctoral or professional degree"
    ]
    correlation_matrix = dataframe[numerical_columns].corr()

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", cbar=True, square=True, ax=ax)
    ax.set_title(title)

    return fig
# Data for 2023
def employment_dist_by_education_level(dataframes):
    labels_2023 = dataframes['education_52_2333']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2023 = dataframes['education_52_2333']['Employment distribution, percent, 2023'][1:]

    # Data for 2019
    labels_2019 = dataframes['education_52_1929']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2019 = dataframes['education_52_1929']['Employment distribution, percent, 2019'][1:]

    # Ensure labels match for comparison
    # assert list(labels_2023) == list(labels_2019), "Labels for 2019 and 2023 do not match!"

    # Create positions for the bars
    x = np.arange(len(labels_2023))  # Positions for groups
    width = 0.35  # Width of each bar

    # Plot the grouped bar chart
    plt.figure(figsize=(14, 7))
    plt.bar(x - width/2, values_2023, width, label='2023', color='skyblue', edgecolor='black')
    plt.bar(x + width/2, values_2019, width, label='2019', color='lightcoral', edgecolor='black')

    # Add labels, title, and legend
    plt.title('Employment Distribution by Education Level: 2019 vs 2023', fontsize=16)
    plt.xlabel('Education Level', fontsize=14)
    plt.ylabel('Employment Distribution (%)', fontsize=14)
    plt.xticks(x, labels_2023, rotation=45, ha='right', fontsize=12)
    plt.legend(title="Year", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()



def emp_pred_chang_by_education_1929_2333(dataframes):
# Data for 2019
    labels_2019 = dataframes['education_52_1929']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2019 = dataframes['education_52_1929']['Employment change, percent, 2019-29'][1:]

    # Data for 2023
    labels_2023 = dataframes['education_52_2333']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2023 = dataframes['education_52_2333']['Percent employment change, 2023-33'][1:]

    # Ensure labels match for comparison
    # assert list(labels_2023) == list(labels_2019), "Labels for 2019 and 2023 do not match!"

    # Convert labels to positions for plotting
    x = np.arange(len(labels_2023))  # Positions for each education level

    # Plot the line graph
    plt.figure(figsize=(14, 7))
    plt.plot(x, values_2023, label='2023', marker='o', color='skyblue', linewidth=2)
    plt.plot(x, values_2019, label='2019', marker='o', color='lightcoral', linewidth=2)

    # Add labels, title, and legend
    plt.title('Employment Prediction Change by Education Level: 2019-29 vs 2023-33', fontsize=16)
    plt.xlabel('Education Level', fontsize=14)
    plt.ylabel('Employment Change (%)', fontsize=14)
    plt.xticks(x, labels_2023, rotation=45, ha='right', fontsize=12)
    plt.legend(title="Year", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

def median_wage_change(dataframes):


    labels_2019 = dataframes['education_52_1929']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2019 = dataframes['education_52_1929']['Median annual wage, 2020(1)'][1:]

    # Data for 2023
    labels_2023 = dataframes['education_52_2333']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2023 = dataframes['education_52_2333']['Median annual wage, dollars, 2023[1]'][1:]

    # Ensure labels match for comparison
    # assert list(labels_2023) == list(labels_2019), "Labels for 2019 and 2023 do not match!"

    # Convert labels to positions for plotting
    x = np.arange(len(labels_2023))  # Positions for each education level

    # Plot the line graph
    # Plot area chart
    plt.figure(figsize=(14, 7))
    plt.fill_between(x, values_2023, alpha=0.6, color='skyblue', label='2023')
    plt.fill_between(x, values_2019, alpha=0.6, color='lightcoral', label='2019')
    plt.plot(x, values_2023, marker='o', color='skyblue', linewidth=2)
    plt.plot(x, values_2019, marker='o', color='lightcoral', linewidth=2)

    # Add labels, title, and legend
    plt.title('Median Annual Wage Change from 2020 vs 2023', fontsize=16)
    plt.xlabel('Education Level', fontsize=14)
    plt.ylabel('Median Annual Wage ($)', fontsize=14)
    plt.xticks(x, labels_2023, rotation=45, ha='right', fontsize=12)
    plt.legend(title="Year", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()