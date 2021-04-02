#15 Quelle est la duree moyenne d’un film ?
SELECT AVG(runtimeMinutes)
FROM title_basics
WHERE titleType LIKE '%movie'