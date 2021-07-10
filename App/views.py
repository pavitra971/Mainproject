from django.shortcuts import render
from .models import Contact

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