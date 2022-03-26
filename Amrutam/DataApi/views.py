from django.shortcuts import render
from woocommerce import API
from pymongo import MongoClient
import time
import datetime
import pymongo
import matplotlib.pyplot as plt
import json
import requests

null = None
false = False
true  = True 

wcapi = API(url='https://www.amrutam.co.in/',
            consumer_key='ck_b976d7eead635d135905eaf95a6dcef8055a88d2',
            consumer_secret='cs_5c6ae65ea81ec59c495f498ac01b04aafeeadc01'
            , version='wc/v3', timeout=600)


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port= '3306',
  user="root",
  password="",
  database="amrutamdjango"
)

db = mydb.cursor()




""" db.execute("CREATE TABLE cuu (name VARCHAR(255), address VARCHAR(255))") """
""" db.execute("ALTER TABLE customers ADD COLUMN First_Name VARCHAR(50)") """

AllOrders = wcapi.get("orders", params = {'per_page' : "100" }).json()

sql = "INSERT INTO orders (id ,First_Name,Last_Name,Email,Phone,City,Pincode,State,address,created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)"
for x_Dict in AllOrders:
  val = ( x_Dict['id'],x_Dict['shipping']['first_name'], x_Dict['shipping']['last_name'], x_Dict['billing']['email'], x_Dict['billing']['phone'][-10:], x_Dict['shipping']['city'],x_Dict['billing']['postcode'], x_Dict['shipping']['state'],  x_Dict['shipping']['address_1'], x_Dict['date_created'])
  db.execute(sql, val)
  mydb.commit()
  print(db.rowcount, "record inserted.")
  
