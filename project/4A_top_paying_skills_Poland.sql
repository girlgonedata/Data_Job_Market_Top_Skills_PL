SELECT 
    skills_dim.skills,
    ROUND(AVG(salary_year_avg), 0) as avg_salary
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE salary_year_avg IS NOT NULL 
AND 
job_location = 'Poland'
GROUP BY skills_dim.skills
ORDER BY avg_salary DESC
LIMIT 25
