#chart4b

import matplotlib.pyplot as plt

# Data
skills = [
    "bigquery", "airflow", "tableau", "windows", "spark", "flow", "git", "hadoop", 
    "scikit-learn", "looker", "python", "sql", "gcp", "pyspark", "excel", "sap", 
    "powerpoint", "gdpr"
]
avg_salaries = [
    111175, 111175, 109006, 108283, 102500, 102500, 102500, 102500, 102500, 
    99979, 96073, 86347, 80492, 77757, 74239, 60109, 60109, 43200
]

# Create the bar chart
plt.figure(figsize=(14, 8))

# Create a white-to-red gradient color scheme
norm = plt.Normalize(min(avg_salaries), max(avg_salaries))
colors = plt.cm.Reds(norm(avg_salaries))

bars = plt.barh(skills, avg_salaries, color=colors)
plt.xlabel('Average Yearly Salary (PLN)', fontsize=14)
plt.title('Top-Paying Skills for Data Analysts in Poland', fontsize=18)
plt.gca().invert_yaxis()  # Highest salary at the top

# Adding value labels on the bars
for bar in bars:
    plt.text(bar.get_width() + 2000, bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,.0f}', va='center')

plt.tight_layout()
plt.show()

