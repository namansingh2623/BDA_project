from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dataprocessing as dp
import ProjectFileGroup4 as pf
import plotly.graph_objects as go


# Function to generate placeholder graph
def placeholder_graph(message="Graph not found"):
    return go.Figure().add_annotation(
        text=message,
        xref="paper", yref="paper",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=20, color="red")
    )


# Process and clean data
try:
    dataframes = dp.process_and_clean_data()
except Exception as e:
    dataframes = None
    print(f"Error processing data: {e}")

# Generate graphs with error handling
try:
    correlation_heatmap = pf.generate_correlation_heatmap(dataframes)
except Exception as e:
    correlation_heatmap = placeholder_graph("Correlation Heatmap Not Found")
    print(f"Error generating correlation heatmap: {e}")

try:
    employment_dist = pf.employment_dist_by_education_level(dataframes)
except Exception as e:
    employment_dist = placeholder_graph("Employment Distribution Not Found")
    print(f"Error generating employment distribution: {e}")

try:
    emp_pred_change = pf.emp_pred_chang_by_education_1929_2333(dataframes)
except Exception as e:
    emp_pred_change = placeholder_graph("Employment Prediction Change Not Found")
    print(f"Error generating employment prediction change: {e}")

try:
    skill_importance = pf.skill_importance_high_vs_low(dataframes)
except Exception as e:
    skill_importance = placeholder_graph("Skill Importance Graph Not Found")
    print(f"Error generating skill importance graph: {e}")

try:
    fastest_growing_occupations_fig = pf.compare_fastest_growing_occupations(dataframes)
except Exception as e:
    fastest_growing_occupations_fig = placeholder_graph("Fastest Growing Occupations Graph Not Found")
    print(f"Error generating fastest growing occupations graph: {e}")

try:
    max_predicted_decline_occupations_fig = pf.show_max_decline_bar_chart_occupation_15_16_2333(dataframes)
except Exception as e:
    fastest_growing_occupations_fig = placeholder_graph("Fastest Growing Occupations Graph Not Found")
    print(f"Error generating fastest growing occupations graph: {e}")

try:
    min_predicted_decline_occupations_fig = pf.show_min_decline_bar_chart_occupation_15_16_2333(dataframes)
except Exception as e:
    fastest_growing_occupations_fig = placeholder_graph("Fastest Growing Occupations Graph Not Found")
    print(f"Error generating fastest growing occupations graph: {e}")

# Intro and markdown texts
intro_md = '''
# Employment and Career Insights Project

This project analyzes job market trends before and after the pandemic, offering insights into education requirements, skill importance, and professions projected to grow or decline. The aim is to help students make informed career decisions by understanding industry demands.

### Key Objectives:
- Analyze job market trends between 2019 and 2023.
- Identify the fastest and slowest growing occupations.
- Understand the skills required for high-wage and low-wage jobs.
- Compare employment distribution by education level.
'''

graph1_md = '''
# Employment Distribution by Education Level (2019 vs 2023)

### Insights:
1. **High school diploma or equivalent** has the highest employment distribution.
2. Specialized degrees (Bachelor's, Master's) are critical for high-paying roles.
3. Stability in education-level employment distribution between 2019 and 2023.
'''

graph2_md = '''
# Skill Importance in High-Wage vs Low-Wage Jobs

### Insights:
- High-wage jobs prioritize **STEM skills** and **critical thinking**.
- Low-wage jobs focus on **customer service** and **manual skills**.
- Core skills like adaptability and problem-solving are essential for all jobs.
'''


graph3_md='''
###  Insights:
- Adjacent education levels (e.g., "High school diploma" and "Some college, no degree") tend to correlate positively, reflecting the natural progression of education.
- Higher education levels (e.g., "Bachelor's degree," "Master's degree," "Doctoral degree") tend to show moderate positive correlations with each other, likely representing professions that value advanced education.
- Lower levels (e.g., "High school diploma" and "Some college, no degree") also correlate positively, reflecting professions requiring less formal education.
'''


pre_covid_df = dataframes['education_53_1929']
post_covid_df = dataframes['education_53_2333']

# Define column names for education levels
education_levels = pre_covid_df.columns[2:9]

# Unique Title Labels
labels = pre_covid_df['Title Labels'].unique().tolist()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        html.H1(children='Employment and Career Insights Project', style={'textAlign': 'center'}),
        dcc.Markdown(children=intro_md, style={'width': '80%', 'margin': 'auto'}),
    ]),

    # Employment Distribution by Education Level
    html.Div([
        html.H1(children='Employment Distribution by Education Level',
                style={'textAlign': 'center', 'margin-top': '70px'}),
        dcc.Graph(figure=employment_dist, id='employment-dist', style={'width': '80%', 'margin': 'auto'}),
        dcc.Markdown(children=graph1_md, style={'width': '80%', 'margin': 'auto'}),
    ]),
    
    # Correlation Heatmap
    html.Div([
        html.H1(children='Heatmap of Education Level', style={'textAlign': 'center', 'margin-top': '70px'}),
        dcc.Graph(figure=correlation_heatmap, id='correlation-heatmap', style={'width': '60%', 'margin': 'auto'}),
        dcc.Markdown(children=graph3_md, style={'width': '80%', 'margin': 'auto'}),
    ]),

    # Employment Prediction Change by Education Level
    html.Div([
        html.H1(children='Employment Prediction Change by Education Level (1929-2033)',
                style={'textAlign': 'center', 'margin-top': '70px'}),
        dcc.Graph(figure=emp_pred_change, id='emp-pred-change', style={'width': '80%', 'margin': 'auto'}),
    ]),
    html.Div([
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
    ]),
    # Fastest Growing Occupations
    html.Div([
        html.H1(children='Fastest Growing Occupations', style={'textAlign': 'center', 'margin-top': '30px'}),
        dcc.Graph(figure=fastest_growing_occupations_fig, id='fastest-growing-occupations',
                  style={'width': '80%', 'margin': 'auto'}),
    ]),
    # # Skill Importance in High-Wage vs Low-Wage Jobs
    html.Div([
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H2(
                            "Maximum Occupation Decline Trend as Predicted in 2033",
                            style={'textAlign': 'center', 'margin-top': '30px'}
                        ),
                        dcc.Graph(
                            figure=max_predicted_decline_occupations_fig,
                            id='max_occupation_decline',
                            style={'margin': 'auto'}
                        ),
                    ]),
                    width=6  # Use half the row's width
                ),
                dbc.Col(
                    html.Div([
                        html.H2(
                            "Minimum Occupation Decline Trend as Predicted in 2033",
                            style={'textAlign': 'center', 'margin-top': '30px'}
                        ),
                        dcc.Graph(
                            figure=min_predicted_decline_occupations_fig,
                            id='min_occupation_decline',
                            style={'margin': 'auto'}
                        ),
                    ]),
                    width=6  # Use half the row's width
                ),
            ],
            justify="center",  # Align the columns in the center
            style={'margin-top': '30px'}
        )
    ]),
    html.Div([
        dcc.Graph(figure=skill_importance, id='skill-importance', style={'width': '80%', 'margin': 'auto'}),
        dcc.Markdown(children=graph2_md, style={'width': '80%', 'margin': 'auto'}),
    ]),


])


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


if __name__ == '__main__':
    app.run(debug=True)
