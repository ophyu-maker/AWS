SELECT 
    year, 
    fishing_entity AS Country, 
    CAST(CAST(SUM(landed_value) AS DOUBLE) AS DECIMAL(38,2)) AS ValuePacificWCSeasCatch
FROM fishdb.data_source_62248
WHERE area_name LIKE '%Pacific%' 
  AND fishing_entity = 'Fiji' 
  AND year > 2000
GROUP BY year, fishing_entity
ORDER BY year;
