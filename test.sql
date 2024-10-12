WITH year_counts AS (
    SELECT 
        year,
        SUM(CASE WHEN type = 'birth' THEN 1 ELSE 0 END) AS births,
        SUM(CASE WHEN type = 'death' THEN 1 ELSE 0 END) AS deaths
    FROM records
    GROUP BY year
),
ordered_year_counts AS (
    SELECT
        year,
        births,
        deaths,
        SUM(births - deaths) OVER (ORDER BY year) AS cumulative_change
    FROM year_counts
),
ranked_cumulative AS (
    SELECT 
        year,
        cumulative_change,
        RANK() OVER (ORDER BY cumulative_change DESC, year ASC) AS rank
    FROM ordered_year_counts
)
SELECT 
    year,
    cumulative_change AS count
FROM ranked_cumulative
WHERE rank = 1
ORDER BY year
LIMIT 1;




SELECT 
    year,
    cumulative_change AS count
FROM (
    SELECT 
        year,
        cumulative_change,
        RANK() OVER (ORDER BY cumulative_change DESC, year ASC) AS `rank`
    FROM (
        SELECT
            year,
            births,
            deaths,
            SUM(births - deaths) OVER (ORDER BY year) AS cumulative_change
        FROM 
            (
                SELECT 
                    year,
                    SUM(CASE WHEN type = 'birth' THEN 1 ELSE 0 END) AS births,
                    SUM(CASE WHEN type = 'death' THEN 1 ELSE 0 END) AS deaths
                FROM records
                GROUP BY year
            ) AS yearly_stats
    ) AS cumulative_data
) AS ranked_data
WHERE rank = 1
ORDER BY year;