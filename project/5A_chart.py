import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = [
    {"skills": "tableau", "demand_count": 11, "avg_salary": 131687},
    {"skills": "python", "demand_count": 31, "avg_salary": 119526},
    {"skills": "sql", "demand_count": 31, "avg_salary": 118758},
    {"skills": "spark", "demand_count": 21, "avg_salary": 112729},
    {"skills": "hadoop", "demand_count": 13, "avg_salary": 111046},
    {"skills": "bigquery", "demand_count": 15, "avg_salary": 108056},
    {"skills": "gcp", "demand_count": 26, "avg_salary": 100837},
    {"skills": "scala", "demand_count": 13, "avg_salary": 97643},
    {"skills": "windows", "demand_count": 13, "avg_salary": 91796}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Scatter plot
sns.scatterplot(data=df, x='demand_count', y='avg_salary', hue='skills', palette='viridis', s=100, edgecolor='w')

# Titles and labels
plt.title('Demand vs Average Salary for Data Skills in Poland', fontsize=16)
plt.xlabel('Demand Count (Number of Job Postings)', fontsize=14)
plt.ylabel('Average Salary (PLN)', fontsize=14)
plt.legend(title='Skills', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
