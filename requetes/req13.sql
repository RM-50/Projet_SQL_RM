#13 Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notes ?
SELECT primaryTitle
FROM title_basics
JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE genres like '%Animation%' 
AND titleType = 'movie'
AND title_ratings.numVotes > 1000
ORDER BY averageRating DESC
LIMIT 10