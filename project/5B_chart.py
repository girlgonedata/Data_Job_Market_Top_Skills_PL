import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from the given data
data = {
    'skills': ['Tableau', 'Python', 'SQL', 'Excel'],
    'demand_count': [13, 15, 26, 16],
    'avg_salary': [105408, 94220, 91422, 73800]
}

df = pd.DataFrame(data)

# Set the style and color palette for seaborn
sns.set(style="whitegrid")
palette = sns.color_palette("viridis", n_colors=2)

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create a bar plot for demand_count
sns.barplot(x='skills', y='demand_count', data=df, palette=palette, ax=ax1, label='Demand Count', alpha=0.7)
ax1.set_ylabel('Demand Count', color='blue')
ax1.set_xlabel('Skills')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis to plot avg_salary
ax2 = ax1.twinx()
sns.lineplot(x='skills', y='avg_salary', data=df, marker='o', color='red', ax=ax2, label='Average Salary')
ax2.set_ylabel('Average Salary (PLN)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add title and legends
plt.title('Most Optimal Skills for Data Analysts in Poland (Demand and Average Salary)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show plot
plt.show()
