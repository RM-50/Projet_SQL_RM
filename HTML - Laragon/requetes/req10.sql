#10 Quelles sont les noms et roles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?
SELECT DISTINCT(primaryName), title_principals.category, title_principals.job
FROM name_basics, title_principals
WHERE name_basics.nconst IN(
SELECT nconst
FROM title_principals
WHERE tconst IN(
SELECT tconst
FROM title_basics
WHERE primaryTitle like '%Return of the Jedi'))