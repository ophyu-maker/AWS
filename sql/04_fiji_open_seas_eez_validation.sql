WITH open_seas AS (
    SELECT 
        year,
        CAST(CAST(SUM(landed_value) AS DOUBLE) AS DECIMAL(38,2)) AS ValueOpenSeasCatch
    FROM fishdb.data_source_62248
    WHERE area_name IS NULL
      AND fishing_entity = 'Fiji'
      AND year > 2000
    GROUP BY year
),
eez AS (
    SELECT 
        year,
        CAST(CAST(SUM(landed_value) AS DOUBLE) AS DECIMAL(38,2)) AS ValueEEZCatch
    FROM fishdb.data_source_62248
    WHERE area_name LIKE '%Fiji%'
      AND fishing_entity = 'Fiji'
      AND year > 2000
    GROUP BY year
),
combined AS (
    SELECT 
        year,
        CAST(CAST(SUM(landed_value) AS DOUBLE) AS DECIMAL(38,2)) AS ValueEEZAndOpenSeasCatch
    FROM fishdb.data_source_62248
    WHERE (area_name LIKE '%Fiji%' OR area_name IS NULL)
      AND fishing_entity = 'Fiji'
      AND year > 2000
    GROUP BY year
)
SELECT
    c.year,
    o.ValueOpenSeasCatch,
    e.ValueEEZCatch,
    CAST((o.ValueOpenSeasCatch + e.ValueEEZCatch) AS DECIMAL(38,2)) AS SumOfOpenSeasAndEEZ,
    c.ValueEEZAndOpenSeasCatch,
    CASE
        WHEN ROUND(ABS((o.ValueOpenSeasCatch + e.ValueEEZCatch) - c.ValueEEZAndOpenSeasCatch), 2) <= 0.01
        THEN 'MATCH'
        ELSE 'NOT MATCH'
    END AS Verification
FROM combined c
LEFT JOIN open_seas o 
    ON c.year = o.year
LEFT JOIN eez e 
    ON c.year = e.year
ORDER BY c.year;
