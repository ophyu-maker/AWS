SELECT 
    year, 
    Country, 
    MAX(TotalWeight) AS Weight
FROM fishdb.mackerelscatch 
GROUP BY year, Country
ORDER BY year, Weight DESC;

SELECT *
FROM fishdb.mackerelscatch
WHERE Country IN ('Japan');
