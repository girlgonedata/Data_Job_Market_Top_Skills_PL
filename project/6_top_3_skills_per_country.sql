--TOP 3 MOST DEMANDED SKILLS PER COUNTRY

WITH RowNumber AS (
SELECT 
    skills_dim.skill_id,
    skills_dim.skills,
    COUNT(skills_job_dim.job_id) AS demand_count,
    job_country,
    ROW_NUMBER() OVER (
        PARTITION BY job_country
        ORDER BY COUNT(skills_job_dim.job_id) DESC 
    ) AS row_order
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
GROUP BY skills_dim.skill_id, job_country
ORDER BY job_country ASC, demand_count DESC
)
SELECT 
    skill_id,
    skills,
    demand_count,
    job_country
    --row_order
FROM RowNumber
WHERE row_order < 4 --to get only 3 top rows per each country

--you can't refer to field aliases in the WHERE clause, so I used CTE instead 
