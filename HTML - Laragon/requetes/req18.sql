#18 Quels sont les titres des films les plus connus de Sean Connery ?
SELECT primaryTitle
FROM title_basics
WHERE tconst IN(
SELECT knownForTitles
FROM name_titles
JOIN name_basics ON name_titles.nconst = name_basics.nconst
WHERE name_basics.primaryName = 'Sean Connery')