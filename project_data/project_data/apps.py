from dash import Dash, html, dcc
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
    fastest_growing_occupations_fig1, fastest_growing_occupations_fig2 = pf.compare_fastest_growing_occupations(dataframes)
except Exception as e:
    fastest_growing_occupations_fig1 = placeholder_graph("Fastest Growing Occupations (Growth) Not Found")
    fastest_growing_occupations_fig2 = placeholder_graph("Fastest Growing Occupations (Numbers) Not Found")
    print(f"Error generating fastest growing occupations: {e}")

# Initialize Dash app
app = Dash()
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
graph1_md = '''# **Analysis of Employment Distribution by Education Level: 2019 vs 2023**

### Key Observations:

1. **Dominance of High School Diploma or Equivalent**:
   - Both in 2019 and 2023, the **"High school diploma or equivalent"** category has the highest employment distribution percentage.
   - This indicates that a significant portion of the workforce requires at least a high school diploma, making it a critical baseline qualification.

2. **Stability Across Time**:
   - Employment distribution across most education levels appears relatively stable between 2019 and 2023.
   - Only minor changes are observed in the percentages for each category, suggesting consistency in workforce qualifications over time.

3. **Higher Education Levels (Bachelor's and Master's Degrees)**:
   - While higher education categories like **"Bachelor's degree"** and **"Master's degree"** show smaller percentages compared to high school diplomas, their share remains significant.
   - This reflects their importance for specialized or higher-paying roles in the workforce.


From this graph, we can see that the highest employment in 2019 was in the category of **"High school diploma or equivalent."** However, we cannot say for sure that a high school diploma or equivalent degree will always have the highest employment because, for higher degrees, the **minimum requirement** is often a high school diploma or equivalent.

We also need to analyze data from the **occupation perspective** to draw a more accurate conclusion. For instance, if the highest-paying job is that of a CEO, we need to examine the **minimum degree** a CEO typically holds.

From this graph, we can definitely say that to secure a good job, a person **needs at least a high school diploma or equivalent.** '''
graph2_md = '''### **Analysis of Skill Importance for High-Wage vs Low-Wage Occupations**

#### Key Observations:
1. **Core Skills in High-Wage Jobs**:
   - **Adaptability**, **Problem Solving**, **Computers and Information Technology**, and **Critical and Analytical Thinking** are significantly more emphasized in high-wage occupations, reflecting the demand for problem-solving and technology-driven skills.

2. **Low-Wage Job Focus**:
   - Skills like **Customer Service**, **Mechanical**, and **Physical Strength** are more important in low-wage roles, indicating a reliance on repetitive or customer-facing tasks.

3. **STEM Dominance in High-Wage Jobs**:
   - High-wage roles also prioritize **Science**, **Mathematics**, and **Creativity and Innovation**, underscoring the importance of STEM-related skills.

4. **For Any Job**:
   - Problem solving, Interpersonal (good communication), Adaptability, and Detail Oriented are always very important skills to have.

#### Implications:
- **Upskilling in Technology and Critical Thinking** is crucial for transitioning to high-wage jobs.
- While **Customer Service**, and skills relating to physical labor remain key for low-wage roles, a focus on **STEM and leadership skills** can open doors to better paying opportunities.
- The analysis highlights the growing importance of cognitive and technical skills in today’s workforce.
'''
graph3_md = ''' '''
graph4_md = ''' '''
graph5_md = ''' '''


app.layout = html.Div([
    html.H1(children='Get Job Data', style={'textAlign': 'center'}),

    dcc.Markdown(children=intro_md, style={'width': '80%', 'margin': 'auto'}),

    dcc.Graph(figure=pf.generate_correlation_heatmap(dataframes), id='correlation-heatmap'),

    dcc.Graph(figure = pf.employment_dist_by_education_level(dataframes)),
    dcc.Markdown(children=graph1_md, style={'width': '80%', 'margin': 'auto'}),

    dcc.Graph(figure = pf.skill_importance_high_vs_low(dataframes)),
    dcc.Markdown(children=graph2_md, style={'width': '80%', 'margin': 'auto'}),

    


])

if __name__ == '__main__':
    app.run(debug=True)