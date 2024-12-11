import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dataprocessing as dp
import ProjectFileGroup4 as pf
import plotly.graph_objects as go


# Sample DataFrame Placeholder
# Replace this with your actual DataFrame loading process
dataframes = dp.process_and_clean_data()
df = dataframes["skills_64_2333"]
education_levels = df['Typical education needed for entry'].unique()
skills_columns = df.columns[1:]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Education Skills Distribution Pie Chart"),
    html.Label("Select Education Level:"),
    dcc.Dropdown(
        id='education-dropdown',
        options=[{'label': level, 'value': level} for level in education_levels],
        value=education_levels[0]
    ),
    dcc.Graph(id='education-skills-pie-chart')
])

@app.callback(
    Output('education-skills-pie-chart', 'figure'),
    Input('education-dropdown', 'value')
)
def update_pie_chart(selected_education):
    filtered_df = df[df['Typical education needed for entry'] == selected_education]
    values = filtered_df[skills_columns].iloc[0]
    fig = go.Figure(
        go.Pie(
            labels=skills_columns,
            values=values,
            name=f'{selected_education}',
            hovertemplate="<b>%{label}</b><br>Importance: %{value}<extra></extra>"
        )
    )
    fig.update_layout(
        title=f"Skills Distribution for {selected_education}",
        margin=dict(t=50, b=50, l=50, r=50),
        showlegend=True
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)