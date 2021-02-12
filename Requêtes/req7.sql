SELECT originalTitle
FROM title_basics
WHERE tconst=(SELECT knownForTitles
				FROM name_titles
				WHERE nconst=(SELECT nconst
								FROM name_basics
								WHERE primaryName='Olivier Nakache'))