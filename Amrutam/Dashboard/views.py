from django.shortcuts import render
import json
from .models import Orders as orders_model

import random
from django.db.models import Count
import pickle

def index(request):
    orders =  orders_model.objects.all()
    """ orderscount = orders.count()
    ordersstatussuccesscount = orders.filter(Status='success').count()
    ordersstatusfailedcount = orders.filter(Status='failed').count()
    ordersstatusprocount =  orders.filter(Status='processing').count()
    ordersstatuspendingcount =  orders.filter(Status='pending').count()
    ordersstatusholdcount =  orders.filter(Status='on-hold').count() """
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
    context = {'orders': orders , }
    return render(request,'Dashboard/index.html' , context)