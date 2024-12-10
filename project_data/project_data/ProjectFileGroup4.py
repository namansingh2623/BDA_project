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


import plotly.graph_objects as go

def emp_pred_chang_by_education_1929_2333(dataframes):
    """
    Create a line graph comparing employment prediction changes by education level (2019-29 vs 2023-33).
    
    Parameters:
    dataframes (dict): Dictionary containing DataFrames for 2019-29 and 2023-33 employment data.
    
    Returns:
    fig (plotly.graph_objects.Figure): A Plotly figure for Dash.
    """
    # Data for 2019
    labels_2019 = dataframes['education_52_1929']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2019 = dataframes['education_52_1929']['Employment change, percent, 2019-29'][1:]

    # Data for 2023
    labels_2023 = dataframes['education_52_2333']['Typical entry-level education'][1:]  # Exclude Total, All Occupations
    values_2023 = dataframes['education_52_2333']['Percent employment change, 2023-33'][1:]

    # Create a Plotly figure
    fig = go.Figure()

    # Add trace for 2019 data
    # fig.add_trace(go.Scatter(
    #     x=labels_2019,
    #     y=values_2019,
    #     mode='lines+markers',
    #     name='2019-29',
    #     line=dict(color='lightcoral', width=2),
    #     marker=dict(size=8)
    # ))

    # Add trace for 2023 data
    fig.add_trace(go.Scatter(
        x=labels_2023,
        y=values_2023,
        mode='lines+markers',
        name='2023-33',
        line=dict(color='skyblue', width=2),
        marker=dict(size=8)
    ))

    # Update layout
    fig.update_layout(
        title="Employment Prediction Change by Education Level: 2023-33",
        xaxis_title="Education Level",
        yaxis_title="Employment Change (%)",
        xaxis=dict(tickangle=45),
        template="plotly_white",
        legend=dict(title="Year")
    )

    return fig
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
    # print("Unique values in wage column:")
    # print(dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'].unique())
    # print("Wage column statistics:")
    # print(dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'].describe())

    # Filter for high-wage and low-wage occupations
    high_wage = dataframes['skills_62_2333'][dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] > 90000]
    low_wage = dataframes['skills_62_2333'][dataframes['skills_62_2333']['Median annual wage, dollars, 2023[1]'] < 60000]

    # Debugging: Check filtered data
    # print(f"High-wage occupations count: {high_wage.shape[0]}")
    # print(f"Low-wage occupations count: {low_wage.shape[0]}")

    # If no data for either category, return an empty figure
    if high_wage.empty or low_wage.empty:
        # print("Warning: No data available for high-wage or low-wage occupations.")
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



#Occupation Dataset More Analysis
def compare_fastest_growing_occupations(dataframes):
    """
    Compare the fastest growing occupations for 2023–33 dataset, returning Plotly figures.
    
    Parameters:
    dataframes (dict): A dictionary containing the DataFrame 'data_2333'.
    
    Returns:
    tuple: (employment_growth_fig, employment_numbers_fig) as Plotly figures.
    """
    import plotly.express as px
    import plotly.graph_objects as go

    # Extract dataset for 2023–33
    data_2333 = dataframes['occupation_13_14_2333'].sort_values(by="Employment change, percent, 2023–33", ascending=False).head()

    # Bar Graph: Employment Growth Comparison
    employment_growth_fig = go.Figure()

    employment_growth_fig.add_trace(go.Bar(
        x=data_2333["2023 National Employment Matrix title"],
        y=data_2333["Employment change, percent, 2023–33"],
        name="2023–33",
        marker_color="lightcoral"
    ))

    employment_growth_fig.update_layout(
        title="Sectors Where Maximum Growth in Employment 2023–33",
        xaxis_title="Occupation",
        yaxis_title="Employment Percentage Change %",
        xaxis=dict(tickangle=45),
        template="plotly_white"
    )

    # Bar Chart: Employment Numbers

    return employment_growth_fig
