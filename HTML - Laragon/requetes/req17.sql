#17 Quels sont les 5 films les plus longs ?
SELECT primaryTitle
FROM title_basics
WHERE titleType LIKE '%movie'
ORDER BY runtimeMinutes DESC
LIMIT 5