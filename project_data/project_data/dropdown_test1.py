from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dataprocessing as dp


dataframes = dp.process_and_clean_data()

pre_occup_df = dataframes['occupation_11_1929']
post_occup_df = dataframes['occupation_11_2333']