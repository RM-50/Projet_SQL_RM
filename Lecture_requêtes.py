import sqlite3
import os



def execute(req):
    conn = sqlite3.connect('imdb.db')
    c = conn.cursor()
    c.execute(req)
    for row in c:
        print(row)
    conn.close()
    
#print(execute("select * from title_basics limit 10"))

def existe(repertoire):
    return os.path.isdir(repertoire)

print(existe('requete'))