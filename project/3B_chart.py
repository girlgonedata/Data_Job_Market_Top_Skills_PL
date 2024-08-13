#chart3b

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = [
    {"skills": "sql", "demand_count": 131},
    {"skills": "python", "demand_count": 85},
    {"skills": "excel", "demand_count": 73},
    {"skills": "tableau", "demand_count": 56},
    {"skills": "power bi", "demand_count": 46},
    {"skills": "gcp", "demand_count": 36},
    {"skills": "r", "demand_count": 28},
    {"skills": "windows", "demand_count": 24},
    {"skills": "looker", "demand_count": 24},
    {"skills": "azure", "demand_count": 23}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x='demand_count', y='skills', data=df, palette='cubehelix')

# Add titles and labels
plt.title('Most In-Demand Skills for Data Analysts in Poland', fontsize=18)
plt.xlabel('Number of Job Postings', fontsize=14)
plt.ylabel('Skills', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()
