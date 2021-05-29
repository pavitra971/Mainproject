from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("",views.index,name='App'),
    path("buy",views.buy,name='buy'),
    path("rent",views.rent,name='rent'),
    path("sell",views.sell,name='sell'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about')



]