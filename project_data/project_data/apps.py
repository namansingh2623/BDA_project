from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dataprocessing as dp
import ProjectFileGroup4 as pf
import plotly.graph_objects as go
import dropdown_wage as dom
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

try:
    median_wage_by_degree_fig = pf.median_wage_by_degree(dataframes)
except Exception as e:
    median_wage_by_degree_fig = placeholder_graph("median_wage_by_degree_fig Graph Not Found")
    print(f"Error generating median_wage_by_degree_fig graph: {e}")
try:
    inflation_adjusted_median_wage_comparison_fig = pf.inflation_adjusted_median_wage_comparison(dataframes, inflation_rate=1.2)
except Exception as e:
    inflation_adjusted_median_wage_comparison_fig = placeholder_graph("inflation_adjusted_median_wage_comparison graph nopt found")
    print(f"Error generating inflation_adjusted_median_wage_comparison graph: {e}")

# Intro and markdown texts
intro_md = '''
- In this project we tend to analyise what kind of profession is required for the students in the future. 
- As per a research, there are people who do not have a clear perspective of what they want to do in the future and what is their carrer path. 
- We plan to analyse the data from the job market before and post pandemic and to help students get a better understand of what kind of proffesion they can pursue and what skill are required for them excel in that profession.


For instance as per these research, 
# Career Aspirations of Students Aged 18 or Below

Understanding how many young individuals know what they want to do when they grow up varies across surveys and studies. Here are some key findings:

## Key Statistics

- **Junior Achievement and EY Survey (2017)**:  
  This survey of 1,000 teenagers aged 13 to 17 found that **91% believed they knew the career they wanted to pursue**.  
  [Source: Payscale](https://www.payscale.com/career-advice/teenager-career-choice-91-percent-teens-think-know-career-want/?utm_source=chatgpt.com)

- **ECMC Group Study (2022)**:  
  In a study involving high school students:
  - **75% reported having a specific career in mind.**
  - **74% felt it was important to have their career plans determined by the time they graduated high school.**  
  [Source: The Journal](https://thejournal.com/articles/2022/05/19/national-study-high-schoolers-eyeing-career-and-workforce-landscape-when-deciding-their-futures.aspx?utm_source=chatgpt.com)

- **OECD PISA 2022 Findings**:  
  The Programme for International Student Assessment (PISA) 2022 reported:
  - **Two in five 15-year-old students across OECD countries lacked clear career plans.**  
  [Source: OECD iLibrary](https://www.oecd-ilibrary.org/education/teenage-career-uncertainty_e89c3da9-en?utm_source=chatgpt.com)

## Summary
While a significant majority of teenagers express confidence in their career aspirations, a substantial portion remain uncertain. These findings underscore the importance of career guidance and exploration programs to help young individuals make informed decisions about their futures.


With our project we plan on creating a 360 degree view of the job market and the skills required for the students to excel in that profession along with the education that is required and the trend of the education and the job market till 2033. 
'''

graph1_md = '''
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

graph3_md = '''
Insights: 
- We are able to analyze patterns across professions
- Finding that "Bachelor's degree" and "Master's degree" having strong correlation might suggest a profession group that values higher education
- Business and Financial Operations Occupations, Healthcare Practitioners and Technical Occupations, and Computer and Mathematical Occupations have 2023 wages that are roughly equal to inflation-adjusted 2019 wages.
- Educational Instruction and Library Occupations, Personal Care and Service Occupations, and Food Preparation and Serving Related Occupations have 2023 wages below their inflation-adjusted 2019 counterparts.
'''
graph4_md ='''
Insights:

- Legal Occupations and Management Occupations exhibit higher 2023 wages than inflation-adjusted 2019 wages, reflecting their resilience and high demand in the labor market.
Educational Instruction and Library Occupations, Personal Care and Service Occupations, and Food Preparation and Serving Occupations show 2023 wages below inflation-adjusted 2019 levels
- Food Preparation, Building and Grounds Cleaning, and Personal Care occupations face the greatest economic pressure, with wages struggling to keep up with inflation.
- STEM fields (e.g., Computer, Mathematical, and Engineering Occupations) maintain stable wages in real terms, underscoring their resilience and continuous demand.
- Healthcare Occupations: A Mixed Picture: Healthcare Practitioners fare better with stable real wages, while Healthcare Support Occupations lag behind, showing disparities within the same sector.

