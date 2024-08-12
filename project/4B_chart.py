import matplotlib.pyplot as plt
import pandas as pd

# Data
data = [
    {"skills": "bigquery", "avg_salary": 111175},
    {"skills": "airflow", "avg_salary": 111175},
    {"skills": "tableau", "avg_salary": 109006},
    {"skills": "windows", "avg_salary": 108283},
    {"skills": "spark", "avg_salary": 102500},
    {"skills": "flow", "avg_salary": 102500},
    {"skills": "git", "avg_salary": 102500},
    {"skills": "hadoop", "avg_salary": 102500},
    {"skills": "scikit-learn", "avg_salary": 102500},
    {"skills": "looker", "avg_salary": 99979},
    {"skills": "python", "avg_salary": 96073},
    {"skills": "sql", "avg_salary": 86347},
    {"skills": "gcp", "avg_salary": 80492},
    {"skills": "pyspark", "avg_salary": 77757},
    {"skills": "excel", "avg_salary": 74239},
    {"skills": "sap", "avg_salary": 60109},
    {"skills": "powerpoint", "avg_salary": 60109},
    {"skills": "gdpr", "avg_salary": 43200}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
plt.barh(df['skills'], df['avg_salary'], color='skyblue')
plt.xlabel('Average Salary (PLN)')
plt.title('Average Salary by Skill for Data Analysts in Poland')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest salaries on top
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()
