from django.shortcuts import render

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