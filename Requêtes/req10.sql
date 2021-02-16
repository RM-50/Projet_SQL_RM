SELECT name_basics.primaryName, category, job
FROM title_principals, name_basics
WHERE tconst IN(SELECT tconst
				FROM title_basics
				WHERE primaryTitle like '%Return of the Jedi')