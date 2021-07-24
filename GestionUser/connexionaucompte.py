#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import sys
import hashlib

print("*******************************************")
print("*                                         *")
print("*        Connexion à votre compte         *")
print("*                                         *")
print("*******************************************")


############## Connexion à la base de donnée ############
try:
   conn = mysql.connector.connect(host="localhost", user="root", password="", database="bibliotheque")
   cursor = conn.cursor()
   print("Connexion à la base de donnée Réussi\n")
   
   try: 
  ############## Entrez des logins ############
       print("Connexion à votre compte :")
       login=input("login : ")

       while login== "":
          print("Veuillez saisir un login")
          login=input("login : ")
          
       print("")
       password=(input("Password : "))
       print("")
       mdp_hashe=hashlib.md5(password.encode()).hexdigest()
       
       try:
############## Connexion avec les logins ############
          res = cursor.execute('SELECT * FROM user WHERE login LIKE \'%'  + login + '%\'')
          res = cursor.fetchone()

          if res[4]==mdp_hashe:
             print("connexion reussi \n")
          else:
             print("Erreur de Connexion")
            
       except:
           print("Erreur de Connexion\n")
           
   except:
       # En cas d'erreur on annule les modifications
       conn.rollback()
       
except mysql.connector.errors.InterfaceError as e:
   print("Error %d: %s" % (e.args[0],e.args[1]))
   sys.exit(1)






