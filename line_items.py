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










sql = "INSERT IGNORE INTO dashboard_line_items (id  ,	p_id ,	sku , name, variation_id , quantity , tax_class , 	address1,address2	,pincode, city	 , 	state , country , is_paying_customer , avatar_url, date_created_gmt ,  date_modified_gmt 	) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s ,%s , %s , %s ,%s,%s)"



n = 0
m = 999999
x = 100
while (n < m) and ( x != None) :
    n += 1
    AllOrders = wcapi.get("orders", params = {'per_page' : x , 'page': n }).json() 
    for x_Dict in AllOrders:

      val = ( x_Dict['id'],x_Dict['username'],x_Dict['first_Name'],x_Dict['last_Name'],x_Dict['role'],x_Dict['email'],x_Dict['phone'],x_Dict['address1'],x_Dict['address2'],x_Dict['pincode'],x_Dict['city'],x_Dict['state'],x_Dict['country'],x_Dict['is_paying_customer'],x_Dict['avatar_url'],x_Dict['date_created_gmt'],x_Dict['date_modified_gmt'],x_Dict['address2'],x_Dict['date_created'],x_Dict['date_modified_gmt'],x_Dict['customer_id'],x_Dict['number'])
      db.execute(sql, val)
      mydb.commit()
      print(db.rowcount, "record inserted.")

    print(n)
    time.sleep(5)




  
  