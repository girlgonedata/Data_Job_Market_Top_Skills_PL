#chart2a

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter

# Job skills data
data = [
    "aws", "azure", "snowflake", "databricks", "gdpr", "looker",
    "sql", "aws", "databricks", "azure", "snowflake", "tableau",
    "python", "sql", "databricks", "hadoop", "spark", "pyspark",
    "nosql", "sql", "azure", "spark", "hadoop",
    "python", "pytorch", "tensorflow",
    "aws", "terraform",
    "python", "sql", "snowflake", "airflow", "looker", "tableau", "power bi",
    "sql", "git",
    "python", "bigquery", "gcp", "pyspark", "tableau",
    "sql", "python", "mysql", "postgresql", "bigquery", "snowflake",
    "aws", "gcp", "spark", "airflow", "pyspark", "github"
]

# Count the frequency of each skill
skill_counts = Counter(data)

# Convert to DataFrame for easier plotting
df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Frequency', y='Skill', data=df, palette='cubehelix')

# Title and labels
plt.title('Top Skills Required for High-Paying Data Jobs in Poland', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Skill', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show plot
plt.show()
