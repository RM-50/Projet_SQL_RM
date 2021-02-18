import sqlite3
import os
import tkinter


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
    tab = [0 for i in range(len(l))]
    for i in range(len(tab)):
        tab[i] = [l[i], li[i]]
    dct = {cle:valeur for cle,valeur in tab} 
    return dct

test = lire('requete')

def execution(dico):
    for cle,valeur in dico.items():
        print(cle)
        if 'LIMIT' in valeur:
            execute(valeur)
        else:
            execute(valeur + 'LIMIT 10')
        print('-------------------------------------------')


#print(test)
execution(test)

