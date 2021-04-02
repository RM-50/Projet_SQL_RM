#14 Combien de films durent plus de 3 heures ?
SELECT count(tconst)
FROM title_basics
WHERE runtimeMinutes>'180' 
AND titleType LIKE '%movie'