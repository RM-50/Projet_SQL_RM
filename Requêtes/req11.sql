SELECT primaryTitle
FROM title_basics
WHERE tconst IN(SELECT tconst
				FROM title_ratings
				WHERE numVotes>'10000' AND averageRating>'9')