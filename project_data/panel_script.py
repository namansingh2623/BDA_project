import panel as pn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Enable Panel extensions
pn.extension()

# Convert the data to DataFrames
pre_covid_df = education_53_1929
post_covid_df = education_53_2333

# Education levels (columns to display)
education_levels = pre_covid_df.columns[2:9]

# Occupation labels
Occupation_53_1929 = pre_covid_df['Title Labels'].unique().tolist()

# Create a Select widget for Title Labels
label_selector = pn.widgets.Select(
    name='Label',
    options=Occupation_53_1929,
    value=Occupation_53_1929[0]  # Default value
)

# Function to filter data based on the label_selector
@pn.depends(label_selector)
def filter_professions(selected_label):
    short_dataset = pre_covid_df[pre_covid_df['Title Labels'] == selected_label]
    professions = short_dataset['2019 National Employment Matrix title'].unique().tolist()
    return professions

# Dynamic profession selector
label_selector_profession = pn.widgets.Select(
    name='Profession',
    options=filter_professions(label_selector.value)
)

# Update the profession options dynamically
@pn.depends(label_selector.param.value)
def update_profession_options(selected_label):
    professions = filter_professions(selected_label)
    label_selector_profession.options = professions

# Function to plot the graph
@pn.depends(label_selector.param.value, label_selector_profession.param.value)
def plot_graph(selected_label, selected_profession):
    # Filter data for the selected profession
    x_precovid_1929 = pre_covid_df[pre_covid_df['2019 National Employment Matrix title'] == selected_profession]
    x_postcovid_2333 = post_covid_df[post_covid_df['2023 National Employment Matrix title'] == selected_profession]

    if not x_precovid_1929.empty and not x_postcovid_2333.empty:
        x_precovid_1929_var_list = x_precovid_1929.iloc[0, 2:9].values.tolist()
        x_postcovid_2333_var_list = x_postcovid_2333.iloc[0, 2:9].values.tolist()

        # Plot the line graph
        plt.figure(figsize=(14, 7))
        plt.plot(education_levels, x_precovid_1929_var_list, label='2019', marker='o', color='skyblue', linewidth=2)
        plt.plot(education_levels, x_postcovid_2333_var_list, label='2023', marker='o', color='lightcoral', linewidth=2)

        # Add labels, title, and legend
        plt.title(f"Employment Distribution for '{selected_profession}'\nPre-Covid vs Post-Covid")
        plt.xlabel("Education Level")
        plt.ylabel("Percentage (%)")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    else:
        print("No data available for the selected profession.")

# Panel layout
app = pn.Column(
    pn.Row(
        pn.Column(label_selector, label_selector_profession),
        plot_graph
    )
)

# Serve the Panel app
app.servable()