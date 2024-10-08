#chart4a

import matplotlib.pyplot as plt

# Data
skills = [
    "Databricks", "Snowflake", "Azure", "NoSQL", "Bitbucket", "AWS", "MySQL",
    "Power BI", "PostgreSQL", "GDPR", "Tableau", "Looker", "PySpark", "Git",
    "Theano", "MXNet", "SSIS", "DAX", "Pandas", "Oracle", "PyTorch", "Python",
    "SQL", "Terraform", "R"
]
avg_salaries = [
    178732, 162335, 158099, 157750, 155500, 151233, 142375, 140750,
    140667, 132100, 131687, 129903, 128448, 123100, 123064, 123064,
    123000, 123000, 121000, 120575, 119676, 119526, 118758, 118500, 116241
]

# Create the bar chart
plt.figure(figsize=(14, 8))

# Create a white-to-red gradient color scheme
norm = plt.Normalize(min(avg_salaries), max(avg_salaries))
colors = plt.cm.Reds(norm(avg_salaries))

bars = plt.barh(skills, avg_salaries, color=colors)

plt.xlabel('Average Yearly Salary (PLN)', fontsize=14)
plt.title('Top Paying Data Job Skills in Poland', fontsize=18)
plt.gca().invert_yaxis()  # Highest salary at the top

# Adding value labels on the bars
for bar in bars:
    plt.text(bar.get_width() + 2000, bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,.0f}', va='center')

plt.tight_layout()
plt.show()
