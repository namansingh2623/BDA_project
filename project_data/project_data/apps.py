from dash import Dash, html, dcc, callback, Output, Input

import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import nbimporter
import sys
import DataProcessing.dataprocessing as dp

from importnb import imports
with imports("ipynb"):
    from ProjectFileGroup4 import generate_correlation_heatmap

# Function to get and clean dataframes
def get_dataframes():
    file_path = "Datasets/2019-29/education.xlsx"
    file_path2 = "Datasets/2023-33/education.xlsx"
    file_path3 = "Datasets/2019-29/occupation.xlsx"
    dataframes = dp.process_and_clean_data(file_path, file_path2, file_path3)
    return dataframes

# Load data
dataframes = get_dataframes()

# Dash app setup
app = Dash()

app.layout = html.Div([
    html.H1(children='Title of Dash App from Naman', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='dropdown-selection',
        options=[
            {'label': 'Correlation Matrix for 1929 Data', 'value': 'education_53_1929'},
        ],
        value='education_53_1929',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    # Generate Matplotlib figure
    fig = generate_correlation_heatmap(dataframes[value])

    # Convert Matplotlib figure to Plotly figure
    plotly_fig = pio.to_json(fig)

    return plotly_fig

if __name__ == '__main__':
    app.run(debug=True)