from django.urls import path
from . import views


app_name = 'Dashboard'
urlpatterns = [
    path('', views.index , name = "dashboard"),

    #path('storesfilter/<str:strfilter>',views.index,name='stfier')
    
]