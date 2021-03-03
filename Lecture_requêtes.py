""" 
IMPORTANT : Placer le répertoire contenant les requêtes et la base de donnée 'imdb.db' dans le même répertoire que ce fichier python.

# Sur GitHub, la tabulation est de 8 espaces et je n'arrive pas à le changer ainsi il peut y avoir des morceaux de codes qui semblent étranges, notamment les commentaires.
Si possible, lire le document avec une tabulation de 4 espaces pour une meilleure lisisbilité.
"""

##############################################################
#						Imports								 #
#############################################################

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
		for j in range(len(row)):
			result += '+------------------------'
		result += '+\n|'
		for i in range(len(row)):
			result += str(row[i]) +'\t\t\t '+i*' '+'|'
		result +='\n'
	for k in range(len(row)):
		result += '+------------------------'
	result += '+\n'
	afficher_table(result,titre)
	conn.close()

##################################################################################################################################################

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

##################################################################################################################################################


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

##################################################################################################################################################

def lire(repertoire):
	"""
	Cette fonction permet de lister les requêtes SQL d'un répertoire 'repertoire' placé en paramètre.

	Renvoie:
		Si le répertoire 'repertoire' existe et n'est pas vide :
			Un dictionnaire de type {numéro de la requête(à partir de 1) : 'La requête'} 
		Sinon :
			 "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."
	"""
	if existe(repertoire) and not est_vide(repertoire): 			# test la présence du répertoire 'repertoire' et son contenu
		if os.path.basename(os.getcwd()) != repertoire: 			# test si le repertoire actuel est different du repertoire 'repertoire'
			l = liste(repertoire)									# Si oui, se placer dans le repertoire 'repertoire' et le lister
			os.chdir(repertoire)       							
		else:						
			l = liste(os.path.dirname(os.getcwd()))					# Sinon, lister le repertoire actuel
		li = []
		requete = ''
		for req in l:
			requete = ''
			with open(req, 'r') as file:                            # Ouvre et lit toutes les requêtes du répertoire requête une à une et les place dans une liste de liste.
				line = file.readlines()								# Chaque sous-liste contient comme premier élément le titre de la requête et la requête elle-même comme second élément
				for lignes in line[1:]:
					requete += lignes
				li.append([line[0], requete])
		li.sort()													# Trier les requêtes dans l'ordre croissant, cela va nous être utile par la suite
		tab = [0 for i in range(len(l))]
		for i in range(len(tab)):									# Creer une liste de liste contenant chacune un entier > 0 et une liste (une sous-liste vue précédemment)
			tab[i] = [i+1, li[i]]
		dct = {cle:valeur for cle,valeur in tab}					# Convertit le tableau 'tab' en dictionnaire :
		return dct													# Clé : entier > 0   ; Valeur : liste de type [titre de la requête, requête elle-même]	
	else:
		return "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."

##################################################################################################################################################

def execution():
	"""
	Fait appel a une fonction 'execute()' pour executer l'une des requêtes stockée dans un dictionnaire.
	"""
	repertoire = input('Repertoire contenant les requete ? : ')		# Choix du répertoire contenant les requêtes
	if existe(repertoire) and not est_vide(repertoire):
		dico = lire(repertoire)                                     # création d'un dictionnaire à l'aide de la fonction précédente
		req = int(input("Quelle requete ? (commence à la requête 1, pas 01 ni 0) : "))	# choix de la requête, entier > 0
		if type(req) != int or req not in dico:
			print("Numéro de requetes invalide")
			return None
		if 'LIMIT' in dico[req][1]:									# Si la requête contient une limite on l'execute directement
			execute(dico[req][1], dico[req][0])
		else:
			execute(dico[req][1] + 'LIMIT 10', dico[req][0]) 		# Sinon, on ajoute une limite de 10 éléments maximum avant de l'executer à l'aide de la fonction 'execute()'
	else:
		print("Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe. Si l'orthographe est correcte, verifiez que le repertoire n'est pas vide.")

##############################################################
# 						Affichage 							 #
##############################################################


def afficher_table(table, titre =""):
	"""
	Affiche une table.
	Cette fonction était demandée dans le sujet.
	On peut avoir un affichage en console ou dans une fenêtre tkinter
	Cependant, on la redéfini ci-dessous.
	Auteurs: M CHOUCHI
	Arguments:
		table: une liste de tuples
		titre: str du titre à afficher avant la table
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

