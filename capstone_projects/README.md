# Readme for ABC Company Employee Data Analysis

## Project Overview
This notebook performs preprocessing and exploratory analysis on an employee dataset 

## Preprocessing
- dropped the column college as it contains null values .if we drop the rows ,then information to get more insights may lose.So ,its better to drop coellege column as the analysis not contributing much from that column
- Corrected the 'Height' column by replacing values with random integers between 150 and 180 
- Filled missing salaries by position with the mean salary of that position.

## Key Metrics & Findings
- Total employees analysed: 458

### Top 5 Teams by Employee Count
- New Orleans Pelicans: 19 employees (4.15%)
- Memphis Grizzlies: 18 employees (3.93%)
- Utah Jazz: 16 employees (3.49%)
- Milwaukee Bucks: 16 employees (3.49%)
- New York Knicks: 16 employees (3.49%)

### Position Distribution
- SG: 102 employees
- PF: 100 employees
- PG: 92 employees
- SF: 85 employees
- C: 79 employees

### Predominant Age Group: Not available
-between 21-30 are the predominant age group

### Highest Salary Expenditure
- Team & Position: Los Angeles Lakers (SF)
- Total salary expenditure for that team-position: $31,866,445

### Age vs Salary Correlation
-  correlation (Age, Salary): 0.210
-  correlation around 0.21 indicates a weak positive relationship; salary is not strongly explained by age alone.

## Visualizations Created
- Bar plots for team distribution and position distribution.
- Stacked bar charts for employee positions per team and salary expenditure by team and position.
- Age group bar plot and scatter plot for Age vs Salary by team.

## Insights / Data Story
-  relatively young with a predominant age group noted in the analysis.
- Position distribution shows which roles are more common (SG, PF, PG, SF, C).
- Weak age-salary correlation suggests salary depends more on position, team, experience, or other factors rather than age alone.

