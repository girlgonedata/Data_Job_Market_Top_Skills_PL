#chart3a

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for visualization
data = {
    "skills": ["sql", "python", "azure", "aws", "spark", "excel", "java", "gcp", "tableau", "power bi"],
    "demand_count": [7500, 7295, 3701, 3459, 2547, 2406, 1958, 1939, 1807, 1702]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Create a bar plot
sns.barplot(x='demand_count', y='skills', data=df, palette='cubehelix')

# Add titles and labels
plt.title('Most In-Demand Data Skills in the Polish Data Job Market', fontsize=16)
plt.xlabel('Demand Count', fontsize=14)
plt.ylabel('Skills', fontsize=14)

# Show the plot
plt.show()
