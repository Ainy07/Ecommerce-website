from django.shortcuts import render
from django.http.response import HttpResponse
from . models import *

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def contact_us(request):
   
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        u=person.objects.create(name=name,email=email,subject=subject,message=message)
        return render(request,"contact.html")