#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys

sql = "INSERT INTO User (iduser, firstname,lastname,role) VALUES (%d, %s, %s, %s)"
val = (12345, "Matteo", "Lopes", "AS")

sql_create = """
CREATE TABLE IF NOT EXISTS User ( 
   iduser int(5) NOT NULL,
   firstname varchar(10) NOT NULL, 
   lastname varchar(10) DEFAULT NULL, 
   role varchar(2) DEFAULT NULL,  
   PRIMARY KEY(iduser) ); """
try:
   conn = mysql.connector.connect(host="localhost", user="root", password="", database="bibliotheque")
   cursor = conn.cursor()
   cursor.execute(sql_create)
   
   try:

      user = {'iduser': 12345, 'firstname' : "Matteo", 'lastname' : "Lopes", 'role' : "AS"} 
      cursor.execute("""INSERT INTO User (iduser, firstname, lastname, role) VALUES(%(iduser)s, %(firstname)s, %(lastname)s, %(role)s)""", user)
      conn.commit()
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

