import sqlite3
import os
import tkinter

def execute(req):
    conn = sqlite3.connect('C:/Users/Raphaël/Documents/devoirs/NSI/NSI - Projet SQL (database)/imdb.db')
    #conn = sqlite3.connect('C:/Users/Elève/Documents/Cours/Projet_SQL_RM-main/imdb.db')
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
    if os.path.basename(os.getcwd()) != repertoire:
        l = liste(repertoire)
        os.chdir(repertoire)       
    else:
        os.chdir(os.path.dirname(os.getcwd()))
        l = liste(repertoire)
        os.chdir(repertoire)
    li = []
    requete = ''
    for req in l:
        requete = ''
        with open(req, 'r') as file:
            line = file.readlines()
            for lignes in line[1:]:
                requete += lignes
            li.append([line[0], requete])
    li.sort()
    tab = [0 for i in range(len(l))]
    for i in range(len(tab)):
        tab[i] = [i+1, li[i]]
    dct = {cle:valeur for cle,valeur in tab}
    return dct

def execution(req):
    dico = lire('requetes')
    print(dico[req][0])
    if 'LIMIT' in dico[req][1]:
        execute(dico[req][1])
    else:
        execute(dico[req][1]+ 'LIMIT 10')
    print('-------------------------------------------')

execution(1)
execution(2)
execution(3)
execution(4)
execution(5)
execution(6)
execution(7)

