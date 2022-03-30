from django.shortcuts import render
import json
from .models import Orders as orders_model
import datetime
import random
from django.db.models import Count
import pickle

def index(request):
    orders =  orders_model.objects.all()
    orderscount = orders.count()
    ordersstatussuccesscount = orders.filter(status='completed').count()
    ordersstatusfailedcount = orders.filter(status='cancelled').count()
    ordersstatusprocount =  orders.filter(status='processing').count()
    ordersstatuspendingcount =  orders.filter(status='pending').count()
    ordersstatusholdcount =  orders.filter(status='on-hold').count() 
    today = datetime.date.today()
    first = today.replace(day=1)
    second = first.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)




    latesttenorders = orders.order_by('-id')[:10]
    """ print(lastlastMonth.strftime("%B")) """
    """ print(ordersstatusfailedcount) """
    """ ordersstatusprocount = 0
    ordersstatusfailedcount = 0
    for i in orders:
        if(i.Status == "processing"):
            ordersstatusprocount = ordersstatusprocount +1
        elif(i.Status == "failed"):
            ordersstatusfailedcount = ordersstatusfailedcount +1
        else:
            print(i.Status) """
    context = {'orders': orders ,  'orderscount': orderscount , 'ordersstatussuccesscount':ordersstatussuccesscount  , 'ordersstatusfailedcount':ordersstatusfailedcount , 'ordersstatusprocount':ordersstatusprocount  , 'latesttenorders': latesttenorders }
    return render(request,'Dashboard/index.html' , context)