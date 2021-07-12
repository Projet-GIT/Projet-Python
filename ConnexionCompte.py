#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import sys
import hashlib

conn = mysql.connector.connect(host="localhost", user="root", password="", database="bibliotheque")
cursor = conn.cursor()
print("Connexion à la base de donnée Réussi\n")

iduser=(input("Id User : "))
print("")
res = cursor.execute('SELECT * FROM user WHERE iduser LIKE \'%'  + iduser + '%\'')
res = cursor.fetchone()

if res == None :
    print ("erreur")
else:
    print(res)

print(res[4])
print("")

password=(input("Password : "))
print("")
mdp_hashe=hashlib.md5(password.encode()).hexdigest()

if res[4]== mdp_hashe:
    print("connexion reussi")
else:
    print("ERROR")




