#12 Quelle sont les 5 comedies romantiques les mieux notees ?
SELECT primaryTitle
FROM title_basics
JOIN title_ratings ON title_basics.tconst = title_ratings.tconst
WHERE genres like '%Comedy%' AND genres like '%Romance%'
ORDER BY averageRating DESC
LIMIT 5