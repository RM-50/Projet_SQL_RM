import sqlite3
import os



def execute(req):
    conn = sqlite3.connect('C:/Users/Raphaël/Documents/devoirs/NSI/NSI - Projet SQL (database)/imdb.db')
    c = conn.cursor()
    c.execute(req)
    for row in c:
        print(row)
    conn.close()
    
#print(execute("select * from title_basics limit 10"))

def existe(repertoire):
    return os.path.isdir(repertoire)

def est_vide(repertoire):
    return os.stat(repertoire).st_size == 0

def liste(repertoire):
    return os.listdir(repertoire)

def lire(repertoire):
    l = liste(repertoire)
    li = []
    os.chdir(repertoire)
    for req in l:
        
        with open(req, 'r') as request:           
                li.append(request.read())   
    dct = {cle:valeur for cle in l
                      for valeur in li} 
    return dct

test = lire('requete')

print(test)




