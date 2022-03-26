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










sql = "INSERT IGNORE INTO dashboard_orders (id , email , phone ,number,status , order_key , created_via , currency , payment_method , payment_method_title ,transaction_id	,date_paid_gmt , discount_total , discount_tax , shipping_tax , shipping_total , total_tax, total ,  date_created ,date_modified_gmt , customer_id , line_items_id	) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s ,%s , %s , %s ,%s,%s,%s , %s , %s , %s, %s)"



n = 0
m = 2000
x = 100
while (n < m) and ( x != None) :
    n += 1
    AllOrders = wcapi.get("orders", params = {'per_page' : x , 'page': n }).json() 
    for x_Dict in AllOrders:

      val = ( x_Dict['id'],x_Dict['billing']['email'] ,x_Dict['billing']['phone']  ,x_Dict['number'],x_Dict['status'],x_Dict['order_key'],x_Dict['created_via'],x_Dict['currency'],x_Dict['payment_method'],x_Dict['payment_method_title'],x_Dict['transaction_id'],x_Dict['date_paid_gmt'],x_Dict['discount_total'],x_Dict['discount_tax'],x_Dict['shipping_tax'],x_Dict['shipping_total'],x_Dict['total_tax'],x_Dict['total'],x_Dict['date_created'],x_Dict['date_modified_gmt'],x_Dict['customer_id'],x_Dict['number'])
      db.execute(sql, val)
      mydb.commit()
      print(db.rowcount, "record inserted.")

    print(n)



  
  