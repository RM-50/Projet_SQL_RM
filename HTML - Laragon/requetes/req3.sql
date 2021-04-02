#03 En quelle annee est sortie le film The Godfather ?
SELECT startYear
FROM title_basics
WHERE originalTitle like 'The Godfather%' and titleType='movie'
