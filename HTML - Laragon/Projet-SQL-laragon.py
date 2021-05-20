#!C:\Python39\python.exe
#!C:\Winpython\python-3.8.5.amd64\python.exe
#MANGIN Raphaël
#20/05/2021
"""
Important : j'ai volontairement retiré les requêtes n°2 et n°10 car comme elle mettait du temps à afficher le résultat, laragon plantait. Merci de votre compréhension.
"""

import sqlite3
import os

##############################################################
#						Menu 								 #
##############################################################

def menu(rep):
	"""
	Menu affichant les requêtes contenues dans le répertoire 'rep' placé en paramètre sous forme de boutons.
	"""
	n = len(rep)
	#Initialisation de la page html
	print("Content-type: text/html")
	print("\n")
	print("<html><head>")
	print("\n")
	print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
	print("</head><body>")
	print(" <h2> Choisir la requete :</h2>")
	
	for i in range(1,n+1):								# Crée un bouton pour chaque requête qui affiche le résultat en dessous de celui-ci lorsque l'on clic dessus 
		execution = "'"+str(execute_sql_html(rep[str(i)][1]))+"'"
		requete = "' "+str(i)+" '"
		print("\n")
		print(' <button type="button"')
		print('onclick="document.getElementById(',requete,').innerHTML =',execution,'">')
		print(rep[str(i)][0],"</button>\n")
		print(' <p id="',i,'"></p>')
	print("\n</body>\n</html>")				#fin du code html


##############################################################
#						Lecture							 	 #
##############################################################

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
		dct = {str(cle):valeur for cle,valeur in tab}					# Convertit le tableau 'tab' en dictionnaire :
		return dct													# Clé : entier > 0   ; Valeur : liste de type [titre de la requête, requête elle-même]	
	else:
		return "Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe."

##############################################################
#						HTML								 #
##############################################################
""" 
Ce code sert à executer le programme dans une page Web
"""

def execute_sql_html(sql):
	
		
		if os.path.basename(os.getcwd()) == 'requetes':			# On se replace dans le bon répertoire
			os.chdir('C:/laragon/www/python')
		connexion = sqlite3.connect('imdb.db')
		cur = connexion.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		table = "<table>"
		for row in rows:										# Cette boucle execute la requête et affiche son résultat sous forme de tableau
			for i in range(len(row)):
				table += "<td>"+str(row[i])+ "</td>"
			table += "<tr></tr>"
		table += "</table>"
		return table

def execution_html():

    repertoire = 'requetes'											# Choix du répertoire contenant les requêtes
    if existe(repertoire) and not est_vide(repertoire):
        dico = lire(repertoire)   
        menu(dico)  							    # création d'un dictionnaire à l'aide de la fonction précédente
    else:
        print("Ce repertoire n'existe pas ou est introuvable, veuillez verifier l'orthographe. Si l'orthographe est correcte, verifiez que le repertoire n'est pas vide.")

##############################################################
#						Execution							 #
##############################################################

execution_html()       #Sert à executer le code

