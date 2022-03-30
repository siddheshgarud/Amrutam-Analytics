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

""" n = 305

while n < 400:
    n += 1
    print(n)
    customers_all = wcapi.get('orders', params={  # 'page':11,
    'page': n,
    'per_page': 100,
    'order': 'asc',
    'orderby': 'date',
    })
if db({'id': x_Dict['id']}, limit=1) \
            != 0:
            print (true, 'Value already Exists')
        else:

if db (has Id=id) != 0 
print ('Value already exitst) 

elsE: 
for 
msql db - > insert """




sql = "INSERT IGNORE INTO dashboard_products (id , name, slug, permalink,date_created_gmt ,date_modified_gmt, type ,status,featured, catalog_visibility, short_description, sku ,price, regular_price, sale_price, date_on_sale_from_gmt, date_on_sale_to_gmt ,on_sale,  price_html, purchasable , total_sales, downloadable, tax_status, stock_quantity, backorders, backorders_allowed, backordered, manage_stock ,stock_status, sold_individually, weight,  average_rating, reviews_allowed ,rating_count 	) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s ,%s , %s , %s ,%s , %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s ,%s , %s , %s ,%s,%s ,%s )"

37

n = 0
m = 999999
x = 100
while (n < m) and ( x != None) :
    n += 1
    AllOrders = wcapi.get("products", params = {'per_page' : x , 'page': n }).json() 
    for x_Dict in AllOrders:

      val = ( x_Dict['id'],x_Dict['name'],x_Dict['slug'],x_Dict['permalink'],x_Dict['date_created_gmt'],x_Dict['date_modified_gmt'],x_Dict['type'],x_Dict['status'],x_Dict['featured'],x_Dict['catalog_visibility'],x_Dict['short_description'],x_Dict['sku'],x_Dict['price'],x_Dict['regular_price'],x_Dict['sale_price'],x_Dict['date_on_sale_from_gmt'],x_Dict['date_on_sale_to_gmt'],x_Dict['on_sale'],x_Dict['price_html'],x_Dict['purchasable'],x_Dict['total_sales'],x_Dict['downloadable'],x_Dict['tax_status'],x_Dict['stock_quantity'],x_Dict['backorders'],x_Dict['backorders_allowed'],x_Dict['backordered'],x_Dict['manage_stock'],x_Dict['stock_status'],x_Dict['sold_individually'],x_Dict['weight'],x_Dict['average_rating'],x_Dict['reviews_allowed'],x_Dict['rating_count'])
      db.execute(sql, val)
      mydb.commit()
      print(db.rowcount, "record inserted.")

    print(n)
    




  
  