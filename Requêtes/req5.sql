SELECT originalTitle
FROM title_basics
WHERE tconst = (SELECT titleId
				FROM title_akas
				WHERE title='Les Dents de la mer')