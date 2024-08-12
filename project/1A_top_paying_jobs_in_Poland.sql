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
