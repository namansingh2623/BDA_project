
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

import plotly.graph_objects as go
import pandas as pd

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


# Adding comment  to check if I can merge or not 
