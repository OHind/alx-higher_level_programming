-- List the number of records with the same score
SELECT score, COUNT(*) as s FROM second_table GROUP BY score ORDER BY score DESC;
