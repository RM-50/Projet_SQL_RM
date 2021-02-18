import sqlite3
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute("select * from title_basics limit 10")
for row in c:
    print(row)
conn.close()