def show_max_decline_bar_chart_occupation_15_16_2333(dataframes):
    """
    Show professions predicted to have the maximum decline in employment rate using an inverted bar chart.
    """
    import plotly.graph_objects as go

    # Extract dataset for slowest-growing professions
    data_2333_dec = dataframes['occupation_15_16_2333'].sort_values(
        by="Employment change, percent, 2023–33", ascending=True
    ).head(10)

    # Create bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data_2333_dec["2023 National Employment Matrix title"],
        y=data_2333_dec["Employment change, percent, 2023–33"],  # Negative values
        marker_color="red",
        name="Predicted Decline (2023-33)"
    ))

    # Update layout
    fig.update_layout(
        title="Professions Predicted to Have Maximum Decline (2023-33)",
        xaxis_title="Occupation",
        yaxis_title="Employment Change (%)",
        xaxis=dict(tickangle=45),
        yaxis=dict(range=[min(data_2333_dec["Employment change, percent, 2023–33"]), 0]),  # Ensure Y-axis ends at 0
        template="plotly_white"
    )

    return fig

def show_min_decline_bar_chart_occupation_15_16_2333(dataframes):
    """
    Show professions predicted to have the maximum decline in employment rate using an inverted bar chart.
    """
    import plotly.graph_objects as go

    # Extract dataset for slowest-growing professions
    data_2333_dec = dataframes['occupation_15_16_2333'].sort_values(
        by="Employment change, percent, 2023–33", ascending=False
    ).head(10)

    # Create bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data_2333_dec["2023 National Employment Matrix title"],
        y=data_2333_dec["Employment change, percent, 2023–33"],  # Negative values
        marker_color="blue",
        name="Predicted Decline (2023-33)"
    ))

    # Update layout
    fig.update_layout(
        title="Professions Predicted to Have Minimum Decline (2023-33)",
        xaxis_title="Occupation",
        yaxis_title="Employment Change (%)",
        xaxis=dict(tickangle=45),
        yaxis=dict(range=[min(data_2333_dec["Employment change, percent, 2023–33"]), 0]),  # Ensure Y-axis ends at 0
        template="plotly_white"
    )

    return fig


# These are pre vs post pandemic graphs
def employment_change_by_degree(dataframes):
    # Extract the relevant DataFrames from your processed data
    education_52_1929 = dataframes['education_52_1929']
    education_52_2333 = dataframes['education_52_2333']

    # Inspect column names for debugging
    print("Columns in education_52_1929:", education_52_1929.columns)
    print("Columns in education_52_2333:", education_52_2333.columns)

    # Extract relevant columns
    education_levels = education_52_2333['Typical entry-level education']
    empl_change_2019_29 = education_52_1929['Employment change, percent, 2019-29']
    empl_change_2023_33 = education_52_2333['Percent employment change, 2023-33']  # Correct column name

    # Create a grouped horizontal bar chart
    fig = go.Figure()

    # Add bars for 2019-2029
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=empl_change_2019_29,
            name='Pre-Pandemic (2019-29)',
            orientation='h',
            marker=dict(color='blue', line=dict(color='black', width=1))
        )
    )

    # Add bars for 2023-2033
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=empl_change_2023_33,
            name='Post-Pandemic (2023-33)',
            orientation='h',
            marker=dict(color='orange', line=dict(color='black', width=1))
        )
    )

    # Update layout
    fig.update_layout(
        title='Employment Change by Education Level: 2019 vs 2023',
        xaxis_title='Percent Employment Change (%)',
        yaxis_title='Education Levels',
        barmode='group',
        template='plotly_white',
        legend_title='Period'
    )
    return fig


