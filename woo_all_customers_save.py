#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

# import urllib2

import json
from datetime import datetime, time
from dateutil.parser import parse
import pymongo
import dns
from woocommerce import API
import time

null = None
false = False
true = True

wcapi = API(url='https://www.amrutam.co.in/',
            consumer_key='ck_b976d7eead635d135905eaf95a6dcef8055a88d2',
            consumer_secret='cs_5c6ae65ea81ec59c495f498ac01b04aafeeadc01'
            , version='wc/v3', timeout=600)

# order_all = wcapi.get('orders', params={
#         # 'page': n,
#         'per_page': 100,
#         'order': 'asc',
#         'orderby': 'date',
#         'status': 'completed',
#         'after': '2021-03-01T20:06:18'
#         })

    # https://meet.google.com/wpc-wtav-ion
    # print('page: ', n)

# Dict_orders = eval(order_all.text)
# for idx, x_Dict in enumerate(Dict_orders):
#     print(x_Dict['id'], x_Dict['billing']['first_name'], x_Dict['billing']['email'], x_Dict['date_created'])

n = 305
date
while n < 400:
    n += 1
    print(n)

    # order_all = wcapi.get('orders', params={
    #     'page': n,
    #     'per_page': 100,
    #     'order': 'asc',
    #     'orderby': 'date',
    #     'status': 'completed',
    #     })
    # print('page: ', n)

    customers_all = wcapi.get('customers', params={  # 'page':11,
        'page': n,
        'per_page': 100,
        'order': 'asc',
        'orderby': 'registered_date',
        })

# https://meet.google.com/wpc-wtav-ion
# print('page: ', n)

    Dict_customers = eval(customers_all.text)

    # print(Dict_customers)

    client = \
        pymongo.MongoClient('mongodb+srv://amrutam:amrutam129@cluster0.3th9u.mongodb.net/test'
                            )
    mydb = client['Woocomerce_aws']
    woo_customer_db = mydb.woo_all_customers

    # END ----

    db_get = client.get_database('Woocomerce_aws')
    record_get = db_get.woo_all_customers

    # x_Dict['billing']['first_name'], x_Dict['billing']['last_name'], x_Dict['billing']['email'], x_Dict['billing']['phone'], x_Dict['date_created']

    # END ----

    for (idx, x_Dict) in enumerate(Dict_customers):
        print (
            x_Dict['id'],
            x_Dict['billing']['first_name'],
            x_Dict['billing']['last_name'],
            x_Dict['billing']['email'],
            x_Dict['billing']['phone'],
            x_Dict['date_created'],
            )
        if record_get.count_documents({'_id': x_Dict['id']}, limit=1) \
            != 0:
            print (true, 'Value already Exists')
        else:

            # print ('Email: ', x_Dict['billing']['email'], 'date Created', x_Dict['date_created'], 'Order Status: ', x_Dict['status'])

            fmt = '%Y-%m-%dT%H:%M:%S'
            date_created = parse(x_Dict['date_created']).strftime('%s')
            print ('Time in epcoh', date_created)

            record = {
                '_id': x_Dict['id'],
                'Customer First Name': x_Dict['billing']['first_name'],
                'Customer Last Name': x_Dict['billing']['last_name'],
                'Email': x_Dict['billing']['email'],
                'Phone': x_Dict['billing']['phone'],
                'City': x_Dict['billing']['city'],
                'State': x_Dict['billing']['state'],
                'Pincode': x_Dict['billing']['postcode'],
                'created_at': x_Dict['date_created'],
                }

            jsonData = json.dumps(record)
            woo_customer_db.insert_one(record)
            print (type(record), 'Record Inserted: ', idx)

            if (idx + 1) % 100 == 0:
                print('------YAY!!!-------DID 100')
                print ('New Value, successfully inserted the record')
            else:

                # print('page: ', n)

                print(idx)
