import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataprocessing import process_and_clean_data

def load_data():
    """
    Load and process data using the `process_and_clean_data` function.
    Returns:
        dict: Dictionary containing data tables.
    """
    return process_and_clean_data()

def inspect_table(df, table_name):
    """
    Inspect the given DataFrame by displaying basic info.
    Args:
        df (pd.DataFrame): The DataFrame to inspect.
        table_name (str): Name of the table for logging.
    """
    print(f"--- {table_name} ---")
    print(df.info())
    print(df.head())

def process_table(df):
    """
    Display table title, column names, and row data.
    Args:
        df (pd.DataFrame): DataFrame to process.
    """
    table_title = df.iloc[0, 0] 
    print(f"Table Title: {table_title}")
    print("Column Names:", df.columns.tolist())
    print("\nRow Data:")
    print(df.head())


def plot_bar_chart(x, y, title, xlabel, ylabel, color='skyblue'):
    """
    Plot a bar chart.
    Args:
        x (list or pd.Series): Labels for x-axis.
        y (list or pd.Series): Values for y-axis.
        title (str): Chart title.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
        color (str): Color of bars (default: 'skyblue').
    """
    plt.figure(figsize=(10, 6))
    plt.barh(x, y, color=color)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_data_distribution(df, x_col, y_col, title, xlabel, ylabel, color='blue'):
    """
    Plot data distribution for a specific DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        x_col (str): Column name for x-axis.
        y_col (str): Column name for y-axis.
        title (str): Plot title.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
        color (str): Color of the bars.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    plt.barh(df[x_col], df[y_col], color=color)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()
    plt.show()

def main():
    # Load data
    dataframes = load_data()

    # Process and visualize Table 5.1
    table_5_1 = dataframes.get("education_51_2333")
    inspect_table(table_5_1, "Table 5.1")
    process_table(table_5_1)

    # Visualize unemployment rate by educational attainment
    plot_data_distribution(
        table_5_1,
        x_col="Educational attainment",
        y_col="Unemployment rate (%)",
        title="Unemployment Rates by Educational Attainment (2023)",
        xlabel="Unemployment Rate (%)",
        ylabel="Educational Attainment",
        color="skyblue",
    )

    # Process and visualize Table 5.2
    table_5_2 = dataframes.get("education_52_2333")
    inspect_table(table_5_2, "Table 5.2")
    process_table(table_5_2)

    # Employment distribution in 2023
    plot_data_distribution(
        table_5_2,
        x_col="Typical entry-level education",
        y_col="Employment distribution, percent, 2023",
        title="Employment Distribution by Education Level in 2023",
        xlabel="Employment Distribution (%)",
        ylabel="Education Levels",
        color="coral",
    )

    # Employment distribution in 2033
    plot_data_distribution(
        table_5_2,
        x_col="Typical entry-level education",
        y_col="Employment distribution, percent, 2033",
        title="Estimated Employment Distribution by Education Level in 2033",
        xlabel="Estimated Employment Distribution (%)",
        ylabel="Education Levels",
        color="green",
    )

    # Employment change (2023-33)
    plot_data_distribution(
        table_5_2,
        x_col="Typical entry-level education",
        y_col="Percent employment change, 2023-33",
        title="Employment Change by Education Level (2023-33)",
        xlabel="Employment Change (%)",
        ylabel="Education Levels",
        color="blue",
    )

    # Process and visualize Table 5.3
    table_5_3 = dataframes.get("education_53_2333")
    inspect_table(table_5_3, "Table 5.3")
    process_table(table_5_3)

    education_levels = [
        "Less than high school diploma",
        "High school diploma or equivalent",
        "Some college, no degree",
        "Associate's degree",
        "Bachelor's degree",
        "Master's degree",
        "Doctoral or professional degree",
    ]
    total_occupation_data = table_5_3.iloc[:, 2].tolist()[: len(education_levels)]
    plot_bar_chart(
        education_levels,
        total_occupation_data,
        title="Educational Attainment Distribution Percentage (Total, All Occupations, 2023)",
        xlabel="Education Level",
        ylabel="Percentage of Workers",
        color="blue",
    )

    # Process and visualize Table 5.4
    table_5_4 = dataframes.get("education_54_2333")
    inspect_table(table_5_4, "Table 5.4")
    process_table(table_5_4)

if __name__ == "__main__":
    main()