def median_wage_by_degree(dataframes):
    # Extract relevant DataFrames
    education_52_1929 = dataframes['education_52_1929']
    education_52_2333 = dataframes['education_52_2333']

    # Strip whitespace from column headers
    education_52_1929.columns = education_52_1929.columns.str.strip()
    education_52_2333.columns = education_52_2333.columns.str.strip()

    # Extract data for the plot
    education_levels = education_52_2333['Typical entry-level education']
    median_wage_2019 = pd.to_numeric(education_52_1929['Median annual wage, 2020(1)'], errors='coerce')
    median_wage_2023 = pd.to_numeric(education_52_2333['Median annual wage, dollars, 2023[1]'], errors='coerce')

    # Create a grouped horizontal bar chart
    fig = go.Figure()

    # Add bars for 2019
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=median_wage_2019,
            name='Pre-Pandemic (2019)',
            orientation='h',
            marker=dict(color='blue', line=dict(color='black', width=1))
        )
    )

    # Add bars for 2023
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=median_wage_2023,
            name='Post-Pandemic (2023)',
            orientation='h',
            marker=dict(color='purple', line=dict(color='black', width=1))
        )
    )

    # Update layout
    fig.update_layout(
        title='Median Annual Wage by Education Level: 2019 vs 2023',
        xaxis_title='Median Annual Wage (USD)',
        yaxis_title='Education Levels',
        barmode='group',  # Group bars side by side
        template='plotly_white',
        legend_title='Period',
        title_font=dict(size=16),
        xaxis=dict(tickformat='.2f'),
        yaxis=dict(tickfont=dict(size=12)),
    )
    return fig



def education_distribution_by_degree(dataframes):
    # Extract relevant DataFrames
    education_54_1929 = dataframes['education_54_1929']
    education_54_2333 = dataframes['education_54_2333']

    # Define education levels
    education_levels = [
        "No formal educational credential",
        "High school diploma or equivalent",
        "Some college, no degree",
        "Associate's degree",
        "Bachelor's degree",
        "Master's degree",
        "Doctoral or professional degree",
    ]

    # Value counts for pre- and post-pandemic data
    education_counts_19 = education_54_1929['Typical education needed for entry'].value_counts()
    education_counts_23 = education_54_2333['Typical education needed for entry'].value_counts()

    # Reindex to ensure all levels are included in the specified order
    education_counts_19 = education_counts_19.reindex(education_levels, fill_value=0)
    education_counts_23 = education_counts_23.reindex(education_levels, fill_value=0)

    # Create a grouped bar chart
    fig = go.Figure()

    # Add bars for 2019
    fig.add_trace(
        go.Bar(
            x=education_levels,
            y=education_counts_19.values,
            name='2019',
            marker=dict(color='blue', line=dict(color='black', width=1))
        )
    )

    # Add bars for 2023
    fig.add_trace(
        go.Bar(
            x=education_levels,
            y=education_counts_23.values,
            name='2023',
            marker=dict(color='orange', line=dict(color='black', width=1))
        )
    )

    # Update layout
    fig.update_layout(
        title='Distribution of Typical Education Needed for Entry: Pre-Pandemic vs Post-Pandemic',
        xaxis_title='Education Level',
        yaxis_title='Number of Occupations',
        barmode='group',  # Group bars side by side
        template='plotly_white',
        legend_title='Year',
        title_font=dict(size=16),
        xaxis=dict(tickangle=45, tickfont=dict(size=12)),
        yaxis=dict(tickfont=dict(size=12)),
    )
    return fig


