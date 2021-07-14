from django.shortcuts import render
from oauth2client import client
from .models import Contact
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
import pandas as pd


scope= ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds= ServiceAccountCredentials.from_json_keyfile_name('itsp-319406-e1a72ffe4e53.json', scope)
client = gspread.authorize(creds)

# Create your views here.
def index(request):
    return render(request,'index.html')
def buy(request):
    return render(request,'buy.html')
def rent(request):
    return render(request,'rent.html')
def sell(request):
    return render(request,'sell.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":


        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    
    return render(request,'contact.html')

def result(request):
    #the extra info page
    

    
    location=request.GET['location']
    BHK=request.GET['BHK']
    sheet=client.open("Super_market").sheet1
    col=sheet.col_values(2)
    i=1
    for item in col:
        i=i+1
        if item == str(location):
            j=i-1

    shop=sheet.cell(j,4).value
    school=sheet.cell(j,5).value
    hospital=sheet.cell(j,6).value
    res= []
    res.append(shop)
    res.append(school)
    res.append(hospital)

    return render(request, 'result.html', {'result': res})


        #the price-prediction
   # x=client.open("independent_variable").sheet1
   # y=client.open("dependent_variable").sheet1