SELECT count(tconst)
FROM title_basics
WHERE runtimeMinutes>'180' 
AND titleType LIKE '%movie'