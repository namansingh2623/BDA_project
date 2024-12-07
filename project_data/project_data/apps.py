from dash import Dash, html, dcc, callback, Output, Input

import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import nbimporter
import sys
import dataprocessing as dp

import ProjectFileGroup4 as pf

# Function to get and clean dataframes
file_path = "Datasets/2019-29/education.xlsx"
file_path2 = "Datasets/2023-33/education.xlsx"
file_path3 = "Datasets/2019-29/occupation.xlsx"

dataframes = dp.process_and_clean_data(file_path, file_path2, file_path3)

# Access a specific DataFrame
education_53_2333 = dataframes["education_53_2333"]

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

app.layout = html.Div([
    html.H1(children='Get Job Data', style={'textAlign': 'center'}),
    dcc.Graph(figure=pf.generate_correlation_heatmap(dataframe=dataframes['education_53_2333']), id='correlation-heatmap'),
    dcc.Graph(figure = pf.employment_dist_by_education_level(dataframes))
])

if __name__ == '__main__':
    app.run(debug=True)