import sqlite3
import os
import tkinter
import fileinput

def execute(req):
    #conn = sqlite3.connect('C:/Users/Raphaël/Documents/devoirs/NSI/NSI - Projet SQL (database)/imdb.db')
    conn = sqlite3.connect('C:/Users/Elève/Documents/Cours/Projet_SQL_RM-main/imdb.db')
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

#test = lire('requetes')

def execution(dico):
    for cle,valeur in dico.items():
        print(cle)
        if 'LIMIT' in valeur:
            execute(valeur)
        else:
            execute(valeur + 'LIMIT 10')
        print('-------------------------------------------')


#print(test)
#execution(test)

"""def ouverture(r):
    t = [['','']]
    os.chdir('tests')
    for line in fileinput.input('alire.md'):
        if r in line:
            t[0][0] = line
        else:
            print('error')
    fileinput.close()
    return t

#ouverture('#01')""" # Tentatice de ne sais pas vraiment quoi

def choisir_requete(r, rep=lire('requetes')):
    return execution2(rep[r], r)           



def execution2(r, rep):
    print(rep)
    if 'LIMIT' in r:
        execute(r)
    else:
        execute(r + 'LIMIT 10')
    print('-------------------------------------------')

choisir_requete('req18.sql')