'''


pre_covid_df = dataframes['education_53_1929']
post_covid_df = dataframes['education_53_2333']

# Define column names for education levels
education_levels = pre_covid_df.columns[2:9]

# Unique Title Labels
labels = pre_covid_df['Title Labels'].unique().tolist()


pre_occup_df = dataframes['occupation_11_1929']
post_occup_df = dataframes['occupation_11_2333']

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])




app.layout = html.Div([
    html.Div([
        html.H1(children='Employment and Career Insights Project', style={'textAlign': 'center'}),
        dcc.Markdown(children=intro_md, style={'width': '80%'}),
    ]),
    # Correlation Heatmap
    html.Div([

        html.H1(children='Heatmap of Education Level', style={'textAlign': 'center'}),
        dcc.Graph(figure=correlation_heatmap, id='correlation-heatmap', style={'width': '60%', 'margin': 'auto'}),
        dcc.Markdown(children=graph3_md, style={'width': '80%'}),
    ]),
    html.Div([
        html.H2("Lets see what Degree does most Employees ", style={'textAlign': 'center','margin-top':'70px'}),
        html.H2("have who are working in this profession", style={'textAlign': 'center','margin-top':'20px'}),
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
    # Employment Distribution by Education Level
    html.Div([
        html.H1(children='# Employment Distribution by Education Level (2019 vs 2023)', style={'textAlign': 'center','margin-top':'70px'}),
        dcc.Graph(figure=employment_dist, id='employment-dist', style={'width': '80%', 'margin': 'auto'}),
        dcc.Markdown(children=graph1_md, style={'width': '80%', 'margin': 'auto'}),
    ]),
    # Employment Prediction Change by Education Level
    html.Div([
        html.H1(children='Employment Prediction Change by Education Level (1929-2033)', style={'textAlign': 'center','margin-top':'70px'}),
        dcc.Graph(figure=emp_pred_change, id='emp-pred-change', style={'width': '80%', 'margin': 'auto'}),
    ]),

    # Fastest Growing Occupations
    html.Div(style={'height': '200px'}),
    html.Div([
        html.H1(children='Fastest Growing Occupations', style={'textAlign': 'center','margin-top':'30px'}),
        dcc.Graph(figure=fastest_growing_occupations_fig, id='fastest-growing-occupations', style={'width': '80%', 'margin': 'auto'}),
    ]),

    # Skill Importance in High-Wage vs Low-Wage Jobs
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

    # DANIAL COL
    html.Div(style={'height': '200px'}),
    html.Div([
        # Section for Factors Affecting Occupational Utilization**
        html.Div([
            html.H1("Factors Affecting Occupational Utilization", style={'textAlign': 'center', 'margin-top': '50px'}),

            # Dropdown for Occupation Selection
            html.Div([
                html.Label("Select Occupation"),
                dcc.Dropdown(
                    id='occupation-title-selector',
                    options=[{'label': title, 'value': title} for title in
                             dataframes["occupation_112_2333"][
                                 "2023 National Employment Matrix occupation title"].unique()],
                    value=None,
                    placeholder="Select an Occupation"
                )
            ], style={'width': '50%', 'margin': 'auto', 'padding': '10px'}),

            # Dropdown for Industry Selection
            html.Div([
                html.Label("Select Industry"),
                dcc.Dropdown(
                    id='industry-title-selector',
                    options=[],
                    value=None,
                    placeholder="Select an Industry"
                )
            ], style={'width': '50%', 'margin': 'auto', 'padding': '10px'}),

            # Display Area for Factors
            html.Div(id='factors-display',
                     style={'width': '80%', 'margin': 'auto', 'padding': '20px', 'textAlign': 'center',
                            'fontSize': '16px'})
        ]),
        html.Div(style={'height': '75px'}),
        # end of factors section

        html.Div([
            dcc.Graph(figure=skill_importance, id='skill-importance', style={'width': '80%', 'margin': 'auto'}),
            dcc.Markdown(children=graph2_md, style={'width': '80%', 'margin': 'auto'}),
        ]),
    ]),

    # Employment Distribution Analysis
    html.Div([
        html.H1("Employment Distribution Analysis", style={'textAlign': 'center'}),
        dcc.Graph(figure=median_wage_by_degree_fig, id='skill-importance-graph',
                  style={'width': '80%', 'margin': 'auto'}),
    ]),

    html.Div(style={'height': '200px'}),
    
    
    dom.create_dropdown_layout(pre_occup_df),
    dom.register_dropdown_callbacks(app, pre_occup_df, post_occup_df),
    
    #Inflation adjusted median annual wage comparison
    html.Div([
        dcc.Graph(figure=inflation_adjusted_median_wage_comparison_fig, id='inflation_adjusted_median_wage_comparison', style={'width': '80%', 'margin': 'auto'}),
        dcc.Markdown(children=graph4_md, style={'width': '80%', 'margin': 'auto'})
    ])


    #leave this at the bottom, add any sections above this
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
# Callback to update industries based on selected occupation
@app.callback(
    Output('industry-title-selector', 'options'),
    Output('industry-title-selector', 'value'),
    Input('occupation-title-selector', 'value')
)
def update_industry_selector(selected_occupation):
    if not selected_occupation:
        return [], None

    filtered_df = dataframes["occupation_112_2333"][
        dataframes["occupation_112_2333"]["2023 National Employment Matrix occupation title"] == selected_occupation
    ]
    industries = filtered_df["2023 National Employment Matrix industry title"].unique()
    options = [{'label': industry, 'value': industry} for industry in industries]
    return options, None
# Callback to display factors affecting occupational utilization
@app.callback(
    Output('factors-display', 'children'),
    Input('occupation-title-selector', 'value'),
    Input('industry-title-selector', 'value')
)
def display_factors_and_employment_change(selected_occupation, selected_industry):
    if not selected_occupation or not selected_industry:
        return "Please select both an occupation and an industry to view the factors and employment change."

    # Call the function from the functions file
    try:
        result = pf.get_factors_and_employment_change(
            dataframes, selected_occupation, selected_industry
        )
    except Exception as e:
        return f"Error: {e}"

    return html.Div([
        html.Pre(result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
    ])



if __name__ == '__main__':
    app.run(debug=True)