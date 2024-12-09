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

def generate_correlation_heatmap(dataframes, title='Feature Correlation Matrix'):
    """
    Generate a heatmap for the correlation matrix of specified numerical columns using Plotly.
    """
    numerical_columns = [
        "High school diploma or equivalent",
        "Some college, no degree",
        "Associate's degree",
        "Bachelor's degree",
        "Master's degree",
        "Doctoral or professional degree",
    ]
    dataframe = dataframes['education_53_1929']
    correlation_matrix = dataframe[numerical_columns].corr()

    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="ylgnbu",
        title=title,
    )
    return fig

# Data for 2023
# def employment_dist_by_education_level(dataframes):
#     labels_2023 = dataframes['education_52_2333']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
#     values_2023 = dataframes['education_52_2333']['Employment distribution, percent, 2023'][1:]

#     # Data for 2019
#     labels_2019 = dataframes['education_52_1929']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
#     values_2019 = dataframes['education_52_1929']['Employment distribution, percent, 2019'][1:]

#     # Ensure labels match for comparison
#     # assert list(labels_2023) == list(labels_2019), "Labels for 2019 and 2023 do not match!"

#     # Create positions for the bars
#     x = np.arange(len(labels_2023))  # Positions for groups
#     width = 0.35  # Width of each bar

#     # Plot the grouped bar chart
#     plt.figure(figsize=(14, 7))
#     plt.bar(x - width/2, values_2023, width, label='2023', color='skyblue', edgecolor='black')
#     plt.bar(x + width/2, values_2019, width, label='2019', color='lightcoral', edgecolor='black')

#     # Add labels, title, and legend
#     plt.title('Employment Distribution by Education Level: 2019 vs 2023', fontsize=16)
#     plt.xlabel('Education Level', fontsize=14)
#     plt.ylabel('Employment Distribution (%)', fontsize=14)
#     plt.xticks(x, labels_2023, rotation=45, ha='right', fontsize=12)
#     plt.legend(title="Year", fontsize=12)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)

#     # Adjust layout and show the plot
#     plt.tight_layout()
#     plt.show()
import plotly.graph_objects as go
import numpy as np

def employment_dist_by_education_level(dataframes):
    """
    Generate a grouped bar chart comparing employment distribution by education level for 2019 and 2023 using Plotly.
    """
    # Data for 2023
    labels_2023 = dataframes['education_52_2333']['Typical entry-level education'].str.strip() # this was the fix for side by side bars
    values_2023 = dataframes['education_52_2333']['Employment distribution, percent, 2023']

    # Data for 2019
    labels_2019 = dataframes['education_52_1929']['Typical entry-level education']
    values_2019 = dataframes['education_52_1929']['Employment distribution, percent, 2019']

    # Create the grouped bar chart using Plotly
    fig = go.Figure()

    # Add bars for 2023
    fig.add_trace(
        go.Bar(
            x=labels_2023,
            y=values_2023,
            name='2023',
            marker=dict(color='skyblue', line=dict(color='black', width=1)),
        )
    )

    # Add bars for 2019
    fig.add_trace(
        go.Bar(
            x=labels_2019,
            y=values_2019,
            name='2019',
            marker=dict(color='lightcoral', line=dict(color='black', width=1)),
        )
    )

    # Update layout for the chart
    fig.update_layout(
        title='Employment Distribution by Education Level: 2019 vs 2023',
        xaxis_title='Education Level',
        yaxis_title='Employment Distribution (%)',
        barmode='group',
        xaxis=dict(tickangle=45),
        legend_title='Year',
        template='plotly_white',
    )

    return fig


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

