#chart2b

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Sample data
data = [
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "sql"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "python"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "gcp"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "airflow"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "windows"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "tableau"},
    {"job_id": 369283, "job_title": "Data Analyst (Delivery Experience Technology & Product)", "salary_year_avg": 111175.0, "skills": "looker"},
    {"job_id": 876513, "job_title": "Data Analyst - Financial Services", "salary_year_avg": 111175.0, "skills": "sql"},
    {"job_id": 876513, "job_title": "Data Analyst - Financial Services", "salary_year_avg": 111175.0, "skills": "gcp"},
    {"job_id": 876513, "job_title": "Data Analyst - Financial Services", "salary_year_avg": 111175.0, "skills": "windows"},
    {"job_id": 876513, "job_title": "Data Analyst - Financial Services", "salary_year_avg": 111175.0, "skills": "looker"},
    {"job_id": 876513, "job_title": "Data Analyst - Financial Services", "salary_year_avg": 111175.0, "skills": "tableau"},
    {"job_id": 367763, "job_title": "Data Analyst", "salary_year_avg": 111175.0, "skills": "sql"},
    {"job_id": 367763, "job_title": "Data Analyst", "salary_year_avg": 111175.0, "skills": "python"},
    {"job_id": 367763, "job_title": "Data Analyst", "salary_year_avg": 111175.0, "skills": "bigquery"},
    {"job_id": 367763, "job_title": "Data Analyst", "salary_year_avg": 111175.0, "skills": "tableau"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "sql"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "python"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "gcp"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "hadoop"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "spark"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "pyspark"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "scikit-learn"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "excel"},
    {"job_id": 1240464, "job_title": "Data Analyst", "salary_year_avg": 102500.0, "skills": "flow"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "sql"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "python"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "windows"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "looker"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "tableau"},
    {"job_id": 1281562, "job_title": "Data Analyst (CX Tech)", "salary_year_avg": 102500.0, "skills": "git"},
    {"job_id": 470832, "job_title": "SAP Finance Data Analyst", "salary_year_avg": 77017.5, "skills": "sap"},
    {"job_id": 470832, "job_title": "SAP Finance Data Analyst", "salary_year_avg": 77017.5, "skills": "excel"},
    {"job_id": 470832, "job_title": "SAP Finance Data Analyst", "salary_year_avg": 77017.5, "skills": "powerpoint"},
    {"job_id": 189127, "job_title": "Junior Data Analyst (Campaign Team)", "salary_year_avg": 75067.5, "skills": "sql"},
    {"job_id": 189127, "job_title": "Junior Data Analyst (Campaign Team)", "salary_year_avg": 75067.5, "skills": "gcp"},
    {"job_id": 189127, "job_title": "Junior Data Analyst (Campaign Team)", "salary_year_avg": 75067.5, "skills": "looker"},
    {"job_id": 705215, "job_title": "Data Analyst (Pricing)", "salary_year_avg": 57500.0, "skills": "sql"},
    {"job_id": 705215, "job_title": "Data Analyst (Pricing)", "salary_year_avg": 57500.0, "skills": "gcp"},
    {"job_id": 67765, "job_title": "Junior/Mid/Senior Data Analyst (Pricing)", "salary_year_avg": 53014.0, "skills": "sql"},
    {"job_id": 67765, "job_title": "Junior/Mid/Senior Data Analyst (Pricing)", "salary_year_avg": 53014.0, "skills": "gcp"},
    {"job_id": 282943, "job_title": "Junior Data Analyst - e-Xperience 2023", "salary_year_avg": 53014.0, "skills": "sql"},
    {"job_id": 282943, "job_title": "Junior Data Analyst - e-Xperience 2023", "salary_year_avg": 53014.0, "skills": "python"},
    {"job_id": 282943, "job_title": "Junior Data Analyst - e-Xperience 2023", "salary_year_avg": 53014.0, "skills": "gcp"},
    {"job_id": 282943, "job_title": "Junior Data Analyst - e-Xperience 2023", "salary_year_avg": 53014.0, "skills": "pyspark"}
]


# Create a DataFrame
df = pd.DataFrame(data)

# Count the frequency of each skill
skill_counts = df['skills'].value_counts()

# Convert to DataFrame for easier plotting
df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Frequency', y='Skill', data=df, palette='cubehelix')

# Title and labels
plt.title('Skills Required for Top-Paying Data Analyst Jobs in Poland', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Skill', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show plot
plt.show()
