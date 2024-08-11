--1 top paying jobs - What are the top paying data jobs (all roles) in Poland in this dataset?

SELECT
    job_id,
    job_title,
    job_location,
    job_schedule_type,
    salary_year_avg,
    job_posted_date,
    company_dim.name as company_name
FROM 
    job_postings_fact
LEFT JOIN company_dim ON company_dim.company_id = job_postings_fact.company_id
WHERE job_location = 'Poland'
AND salary_year_avg IS NOT NULL
ORDER BY salary_year_avg DESC


--2 A top paying roles - what are the skills for 10 top paying data jobs in Poland?

WITH top_paying_jobs AS ( 
    SELECT
        job_id,
        job_title,
        salary_year_avg,
        company_dim.name as company_name
    FROM 
        job_postings_fact
    LEFT JOIN company_dim ON company_dim.company_id = job_postings_fact.company_id
    WHERE 
    job_location = 'Poland'
    AND salary_year_avg IS NOT NULL
    ORDER BY salary_year_avg DESC
    LIMIT 10
)

SELECT
    top_paying_jobs.*,
    skills
FROM top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY
    salary_year_avg DESC

--2 B top paying roles - what are the skills for top 10 paying Data Analyst roles in Poland?

WITH top_paying_jobs AS (
    SELECT
        job_id,
        job_title,
        salary_year_avg,
        company_dim.name as company_name
    FROM 
        job_postings_fact
    LEFT JOIN company_dim ON company_dim.company_id = job_postings_fact.company_id
    WHERE 
    job_title_short = 'Data Analyst' AND 
    job_location = 'Poland'
    AND salary_year_avg IS NOT NULL
    ORDER BY salary_year_avg DESC
    LIMIT 10
)

SELECT
    top_paying_jobs.*,
    skills
FROM top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY
    salary_year_avg DESC
    
--3A top demanded skills in Poland regardless of data job position (all roles)

SELECT 
    skills,
    COUNT(skills_job_dim.job_id) AS demand_count
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
--WHERE job_location = 'Poland'
AND job_country = 'Poland'
GROUP BY skills
ORDER BY demand_count DESC
LIMIT 10

--3B top demanded skills for Data Analyst position in Poland
SELECT 
    skills,
    COUNT(skills_job_dim.job_id) AS demand_count
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE job_location = 'Poland' AND job_title_short = 'Data Analyst'
GROUP BY skills
ORDER BY demand_count DESC
LIMIT 10

--4 the most optimal skills to learn to get high paying data job (regardless of specific position) in Poland?

WITH skills_demand as (
    SELECT 
        skills_dim.skill_id,
        skills_dim.skills,
        COUNT(skills_job_dim.job_id) AS demand_count
    FROM job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
    WHERE salary_year_avg IS NOT NULL
    AND job_location = 'Poland'
    GROUP BY skills_dim.skill_id
)

, average_salary as (
    SELECT
        skills_job_dim.skill_id,
        ROUND(AVG(salary_year_avg), 0) as avg_salary
    FROM job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
    WHERE salary_year_avg IS NOT NULL
    AND job_location = 'Poland'
    GROUP BY skills_job_dim.skill_id
)

SELECT 
    skills_demand.skill_id,
    skills_demand.skills,
    demand_count,
    avg_salary
FROM
    skills_demand
INNER JOIN average_salary ON average_salary.skill_id = skills_demand.skill_id
WHERE demand_count > 10
ORDER BY
    avg_salary DESC,
    demand_count DESC
    
LIMIT 25

--5 Skills by country - data for worldmap vis

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