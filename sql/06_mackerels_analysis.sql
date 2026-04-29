SELECT 
    year, 
    Country, 
    MAX(TotalWeight) AS Weight
FROM fishdb.mackerelscatch 
GROUP BY year, Country
ORDER BY year, Weight DESC;
