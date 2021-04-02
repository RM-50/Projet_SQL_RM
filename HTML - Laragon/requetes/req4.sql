#04 En quelle annee est sortie le premier film Superman ?
SELECT min(startYear)
FROM title_basics
WHERE titleType='movie' and originalTitle='Superman' 
