#09 Qui a ecrit le scenario du film Taxi sorti en 1998 ?
SELECT primaryName
FROM name_basics
WHERE nconst IN(SELECT writers
				FROM title_writers
				WHERE tconst IN(SELECT tconst
								FROM title_basics
								WHERE primaryTitle='Taxi' and startYear='1998'))
				

											