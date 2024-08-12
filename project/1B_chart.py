import matplotlib.pyplot as plt
import pandas as pd

# Data for the visualization
data = [

  {
    "job_id": 369283,
    "job_title": "Data Analyst (Delivery Experience Technology & Product)",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "111175.0",
    "job_posted_date": "2023-07-07 09:28:39",
    "company_name": "Allegro"
  },
  {
    "job_id": 876513,
    "job_title": "Data Analyst - Financial Services",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "111175.0",
    "job_posted_date": "2023-01-28 12:19:26",
    "company_name": "Allegro"
  },
  {
    "job_id": 367763,
    "job_title": "Data Analyst",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "111175.0",
    "job_posted_date": "2023-09-05 04:19:21",
    "company_name": "Allegro"
  },
  {
    "job_id": 1240464,
    "job_title": "Data Analyst",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "102500.0",
    "job_posted_date": "2023-01-31 12:15:58",
    "company_name": "Capco"
  },
  {
    "job_id": 1281562,
    "job_title": "Data Analyst (CX Tech)",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "102500.0",
    "job_posted_date": "2023-03-25 11:43:15",
    "company_name": "Allegro"
  },
  {
    "job_id": 470832,
    "job_title": "SAP Finance Data Analyst",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "77017.5",
    "job_posted_date": "2023-12-16 21:11:19",
    "company_name": "Westinghouse Electric Company"
  },
  {
    "job_id": 189127,
    "job_title": "Junior Data Analyst (Campaign Team)",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "75067.5",
    "job_posted_date": "2023-12-22 03:10:55",
    "company_name": "Allegro"
  },
  {
    "job_id": 705215,
    "job_title": "Data Analyst (Pricing)",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "57500.0",
    "job_posted_date": "2023-06-27 20:47:14",
    "company_name": "Allegro"
  },
  {
    "job_id": 67765,
    "job_title": "Junior/Mid/Senior Data Analyst (Pricing)",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "53014.0",
    "job_posted_date": "2023-02-27 21:09:30",
    "company_name": "Allegro"
  },
  {
    "job_id": 282943,
    "job_title": "Junior Data Analyst - e-Xperience 2023",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "53014.0",
    "job_posted_date": "2023-04-18 10:46:01",
    "company_name": "Allegro"
  },
  {
    "job_id": 12599,
    "job_title": "HR Data Analyst",
    "job_location": "Poland",
    "job_schedule_type": "Full-time",
    "salary_year_avg": "43200.0",
    "job_posted_date": "2023-12-16 13:11:25",
    "company_name": "Westinghouse Electric Company"
  }
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
plt.title('Top 20 Highest-Paying Data Analyst in Poland (2023)')

# Show the plot
plt.show()