def median_wage_by_degree(dataframes):
    # Extract relevant DataFrames
    education_52_1929 = dataframes['education_52_1929']
    education_52_2333 = dataframes['education_52_2333']

    # Strip whitespace from column headers
    education_52_1929.columns = education_52_1929.columns.str.strip()
    education_52_2333.columns = education_52_2333.columns.str.strip()

    # Extract data for the plot
    education_levels = education_52_2333['Typical entry-level education']
    median_wage_2019 = pd.to_numeric(education_52_1929['Median annual wage, 2020(1)'], errors='coerce')
    median_wage_2023 = pd.to_numeric(education_52_2333['Median annual wage, dollars, 2023[1]'], errors='coerce')

    # Create a grouped horizontal bar chart
    fig = go.Figure()

    # Add bars for 2019
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=median_wage_2019,
            name='Pre-Pandemic (2019)',
            orientation='h',
            marker=dict(color='blue', line=dict(color='black', width=1))
        )
    )

    # Add bars for 2023
    fig.add_trace(
        go.Bar(
            y=education_levels,
            x=median_wage_2023,
            name='Post-Pandemic (2023)',
            orientation='h',
            marker=dict(color='purple', line=dict(color='black', width=1))
        )
    )

    # Update layout
    fig.update_layout(
        title='Median Annual Wage by Education Level: 2019 vs 2023',
        xaxis_title='Median Annual Wage (USD)',
        yaxis_title='Education Levels',
        barmode='group',  # Group bars side by side
        template='plotly_white',
        legend_title='Period',
        title_font=dict(size=16),
        xaxis=dict(tickformat='.2f'),
        yaxis=dict(tickfont=dict(size=12)),
    )
    return fig

#Dan Function working on occupation Factors affecting occupational utilization table 1.12 occupation 
def get_factors_utilization(dataframes, occupation_title, industry_title):
    """
    Retrieves the factors affecting occupational utilization based on the selected
    occupation title and industry title.

    Parameters:
        dataframes (dict): Dictionary of all processed dataframes.
        occupation_title (str): The selected occupation title to filter.
        industry_title (str): The selected industry title to filter.

    Returns:
        str: A formatted string of the factors affecting utilization.
    """
    # Access the relevant DataFrame
    occupation_112_2333 = dataframes["occupation_112_2333"]

    # Filter the DataFrame based on the provided occupation and industry titles
    filtered_df = occupation_112_2333[
        (occupation_112_2333["2023 National Employment Matrix occupation title"] == occupation_title) &
        (occupation_112_2333["2023 National Employment Matrix industry title"] == industry_title)
    ]

    # Check if any data matches the filters
    if filtered_df.empty:
        return f"No factors found for occupation: {occupation_title} and industry: {industry_title}"
    else:
        # Format the factors into a readable string
        factors = "\n".join(filtered_df["Factors affecting occupational utilization"].unique())
        return f"Factors affecting utilization for {occupation_title} in {industry_title}:\n\n{factors}"
    
def get_factors_and_employment_change(dataframes, occupation_title, industry_title):
    """
    Fetches factors affecting occupational utilization and employment change percent
    for the given occupation title and industry title.

    Parameters:
    - dataframes: Dictionary containing the dataframes.
    - occupation_title: Selected occupation title.
    - industry_title: Selected industry title.

    Returns:
    - A string summarizing the factors and employment change percent.
    """
    # Rename columns to align the merge keys
    occupation_112_2333 = dataframes["occupation_112_2333"].rename(
        columns={"2023 National Employment Matrix occupation code": "2023 National Employment Matrix code"}
    )
    occupation_110_2333 = dataframes["occupation_110_2333"]

    # Merge dataframes on the shared key
    joined_df = pd.merge(
        occupation_112_2333,
        occupation_110_2333,
        on="2023 National Employment Matrix code",
        how="inner"
    )

    # Filter for the selected occupation and industry
    filtered_df = joined_df[
        (joined_df["2023 National Employment Matrix occupation title"] == occupation_title) &
        (joined_df["2023 National Employment Matrix industry title"] == industry_title)
    ]

    if filtered_df.empty:
        return f"No data available for {occupation_title} in {industry_title}."

    # Extract the factors and employment change
    factors = filtered_df["Factors affecting occupational utilization"].unique()
    employment_change = filtered_df["Employment change, percent, 2023–33"].iloc[0]

    # Construct the result string
    result = (
        f"Projected employment rate change: {employment_change}%\n\n"
        f"Factors affecting utilization for {occupation_title} in {industry_title}:\n"
        + "\n".join(f"- {factor}" for factor in factors)
    )

    return result

