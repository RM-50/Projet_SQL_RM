import sqlite3
import os
import tkinter

def execute(req,titre=''):	
	result = ''
	conn = sqlite3.connect('C:/Users/Raphaël/Documents/devoirs/NSI/NSI - Projet SQL (database)/imdb.db')
	#conn = sqlite3.connect('C:/Users/Elève/Documents/Cours/Projet_SQL_RM-main/imdb.db')
	c = conn.cursor()
	c.execute(req)
	for row in c:
		result += '+------------------------+\n|'+ str(row[0]) +'\t\t\t |\n'
	result += '+------------------------+\n'
	afficher_table(result,titre)
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

def execution():
	req = int(input("Quelle requête ? (commence à la requête 1, pas 01 ni 0) : "))
	dico = lire('requetes')
	if 'LIMIT' in dico[req][1]:
		execute(dico[req][1], dico[req][0])
	else:
		execute(dico[req][1] + 'LIMIT 10', dico[req][0])
	print('-------------------------------------------')

"""execution(1)
execution(2)
execution(3)
execution(4)
execution(5)
execution(6)
execution(7)
"""

#####


def afficher_table(table, titre ="", debut = 1, fin = None):
	"""
	Affiche une table.
	Cette fonction était demandée dans le sujet.
	On peut avoir un affichage en console ou dans une fenêtre tkinter
	Cependant, on la redéfini ci-dessous.
	Auteurs: M CHOUCHI
	Arguments:
		table: une liste de tuples
		titre: str du titre à afficher avant la table
		debut: indice de la première ligne que l'on veut afficher
		fin: indice de la dernière ligne que l'on veut afficher
			si fin est à None, on affiche jusqu'à la dernière ligne
	Renvoi:
		rien
	"""
	if titre != "":
		titre += "\n\n"
	#print(titre + texte_table(table, debut, fin))
	affichage(titre + table, titre)


def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	dans une fenêtre tkinter
	Auteurs: M CHOUCHI
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()

 
execution()
