from django.shortcuts import render
from oauth2client import client
from .models import Contact
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
import pandas as pd
import joblib
import csv

mj=joblib.load('./model/ML_model_joblib.pkl')


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


def predict(location, sqft, bath, bhk):
    with open("IndependentVariable.csv" , 'r') as csvfile:
        X=csv.reader(csvfile)   
    sheet=client.open("independent _variable").sheet1
    row_1=sheet.row_values(1)
    a=-1
    for item in row_1:
        a=a+1
        if item == str(location):
            j=a-1
    loc_index=j    

  #  loc_index = np.where(X.columns==location)[0][0]
    
    x = np.zeros(243)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        
  #  print([x])
    y= mj.predict([x])
    a=y[0]
    return a

def result(request):
    #the extra info page
    

    
    location=request.GET['location']
    BHK=request.GET['BHK']
    sqft=request.GET['squarefeet']
    bath=request.GET['Bath']
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
    price=predict(location,sqft,bath,BHK)
    price=price*100/84.4
    price_rounded= round(price,2)
    price_lower= price_rounded - (7/100*price_rounded)
    price_upper =price_rounded + (7/100*price_rounded)
    price_lower_rounder= round(price_lower,2)
    price_upper_rounded= round(price_upper,2)
    res.append(price_lower_rounder)
    res.append(price_upper_rounded)


    return render(request, 'result.html', {'result': res})


