import matplotlib.pyplot as plt
import pandas as pd

# Data for the visualization
data = [
    {"job_title": "Head of Data Platform and Cloud", "salary_year_avg": 221000.0, "company_name": "Palta"},
    {"job_title": "Corporate Audit, AVP – Full Stack Data Scientist", "salary_year_avg": 186928.0, "company_name": "State Street"},
    {"job_title": "Machine Learning Engineer", "salary_year_avg": 186000.0, "company_name": "HEINEKEN"},
    {"job_title": "Senior ML Engineer", "salary_year_avg": 185500.0, "company_name": "Exadel"},
    {"job_title": "Senior Machine Learning Engineer", "salary_year_avg": 166000.0, "company_name": "SmartRecruiters Inc"},
    {"job_title": "Big Data / AI Engineer", "salary_year_avg": 164500.0, "company_name": "Warner Bros. Discovery"},
    {"job_title": "Analytics Engineer", "salary_year_avg": 158500.0, "company_name": "Palta"},
    {"job_title": "Senior Data Scientist (Search)", "salary_year_avg": 157500.0, "company_name": "Allegro"},
    {"job_title": "Data Scientist", "salary_year_avg": 157500.0, "company_name": "Opera"},
    {"job_title": "Data Engineer - Data&AI", "salary_year_avg": 155500.0, "company_name": "Allegro"},
    {"job_title": "Data Engineer - Data Science Hub", "salary_year_avg": 155500.0, "company_name": "Allegro"},
    {"job_title": "Azure Open AI Engineer", "salary_year_avg": 154750.0, "company_name": "Accenture"},
    {"job_title": "Data Engineer - Delivery Experience", "salary_year_avg": 147500.0, "company_name": "Allegro"},
    {"job_title": "Data Engineer", "salary_year_avg": 146000.0, "company_name": "HEINEKEN"},
    {"job_title": "Data Engineer (Python, Hadoop)", "salary_year_avg": 133500.0, "company_name": "Capco"},
    {"job_title": "Data Engineer (Hadoop)", "salary_year_avg": 133500.0, "company_name": "Capco"},
    {"job_title": "Data Engineer (Data Science Hub)", "salary_year_avg": 133500.0, "company_name": "Allegro"},
    {"job_title": "Data Engineer (Data Science Hub)", "salary_year_avg": 133000.0, "company_name": "Allegro"},
    {"job_title": "Data Scientist (S&OP)", "salary_year_avg": 132500.0, "company_name": "Allegro"},
    {"job_title": "Data Scientist (Data Science Hub)", "salary_year_avg": 132500.0, "company_name": "Allegro"}
]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Sort by salary
df = df.sort_values(by="salary_year_avg", ascending=False)

# Create the bar plot
plt.figure(figsize=(10, 8))
bars = plt.barh(df['job_title'], df['salary_year_avg'], color='skyblue')

# Add company name labels to each bar
for bar, company in zip(bars, df['company_name']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f' {company}', va='center', ha='left')

# Add titles and labels
plt.xlabel('Average Yearly Salary (PLN)')
plt.ylabel('Job Title')
plt.title('Top 20 Highest-Paying Data Jobs in Poland (2023)')

# Invert the y-axis to have the highest salary at the top
plt.gca().invert_yaxis()

# Show the plot
plt.show()
