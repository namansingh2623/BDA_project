import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import dataprocessing as dp
import ProjectFileGroup4 as pf
import plotly.graph_objects as go

# Sample data (replace this with actual DataFrame loading)

dataframes = dp.process_and_clean_data()

df = dataframes["skills_62_2333"]

dataframes = {"skills_62_2333": df}

def skills_pie_chart2(dataframes, title_label, matrix_title):
    df = dataframes["skills_62_2333"]
    skills_columns = df.columns[8:25]

    filtered_df = df[(df['Title Labels'] == title_label) &
                     (df['2023 National Employment Matrix title'] == matrix_title)]

    values = filtered_df[skills_columns].iloc[0]
    
    fig = go.Figure(
        go.Pie(
            labels=skills_columns,
            values=values,
            name=f'{title_label} - {matrix_title}',
            hovertemplate="<b>%{label}</b><br>Value: %{value}<br><extra></extra>"
        )
    )

    fig.update_layout(
        title=f"Skills Distribution for {title_label} - {matrix_title}",
        margin=dict(t=150, b=50, l=50, r=50),
        height=700
    )

    return fig

app = dash.Dash(__name__)

unique_titles = df['Title Labels'].unique()
unique_labels_dict = {
    title: df[df['Title Labels'] == title]['2023 National Employment Matrix title'].unique() 
    for title in unique_titles
}

app.layout = html.Div([
    html.Div([
        html.Label("Select Title Category:"),
        dcc.Dropdown(
            id='title-dropdown',
            options=[{'label': title, 'value': title} for title in unique_titles],
            value=unique_titles[0]
        )
    ]),
    
    html.Div([
        html.Label("Select Specific Title:"),
        dcc.Dropdown(
            id='label-dropdown'
        )
    ]),

    dcc.Graph(id='skills-pie-chart')
])

@app.callback(
    Output('label-dropdown', 'options'),
    Output('label-dropdown', 'value'),
    Input('title-dropdown', 'value')
)
def update_labels(title):
    labels = unique_labels_dict[title]
    return [{'label': label, 'value': label} for label in labels], labels[0]

@app.callback(
    Output('skills-pie-chart', 'figure'),
    Input('title-dropdown', 'value'),
    Input('label-dropdown', 'value')
)
def update_chart(title, label):
    return skills_pie_chart2(dataframes, title, label)

if __name__ == '__main__':
    app.run_server(debug=True)
