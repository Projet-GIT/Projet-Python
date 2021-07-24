#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys
import hashlib

############## Création de la table si elle n'existe pas ############

sql_create = """
CREATE TABLE IF NOT EXISTS User (
   iduser int(5) NOT NULL,
   firstname varchar(10) NOT NULL,
   lastname varchar(10) DEFAULT NULL,
   role varchar(2) DEFAULT NULL,
   password varchar(250) DEFAULT NULL,
   region varchar(3) DEFAULT NULL,
   login varchar(10) DEFAULT NULL,
   PRIMARY KEY(iduser) ); """

############## Création de l'utilisateur avec gestion du mot de passe ############
print("*******************************************")
print("*                                         *")
print("*        Création de votre compte         *")
print("*                                         *")
print("*******************************************")


user={}
print("Création d'un utilisateur : ")
print("")
user["iduser"]=(input("Id User : "))
print("")
user["firstname"]=(input("Prénom : "))
print("")
user["lastname"]=(input("Nom : "))
print("")
user["role"]=(input("Role : "))
print("")

mdp=input("Entrez le mot de passe:")
mdp_hashe=hashlib.md5(mdp.encode()).hexdigest()
user["password"]=(mdp_hashe)
print("")

user["region"]=(input("Region : "))
print("")
user["login"]=(input("Login (Max 10 caractères): "))

print(user)

if user["role"]== "AC":
    print("Déjà '3' AC crée!")
    exit(5)
else:
    pass

############## Ajout de l'utilisateur dans la base de donnée ############

try:
   conn = mysql.connector.connect(host="localhost", user="root", password="", database="bibliotheque")
   cursor = conn.cursor()
   cursor.execute(sql_create)
   print("Connexion à la base de donnée Réussi\n")

   try:
      print(user)
      #user = {'iduser': 12345, 'firstname' : "Matteo", 'lastname' : "Lopes", 'role' : "AS"}
      cursor.execute("""INSERT INTO User (iduser, firstname, lastname, role, password, region, login) VALUES(%(iduser)s, %(firstname)s, %(lastname)s, %(role)s, %(password)s, %(region)s, %(login)s)""", user)
      conn.commit()
      print("Utilisateur Crée avec succès\n")
   except:
      # En cas d'erreur on annule les modifications
      conn.rollback()

except mysql.connector.errors.InterfaceError as e:
   print("Error %d: %s" % (e.args[0],e.args[1]))
   sys.exit(1)

finally:
   # On ferme la connexion
   if conn:
      conn.close()
