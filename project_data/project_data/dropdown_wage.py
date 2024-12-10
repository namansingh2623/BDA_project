from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dataprocessing as dp


dataframes = dp.process_and_clean_data()

pre_occup_df = dataframes['occupation_11_1929_2']
post_occup_df = dataframes['occupation_11_2333']

print("Columns in post_occup_df:", post_occup_df.columns)

def create_dropdown_layout(pre_occup_df):
    """
    Returns the layout for the dropdown and bar graph.
    """
    occupations = pre_occup_df["2019 National Employment Matrix title"].unique()

    return html.Div([
        html.H1("Median Annual Wage Comparison", style={'textAlign': 'center'}),

        # Dropdown for Occupation selection
        html.Div([
            html.Label("Select Occupation"),
            dcc.Dropdown(
                id='occupation-selector',
                options=[{'label': occupation, 'value': occupation} for occupation in occupations],
                value=occupations[0]  # Default to the first occupation
            )
        ], style={'width': '60%', 'margin': 'auto', 'padding': '10px'}),

        # Graph
        dcc.Graph(id='median-wage-graph')
    ])

def register_dropdown_callbacks(app, pre_occup_df, post_occup_df):
    """
    Registers callbacks for the dropdown and bar graph.
    """
    @app.callback(
        Output('median-wage-graph', 'figure'),
        Input('occupation-selector', 'value')
    )
    def update_graph(selected_occupation):
        # Filter data for the selected occupation
        
        
        pre_occup_df["2019 National Employment Matrix title"] = pre_occup_df["2019 National Employment Matrix title"].str.strip().str.lower()
        post_occup_df["2023 National Employment Matrix title"] = post_occup_df["2023 National Employment Matrix title"].str.strip().str.lower()
        selected_occupation = selected_occupation.strip().lower()
        
        # print("Selected Occupation:", selected_occupation)
        # filtered_post_occup = post_occup_df[post_occup_df["2023 National Employment Matrix title"] == selected_occupation]
        # print("Filtered 2023 Data:", filtered_post_occup)

        
        wage_2019 = pre_occup_df[pre_occup_df["2019 National Employment Matrix title"] == selected_occupation]["Median annual wage, 2020(1)"].values
        wage_2023 = post_occup_df[post_occup_df["2023 National Employment Matrix title"] == selected_occupation]["Median annual wage, dollars, 2023[1]"].values
        
        # print("Wage 2019:", wage_2019)
        # print("Wage 2023:", wage_2023)
        
        # print("Unique titles in pre_occup_df:", len(pre_occup_df["2019 National Employment Matrix title"].unique()))
        # print("Unique titles in post_occup_df:", len(post_occup_df["2023 National Employment Matrix title"].unique()))


        fig = go.Figure()

        # Add bar for 2019
        if len(wage_2019) > 0:
            fig.add_trace(go.Bar(
                x=["2019"],
                y=[wage_2019[0]],
                name="2019",
                marker_color='skyblue'
            ))

        # Add bar for 2023
        if len(wage_2023) > 0:
            fig.add_trace(go.Bar(
                x=["2023"],
                y=[wage_2023[0]],
                name="2023",
                marker_color='lightcoral'
            ))

        # Update layout
        fig.update_layout(
            title=f"Median Annual Wage Comparison: {selected_occupation}",
            xaxis_title="Year",
            yaxis_title="Median Annual Wage ($)",
            template="plotly_white",
            showlegend=True
        )

        return fig