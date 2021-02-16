SELECT primaryTitle
FROM title_basics
WHERE titleType LIKE '%movie'
ORDER BY runtimeMinutes DESC
LIMIT 1
