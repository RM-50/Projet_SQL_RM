#11 Quels sont les titres des films notes plus de 9 sur 10 avec plus de 10 000 votes ?
SELECT primaryTitle
FROM title_basics
WHERE tconst IN(SELECT tconst
				FROM title_ratings
				WHERE numVotes>'10000' AND averageRating>'9')
