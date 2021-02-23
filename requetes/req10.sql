#10 Quelles sont les noms et roles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?
SELECT name_basics.primaryName, category, job
FROM title_principals, name_basics
WHERE tconst IN(SELECT tconst
				FROM title_basics
				WHERE primaryTitle like '%Return of the Jedi')