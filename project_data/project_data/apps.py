from dash import Dash, html, dcc, callback, Output, Input

import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import nbimporter
import sys
import dataprocessing as dp

import ProjectFileGroup4 as pf


dataframes = dp.process_and_clean_data()

app = Dash()

app.layout = html.Div([
    html.H1(children='Get Job Data', style={'textAlign': 'center'}),
    dcc.Graph(figure=pf.generate_correlation_heatmap(dataframes), id='correlation-heatmap'),
    dcc.Graph(figure = pf.employment_dist_by_education_level(dataframes))
])

if __name__ == '__main__':
    app.run(debug=True)