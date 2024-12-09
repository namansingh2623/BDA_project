from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dataprocessing as dp

dataframes = dp.process_and_clean_data()

# Assuming `dataframes` contains your data
pre_covid_df = dataframes['education_53_1929']
post_covid_df = dataframes['education_53_2333']

# Define column names for education levels
education_levels = pre_covid_df.columns[2:9]

# Unique Title Labels
labels = pre_covid_df['Title Labels'].unique().tolist()
print()
# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Employment Distribution Analysis", style={'textAlign': 'center'}),

    # Dropdown for Label selection
    html.Div([
        html.Label("Select Label"),
        dcc.Dropdown(
            id='label-selector',
            options=[{'label': label, 'value': label} for label in labels],
            value=labels[0]
        )
    ], style={'width': '30%', 'margin': 'auto', 'padding': '10px'}),

    # Dropdown for Profession selection
    html.Div([
        html.Label("Select Profession"),
        dcc.Dropdown(id='profession-selector', options=[], value=None)
    ], style={'width': '60%', 'margin': 'auto', 'padding': '10px'}),

    # Graph
    dcc.Graph(id='employment-distribution-graph')
])


# Callback to update the profession options dynamically based on selected label
@app.callback(
    Output('profession-selector', 'options'),
    Output('profession-selector', 'value'),
    Input('label-selector', 'value')
)
def update_profession_selector(selected_label):
    filtered_df = pre_covid_df[pre_covid_df['Title Labels'] == selected_label]
    professions = filtered_df['2019 National Employment Matrix title'].unique().tolist()
    options = [{'label': prof, 'value': prof} for prof in professions]
    value = professions[0] if professions else None
    return options, value


# Callback to update the graph based on selected label and profession
@app.callback(
    Output('employment-distribution-graph', 'figure'),
    Input('label-selector', 'value'),
    Input('profession-selector', 'value')
)
def update_graph(selected_label, selected_profession):
    # Filter data for the selected label and profession
    pre_covid_filtered = pre_covid_df[pre_covid_df['2019 National Employment Matrix title'] == selected_profession]
    post_covid_filtered = post_covid_df[post_covid_df['2023 National Employment Matrix title'] == selected_profession]

    fig = go.Figure()

    if not pre_covid_filtered.empty and not post_covid_filtered.empty:
        pre_covid_values = pre_covid_filtered.iloc[0, 2:9].values.tolist()
        post_covid_values = post_covid_filtered.iloc[0, 2:9].values.tolist()

        # Add Pre-Covid data
        fig.add_trace(go.Scatter(
            x=education_levels,
            y=pre_covid_values,
            mode='lines+markers',
            name='2019',
            line=dict(color='skyblue', width=2),
            marker=dict(size=8)
        ))

        # Add Post-Covid data
        fig.add_trace(go.Scatter(
            x=education_levels,
            y=post_covid_values,
            mode='lines+markers',
            name='2023',
            line=dict(color='lightcoral', width=2),
            marker=dict(size=8)
        ))

        # Update layout
        fig.update_layout(
            title=f"Employment Distribution for '{selected_profession}'<br>Pre-Covid vs Post-Covid",
            xaxis_title="Education Level",
            yaxis_title="Percentage (%)",
            template="plotly_white"
        )
    else:
        # Add placeholder text if no data is available
        fig.add_annotation(
            text="No data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=20, color="red")
        )
        fig.update_layout(
            title="Employment Distribution",
            template="plotly_white"
        )

    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)