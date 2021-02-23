##############################################################
#						Imports								 #
##############################################################

import sqlite3
import os
import tkinter


##############################################################
#					Lecture des requêtes					 #
##############################################################


def execute(req,titre=''):	
	"""
	Execute une requête SQL 'req' et affiche le résultat dans une fenêtre TKinter à l'aide d'une fonction 'afficher_table()'
	
	Arguments:
		req : str correspondant à la requête SQL à executer
		titre : str du titre de la requête 
	"""
	result = ''
	os.chdir(os.path.dirname(os.getcwd()))
	conn = sqlite3.connect('imdb.db')
	#conn = sqlite3.connect('C:/Users/Elève/Documents/Cours/Projet_SQL_RM-main/imdb.db')
	c = conn.cursor()
	c.execute(req)
	for row in c:
		result += '+------------------------+\n|'+ str(row[0]) +'\t\t\t |\n'
	result += '+------------------------+\n'
	afficher_table(result,titre)
	conn.close()

def existe(repertoire):
	"""
	Renvoie True si le répertoire 'repertoire' placé en argument existe.
	"""
	return os.path.isdir(repertoire)

def est_vide(repertoire):
	"""
	Renvoie True si le répertoire 'repertoire' placé en argument est vide.
	"""
	return os.stat(repertoire).st_size == 0

def liste(repertoire):
	"""
	Cette fonction permet de lister le contenu d'un répertoire 'repertoire' placé en argument de la fonction.

	Renvoie:
		Si le répertoire 'repertoire' existe et n'est pas vide :
			La liste des éléments du répertoire 'repertoire'
		Sinon :
			 "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."
	"""
	if existe(repertoire) and not est_vide(repertoire):
    		return os.listdir(repertoire)
	else:
		return "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."
	
def lire(repertoire):
	"""
	Cette fonction permet de lister les requêtes SQL d'un répertoire 'repertoire' placé en paramètre.

	Renvoie:
		Si le répertoire 'repertoire' existe et n'est pas vide :
			Un dictionnaire de type {numéro de la requête(à partir de 1) : 'La requête'} 
		Sinon :
			 "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."
	"""
	if existe(repertoire) and not est_vide(repertoire):
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
	else:
		return "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."
    
def execution():
	"""
	Fait appel a une fonction 'execute()' pour executer l'une des requêtes stockée dans un dictionnaire.
	"""
	repertoire = input('Repertoire contenant les requete ? : ')
	if existe(repertoire) and not est_vide(repertoire):
		dico = lire(repertoire)
		req = int(input("Quelle requete ? (commence à la requête 1, pas 01 ni 0) : "))	
		if 'LIMIT' in dico[req][1]:
			execute(dico[req][1], dico[req][0])
		else:
			execute(dico[req][1] + 'LIMIT 10', dico[req][0])
		print('-------------------------------------------')
	else:
		print("Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe.")

##############################################################
# 						Affichage 							 #
##############################################################


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

##############################################################
#						 Execution							 #
##############################################################
 
execution()
