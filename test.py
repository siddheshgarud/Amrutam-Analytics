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


client = MongoClient()
client = MongoClient('localhost', 27017)
mydb = client["Amrutamdjango2"]
mycol = mydb["orders"]

print(datetime.datetime.today().weekday())

AllOrders = wcapi.get("customers", params = {'per_page' : "10" }).json()

dict2 = []

""" for x_Dict in AllOrders:
  record = {

                
                '_id': x_Dict['id'],
                'Customer First Name': x_Dict['shipping']['first_name'],
                'Customer Last Name': x_Dict['shipping']['last_name'],
                'Customer First Name': x_Dict['billing']['first_name'],
                'Customer Last Name': x_Dict['billing']['last_name'],
                'Email': x_Dict['billing']['email'],
                'Email': x_Dict['email'],
                'Phone': x_Dict['billing']['phone'][-10:],
                'City': x_Dict['shipping']['city'],
                'State': x_Dict['shipping']['state'],
                'Pincode': x_Dict['shipping']['postcode'],
                'City': x_Dict['billing']['city'],
                'State': x_Dict['billing']['state'],
                'Pincode': x_Dict['billing']['postcode'],
                'created_at': x_Dict['date_created'],
                }
  mycol.insert_one(record) """

print(mycol.find_one(  { "Customer First Name": "Mariam George"}))

  

"""


dict_orders = eval(AllOrders.text)
dict = []

k=0
for k,i in  enumerate(dict_orders) : 

    print(k+1)
    print(i["id"])
    print(i["date_created"])
    for j in i["line_items"]:
        print("name",j["name"])
        dict.append(j["name"])
    print(i["billing"]["first_name"])
    
    print("/n") 


y = json.dumps(dict)
print(y)
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
mycol.insert_one(data)

print(data)
print(dict2) """