def skill_importance_high_vs_low(dataframes):
    # Define skill columns
    skill_columns = [
        'Adaptability', 'Computers and information technology', 'Creativity and innovation',
        'Critical and analytical thinking', 'Customer service', 'Detail oriented', 'Fine motor',
        'Interpersonal', 'Leadership', 'Mathematics', 'Mechanical', 'Physical strength and stamina',
        'Problem solving and decision making', 'Project management', 'Science', 'Speaking and listening',
        'Writing and reading'
    ]
    
    # Ensure skill columns are numeric
    dataframes['skills_62_2333'][skill_columns] = dataframes['skills_62_2333'][skill_columns].apply(pd.to_numeric, errors='coerce')

    # Clean and convert the 'Median annual wage, dollars, 2023[1]' column
    dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] = (
        dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]']
        .astype(str)  # Convert to string
        .str.replace(',', '', regex=True)  # Remove commas
        .str.extract('(\d+)', expand=False)  # Extract numeric part
    )
    dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] = pd.to_numeric(
        dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'], errors='coerce'
    )

    # Debugging: Check unique values and distribution
    print("Unique values in wage column:")
    print(dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'].unique())
    print("Wage column statistics:")
    print(dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'].describe())

    # Filter for high-wage and low-wage occupations
    high_wage = dataframes['skills_62_2333'][dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] > 90000]
    low_wage = dataframes['skills_62_2333'][dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] < 60000]

    # Debugging: Check filtered data
    print(f"High-wage occupations count: {high_wage.shape[0]}")
    print(f"Low-wage occupations count: {low_wage.shape[0]}")

    # If no data for either category, return an empty figure
    if high_wage.empty or low_wage.empty:
        print("Warning: No data available for high-wage or low-wage occupations.")
        return px.line_polar(title="Skill Importance for High-Wage vs Low-Wage Occupations (No Data)")

    # Calculate average skill ratings for each wage group
    high_wage_skills = high_wage[skill_columns].mean().fillna(0)
    low_wage_skills = low_wage[skill_columns].mean().fillna(0)

    # Prepare data for radar chart
    radar_data = pd.DataFrame({
        'Skill': skill_columns,
        'High-Wage': high_wage_skills.values,
        'Low-Wage': low_wage_skills.values
    })

    # Melt the dataframe for Plotly radar chart
    radar_data = radar_data.melt(id_vars='Skill', var_name='Wage Group', value_name='Skill Rating')

    # Create radar chart
    fig = px.line_polar(
        radar_data,
        r='Skill Rating',
        theta='Skill',
        color='Wage Group',
        title='Skill Importance for High-Wage vs Low-Wage Occupations',
        line_close=True
    )
    fig.update_traces(fill='toself')
    
    # Return the figure
    #fig.show()
    return fig

def most_important_skills_for_cs_jobs(dataframes):
    # Define skill columns
    skill_columns = [
        'Adaptability', 'Computers and information technology', 'Creativity and innovation',
        'Critical and analytical thinking', 'Customer service', 'Detail oriented', 'Fine motor',
        'Interpersonal', 'Leadership', 'Mathematics', 'Mechanical', 'Physical strength and stamina',
        'Problem solving and decision making', 'Project management', 'Science', 'Speaking and listening',
        'Writing and reading'
    ]
    
    # Ensure skill columns are numeric
    dataframes['skills_62_2333'][skill_columns] = dataframes['skills_62_2333'][skill_columns].apply(pd.to_numeric, errors='coerce')

    # Filter rows where '2023 National Employment Matrix code' starts with '15'
    cs_jobs = dataframes['skills_62_2333'][dataframes['skills_62_2333']['2023 National Employment Matrix code'].astype(str).str.startswith('15')]

    # Calculate the average skill ratings for computer science jobs
    avg_skill_ratings = cs_jobs[skill_columns].mean().sort_values(ascending=False)

    # Prepare data for visualization
    skill_data = pd.DataFrame({
        'Skill': avg_skill_ratings.index,
        'Average Rating': avg_skill_ratings.values
    })

    # Create bar chart
    fig = px.bar(
        skill_data,
        x='Skill',
        y='Average Rating',
        title='Most Important Skills for Computer Science Jobs',
        labels={'Skill': 'Skills', 'Average Rating': 'Average Skill Rating'},
        template='plotly_white'
    )
    fig.update_layout(xaxis_tickangle=45)  # Rotate x-axis labels for readability
    
    #fig.show()
    return fig
