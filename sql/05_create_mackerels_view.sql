CREATE OR REPLACE VIEW MackerelsCatch AS
SELECT 
    year, 
    area_name AS WhereCaught, 
    fishing_entity AS Country, 
    SUM(tonnes) AS TotalWeight
FROM fishdb.data_source_62248
WHERE common_name LIKE '%Mackerels%' 
  AND year > 2014
GROUP BY year, area_name, fishing_entity, tonnes
ORDER BY tonnes DESC;
